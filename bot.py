#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deutsch Bot - English -> German translation practice
Stack: python-telegram-bot 20.7, asyncpg (PostgreSQL on Railway), aiohttp (Gemini + health)

Flow:
  /start -> register (name, first time only) -> choose level (A1..B2)
         -> choose topic (Greeting + 21 LWL topics) -> 40 sentences easy->hard
         -> type German -> AI feedback (English) -> next sentence
Content for each (topic x level) is generated once by Gemini on first entry,
then cached in the DB so everyone else reads it from there.
"""

import os
import re
import json
import asyncio
import logging
from datetime import datetime, timezone
from typing import List, Dict, Optional, Tuple

import asyncpg
import aiohttp
from aiohttp import web
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.constants import ChatAction
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
log = logging.getLogger("deutschbot")

# Pre-authored lessons (grammar/vocab note + questions). Lessons not listed here
# fall back to AI generation, so nothing breaks while content is being written.
try:
    from lessons import LESSONS
except Exception:  # noqa: BLE001
    LESSONS = {}

# ----------------------------- Config -----------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
DATABASE_URL = os.environ.get("DATABASE_URL", "")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
PORT = int(os.environ.get("PORT", "8080"))
ADMIN_ID = int(os.environ.get("ADMIN_ID", "0") or "0")  # your numeric Telegram ID, for new-user alerts

GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
GEMINI_MODELS = ["gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-flash-latest"]

LEVELS = ["A1", "A2", "B1", "B2"]
SENTENCES_PER_TOPIC = 40

# topic_key, display title  (Greeting + 21 LWL chapters)
TOPICS: List[Tuple[str, str]] = [
    ("greeting", "Greeting"),
    ("holiday", "Holiday"),
    ("relationship", "Relationship"),
    ("technology", "Technology"),
    ("sports", "Sports"),
    ("food", "Food"),
    ("education", "Education"),
    ("work", "Work"),
    ("health", "Health"),
    ("books_films", "Books and Films"),
    ("accommodation", "Accommodation"),
    ("clothes_fashion", "Clothes & Fashion"),
    ("personality", "Personality"),
    ("business", "Business"),
    ("physical_appearance", "Physical Appearance"),
    ("town_city", "Town and City"),
    ("music", "Music"),
    ("weather", "Weather"),
    ("shopping", "Shopping"),
    ("environment", "Environment"),
    ("advertising", "Advertising"),
    ("government", "Government"),
]
TOPIC_TITLE = {k: v for k, v in TOPICS}

# German grammar woven INTO the sentences at each level (invisible to the user)
GRAMMAR_HINTS = {
    "A1": "Praesens, sein/haben, Akkusativ, basic SVO word order, definite/indefinite articles, "
          "simple negation (nicht/kein), numbers, very common everyday vocabulary. Keep sentences short and simple.",
    "A2": "Perfekt (haben/sein + Partizip II), Dativ, separable verbs (trennbare Verben), "
          "modal verbs (koennen/muessen/wollen/duerfen), comparatives, time and sequence expressions, possessives.",
    "B1": "Praeteritum, subordinate clauses (weil/dass/wenn/obwohl), two-way prepositions (Wechselpraepositionen), "
          "reflexive verbs, comparative and superlative, basic relative clauses, connectors.",
    "B2": "Konjunktiv II (wuerde/haette/waere), Passiv (Vorgangs- und Zustandspassiv), advanced relative clauses, "
          "Genitiv, adjective declension, nominalization, connectors (deshalb, trotzdem, je...desto). "
          "Use longer, more complex sentences.",
}

# ----------------------------- Database -----------------------------
pool: Optional[asyncpg.Pool] = None

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    telegram_id    BIGINT PRIMARY KEY,
    name           TEXT,
    username       TEXT,
    last_seen      TIMESTAMPTZ,
    active_seconds BIGINT DEFAULT 0,
    created_at     TIMESTAMPTZ DEFAULT now()
);
CREATE TABLE IF NOT EXISTS topic_content (
    topic_key  TEXT NOT NULL,
    level      TEXT NOT NULL,
    sentences  JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    PRIMARY KEY (topic_key, level)
);
CREATE TABLE IF NOT EXISTS user_progress (
    telegram_id   BIGINT NOT NULL,
    topic_key     TEXT NOT NULL,
    level         TEXT NOT NULL,
    current_index INT NOT NULL DEFAULT 0,
    completed     BOOLEAN NOT NULL DEFAULT FALSE,
    updated_at    TIMESTAMPTZ DEFAULT now(),
    PRIMARY KEY (telegram_id, topic_key, level)
);
ALTER TABLE users ADD COLUMN IF NOT EXISTS username TEXT;
ALTER TABLE users ADD COLUMN IF NOT EXISTS last_seen TIMESTAMPTZ;
ALTER TABLE users ADD COLUMN IF NOT EXISTS active_seconds BIGINT DEFAULT 0;
"""


async def init_db():
    global pool
    pool = await asyncpg.create_pool(dsn=DATABASE_URL, min_size=1, max_size=5)
    async with pool.acquire() as con:
        await con.execute(SCHEMA)
    log.info("DB ready")


async def get_user(tg_id: int):
    async with pool.acquire() as con:
        return await con.fetchrow("SELECT * FROM users WHERE telegram_id=$1", tg_id)


async def create_user(tg_id: int, name: str, username: Optional[str] = None):
    async with pool.acquire() as con:
        await con.execute(
            "INSERT INTO users (telegram_id, name, username, last_seen) VALUES ($1,$2,$3, now()) "
            "ON CONFLICT (telegram_id) DO UPDATE SET name=$2, username=$3",
            tg_id, name, username,
        )


async def touch_user(tg_id: int):
    """Update last_seen and accumulate active time (gaps capped at 10 minutes)."""
    async with pool.acquire() as con:
        await con.execute(
            "UPDATE users SET "
            "active_seconds = COALESCE(active_seconds, 0) + "
            "LEAST(COALESCE(EXTRACT(EPOCH FROM (now() - last_seen))::bigint, 0), 600), "
            "last_seen = now() "
            "WHERE telegram_id = $1",
            tg_id,
        )


async def get_content(topic_key: str, level: str) -> Optional[List[Dict]]:
    async with pool.acquire() as con:
        row = await con.fetchrow(
            "SELECT sentences FROM topic_content WHERE topic_key=$1 AND level=$2",
            topic_key, level,
        )
    if not row:
        return None
    data = row["sentences"]
    if isinstance(data, str):  # asyncpg returns jsonb as str by default
        data = json.loads(data)
    return data


async def save_content(topic_key: str, level: str, sentences: List[Dict]):
    async with pool.acquire() as con:
        await con.execute(
            "INSERT INTO topic_content (topic_key, level, sentences) VALUES ($1,$2,$3) "
            "ON CONFLICT (topic_key, level) DO UPDATE SET sentences=$3",
            topic_key, level, json.dumps(sentences, ensure_ascii=False),
        )


async def get_progress(tg_id: int, topic_key: str, level: str) -> Tuple[int, bool]:
    async with pool.acquire() as con:
        row = await con.fetchrow(
            "SELECT current_index, completed FROM user_progress "
            "WHERE telegram_id=$1 AND topic_key=$2 AND level=$3",
            tg_id, topic_key, level,
        )
    if row:
        return row["current_index"], row["completed"]
    return 0, False


async def save_progress(tg_id: int, topic_key: str, level: str, idx: int, completed: bool):
    async with pool.acquire() as con:
        await con.execute(
            "INSERT INTO user_progress (telegram_id, topic_key, level, current_index, completed, updated_at) "
            "VALUES ($1,$2,$3,$4,$5, now()) "
            "ON CONFLICT (telegram_id, topic_key, level) "
            "DO UPDATE SET current_index=$4, completed=$5, updated_at=now()",
            tg_id, topic_key, level, idx, completed,
        )


async def progress_map(tg_id: int, level: str) -> Dict[str, Tuple[int, bool]]:
    async with pool.acquire() as con:
        rows = await con.fetch(
            "SELECT topic_key, current_index, completed FROM user_progress "
            "WHERE telegram_id=$1 AND level=$2",
            tg_id, level,
        )
    return {r["topic_key"]: (r["current_index"], r["completed"]) for r in rows}


# ----------------------------- Gemini -----------------------------
async def gemini_chat(messages: List[Dict], max_tokens: int = 800, temperature: float = 0.7) -> Optional[str]:
    headers = {"Authorization": f"Bearer {GEMINI_API_KEY}", "Content-Type": "application/json"}
    timeout = aiohttp.ClientTimeout(total=120)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        for model in GEMINI_MODELS:
            payload = {
                "model": model,
                "messages": messages,
                "max_tokens": max_tokens,
                "temperature": temperature,
            }
            try:
                async with session.post(GEMINI_URL, json=payload, headers=headers) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        return data["choices"][0]["message"]["content"]
                    if resp.status in (429, 500, 502, 503):
                        log.warning("Gemini %s -> %s, trying next model", model, resp.status)
                        continue
                    txt = await resp.text()
                    log.error("Gemini %s error %s: %s", model, resp.status, txt[:200])
                    continue
            except Exception as e:  # noqa: BLE001
                log.error("Gemini %s exception: %s", model, e)
                continue
    return None


def _extract_json_array(text: str):
    t = text.strip()
    if t.startswith("```"):
        t = t.strip("`")
        if t[:4].lower() == "json":
            t = t[4:]
    start, end = t.find("["), t.rfind("]")
    if start != -1 and end != -1 and end > start:
        t = t[start:end + 1]
    return json.loads(t)


async def generate_sentences(topic_key: str, level: str) -> List[Dict]:
    title = TOPIC_TITLE[topic_key]
    hints = GRAMMAR_HINTS[level]
    prompt = (
        f"You are a German-language curriculum designer.\n"
        f"Create EXACTLY {SENTENCES_PER_TOPIC} English sentences that a learner will translate into German.\n\n"
        f"Topic: {title}\n"
        f"CEFR level: {level}\n"
        f"Grammar and vocabulary for this level: {hints}\n\n"
        f"Rules:\n"
        f"- Every sentence must fit the topic '{title}' and the level {level}.\n"
        f"- Order them from EASIER to HARDER (sentence 1 easiest, sentence {SENTENCES_PER_TOPIC} hardest).\n"
        f"- Naturally embed the level's grammar so translating each sentence practises that grammar.\n"
        f"- Use natural, useful, everyday English.\n"
        f"- Provide an accurate, natural reference German translation for each.\n\n"
        f"Return ONLY a valid JSON array of {SENTENCES_PER_TOPIC} objects. No markdown, no comments.\n"
        f'Format: [{{"en": "English sentence", "de": "German translation", '
        f'"focus": "short English note on the grammar/vocab practised"}}]'
    )
    for attempt in range(2):
        raw = await gemini_chat([{"role": "user", "content": prompt}], max_tokens=6000, temperature=0.7)
        if not raw:
            continue
        try:
            data = _extract_json_array(raw)
            cleaned = []
            for item in data:
                en = (item.get("en") or "").strip()
                de = (item.get("de") or "").strip()
                focus = (item.get("focus") or "").strip()
                if en and de:
                    cleaned.append({"en": en, "de": de, "focus": focus})
            if len(cleaned) >= 30:
                return cleaned[:SENTENCES_PER_TOPIC]
            log.warning("generation gave only %s items (attempt %s)", len(cleaned), attempt)
        except Exception as e:  # noqa: BLE001
            log.error("parse generation failed (attempt %s): %s", attempt, e)
    return []


async def get_feedback(en: str, de_ref: str, user_answer: str, level: str) -> str:
    prompt = (
        f"You are a witty, super-casual German tutor - funny and warm, like a friend who teaches "
        f"German over a beer. You joke around and keep it light, but your corrections are always accurate.\n"
        f"The learner translated an English sentence into German.\n\n"
        f"English: {en}\n"
        f"Reference German (ONE valid option, not the only one): {de_ref}\n"
        f"Learner's answer: {user_answer}\n\n"
        f"Give SHORT, casual, funny feedback in ENGLISH, in this structure:\n"
        f"1) One playful verdict line: '✅ Nailed it!' / '⚠️ Soooo close' / '❌ Oof, let's fix this'\n"
        f"2) 'Correct version:' a natural correct German sentence (in German).\n"
        f"3) 1 to 3 short, light-hearted bullet notes on the key points (case/Fall, word order, verb "
        f"conjugation, articles, vocabulary). Humor is welcome, but keep the grammar correct and clear. "
        f"If it's perfect, hype them up.\n"
        f"4) Last line EXACTLY: '📊 Score: X/10'\n"
        f"Keep it short, friendly and fun. Accept correct paraphrases as correct even if different from "
        f"the reference. Tease gently - never insult or discourage."
    )
    raw = await gemini_chat([{"role": "user", "content": prompt}], max_tokens=700, temperature=0.7)
    if not raw:
        return "⚠️ Couldn't get feedback right now. Just send the same sentence again in a sec."
    return raw.strip()


# ----------------------------- Placement test -----------------------------
PLACEMENT_KEY = "__placement__"
PLACEMENT_LVL = "MIX"


async def generate_placement() -> List[Dict]:
    prompt = (
        "You are a German placement-test designer.\n"
        "Create EXACTLY 12 English sentences for a learner to translate into German, to assess "
        "their CEFR level. Use 3 sentences for EACH level, in this order: A1 (easiest), A2, B1, "
        "B2 (hardest). Go from easier to harder overall.\n"
        "For each sentence give: the English text, a natural reference German translation, and its level.\n"
        "Return ONLY a valid JSON array of 12 objects, no markdown, no comments:\n"
        '[{"en": "English sentence", "de": "German translation", "level": "A1"}]'
    )
    for attempt in range(2):
        raw = await gemini_chat([{"role": "user", "content": prompt}], max_tokens=2500, temperature=0.6)
        if not raw:
            continue
        try:
            data = _extract_json_array(raw)
            cleaned = []
            for item in data:
                en = (item.get("en") or "").strip()
                de = (item.get("de") or "").strip()
                lvl = (item.get("level") or "").strip().upper()
                if en and de and lvl in LEVELS:
                    cleaned.append({"en": en, "de": de, "level": lvl})
            if len(cleaned) >= 8:
                return cleaned
            log.warning("placement gen gave %s items (attempt %s)", len(cleaned), attempt)
        except Exception as e:  # noqa: BLE001
            log.error("placement parse failed (%s): %s", attempt, e)
    return []


async def grade_score(en: str, de_ref: str, user_answer: str) -> int:
    prompt = (
        "Rate how correct this German translation is, from 0 to 10 "
        "(10 = perfect, 0 = empty or totally wrong). Accept valid paraphrases as correct.\n"
        f"English: {en}\n"
        f"Reference German: {de_ref}\n"
        f"Learner's answer: {user_answer}\n"
        "Reply with ONLY a single integer from 0 to 10. No words, no punctuation."
    )
    raw = await gemini_chat([{"role": "user", "content": prompt}], max_tokens=10, temperature=0.0)
    if not raw:
        return 5
    m = re.search(r"\d+", raw)
    if not m:
        return 5
    return max(0, min(10, int(m.group())))


async def get_placement_set() -> List[Dict]:
    cached = await get_content(PLACEMENT_KEY, PLACEMENT_LVL)
    if cached:
        return cached
    fresh = await generate_placement()
    if fresh:
        await save_content(PLACEMENT_KEY, PLACEMENT_LVL, fresh)
    return fresh


# ----------------------------- Keyboards -----------------------------
LEVEL_TEST_BTN = "📊 Level Test"


def main_reply_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup([[LEVEL_TEST_BTN]], resize_keyboard=True)


def levels_keyboard() -> InlineKeyboardMarkup:
    rows, row = [], []
    for lv in LEVELS:
        row.append(InlineKeyboardButton(lv, callback_data=f"lvl:{lv}"))
        if len(row) == 2:
            rows.append(row); row = []
    if row:
        rows.append(row)
    return InlineKeyboardMarkup(rows)


def topics_keyboard(level: str, prog: Dict[str, Tuple[int, bool]]) -> InlineKeyboardMarkup:
    rows, row = [], []
    for key, title in TOPICS:
        idx, done = prog.get(key, (0, False))
        if done:
            label = f"✅ {title}"
        elif idx > 0:
            label = f"{title} ({idx})"
        else:
            label = title
        row.append(InlineKeyboardButton(label, callback_data=f"top:{level}:{key}"))
        if len(row) == 2:
            rows.append(row); row = []
    if row:
        rows.append(row)
    rows.append([InlineKeyboardButton("🔙 Levels", callback_data="back:levels")])
    return InlineKeyboardMarkup(rows)


def practice_keyboard(level: str, key: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("⏭ Skip", callback_data=f"skip:{level}:{key}"),
        InlineKeyboardButton("🔙 Topics", callback_data=f"back:topics:{level}"),
    ]])


def finished_keyboard(level: str, key: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔁 Restart", callback_data=f"restart:{level}:{key}")],
        [InlineKeyboardButton("🔙 Topics", callback_data=f"back:topics:{level}")],
    ])


# ----------------------------- Handlers -----------------------------
WELCOME = (
    "👋 Hi! Welcome to the German practice bot.\n\n"
    "You'll see English sentences and translate them into German, then get feedback "
    "on your grammar and vocabulary.\n\n"
    "First, what's your name?"
)


async def notify_admin(context: ContextTypes.DEFAULT_TYPE, tg_user, display_name: str):
    """Send the admin a heads-up when a new user joins."""
    if not ADMIN_ID or tg_user.id == ADMIN_ID:
        return
    uname = f"@{tg_user.username}" if tg_user.username else "(no username)"
    text = (
        f"🆕 New user joined!\n"
        f"Name: {display_name}\n"
        f"Username: {uname}\n"
        f"ID: {tg_user.id}"
    )
    try:
        await context.bot.send_message(chat_id=ADMIN_ID, text=text)
    except Exception as e:  # noqa: BLE001
        log.warning("could not notify admin: %s", e)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    tg_id = update.effective_user.id
    await touch_user(tg_id)

    user = await get_user(tg_id)
    if not user:
        # Always ask for a name on first entry. The @username and numeric ID are
        # captured automatically from the Telegram account at registration.
        context.user_data["mode"] = "register"
        await update.message.reply_text(WELCOME)
        return
    await update.message.reply_text(f"Hi {user['name']}! 🇩🇪", reply_markup=main_reply_kb())
    await show_levels(update, context)


async def show_levels(update: Update, context: ContextTypes.DEFAULT_TYPE, greeting: str = "Choose your level:"):
    text = f"{greeting}\n\nPick a level:"
    if update.callback_query:
        await update.callback_query.edit_message_text(text, reply_markup=levels_keyboard())
    else:
        await update.message.reply_text(text, reply_markup=levels_keyboard())


async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mode = context.user_data.get("mode")
    tg_id = update.effective_user.id
    await touch_user(tg_id)

    if (update.message.text or "").strip() == LEVEL_TEST_BTN:
        await start_placement(update, context)
        return

    if mode == "register":
        name = (update.message.text or "").strip()[:50] or "Freund"
        uname = update.effective_user.username
        await create_user(tg_id, name, uname)
        context.user_data["mode"] = None
        await notify_admin(context, update.effective_user, name)
        await update.message.reply_text(f"Welcome, {name}! ✅", reply_markup=main_reply_kb())
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("📊 Take placement test", callback_data="pl:start")],
            [InlineKeyboardButton("Skip - choose myself", callback_data="pl:skip")],
        ])
        await update.message.reply_text(
            "Want a quick placement test to find your level? (12 short translations)",
            reply_markup=kb,
        )
        return

    if mode == "placement":
        await handle_placement_answer(update, context)
        return

    if mode == "practice":
        await handle_answer(update, context)
        return

    await update.message.reply_text("Send /start to begin.")


async def send_sentence(update: Update, context: ContextTypes.DEFAULT_TYPE, edit: bool = False):
    level = context.user_data["level"]
    key = context.user_data["topic"]
    sentences = context.user_data["sentences"]
    idx = context.user_data["index"]
    total = len(sentences)
    en = sentences[idx]["en"]
    text = (
        f"📘 {TOPIC_TITLE[key]} - {level}\n"
        f"Sentence {idx + 1} of {total}\n"
        f"--------------------\n"
        f"🇬🇧 {en}\n\n"
        f"✍️ Translate this into German:"
    )
    kb = practice_keyboard(level, key)
    if edit and update.callback_query:
        msg = await update.callback_query.edit_message_text(text, reply_markup=kb)
    else:
        msg = await update.effective_chat.send_message(text, reply_markup=kb)
    try:
        context.user_data["last_msg_id"] = msg.message_id
    except Exception:  # noqa: BLE001
        pass


async def start_topic(update: Update, context: ContextTypes.DEFAULT_TYPE, level: str, key: str):
    q = update.callback_query
    tg_id = update.effective_user.id

    lesson = LESSONS.get((level, key))
    if lesson:
        # Pre-authored lesson: show the grammar/vocab note first, then questions on tap.
        questions = lesson["questions"]
        idx, done = await get_progress(tg_id, key, level)
        if done or idx >= len(questions):
            await q.edit_message_text(
                f"You've already completed this lesson at level {level}! ✅\nGo again?",
                reply_markup=finished_keyboard(level, key),
            )
            return
        label = "Start ▶️" if idx == 0 else f"Continue ▶️ ({idx}/{len(questions)})"
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton(label, callback_data=f"go:{level}:{key}")],
            [InlineKeyboardButton("🔙 Topics", callback_data=f"back:topics:{level}")],
        ])
        await q.edit_message_text(
            f"📖 {TOPIC_TITLE[key]} - {level}\n\n{lesson['note']}",
            reply_markup=kb,
        )
        return

    # Fallback: AI-generated lesson (no note), cached after the first run.
    sentences = await get_content(key, level)
    if sentences is None:
        await q.edit_message_text(
            f"⏳ Preparing '{TOPIC_TITLE[key]}' for level {level}...\n"
            f"(first time only - a few seconds)"
        )
        sentences = await generate_sentences(key, level)
        if not sentences:
            await q.edit_message_text(
                "❌ Couldn't generate sentences right now. Please try again in a moment.",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("🔙 Topics", callback_data=f"back:topics:{level}")]]
                ),
            )
            return
        await save_content(key, level, sentences)

    idx, done = await get_progress(tg_id, key, level)
    if done or idx >= len(sentences):
        await q.edit_message_text(
            f"You've already completed this topic at level {level}! ✅\nGo again?",
            reply_markup=finished_keyboard(level, key),
        )
        return

    context.user_data["mode"] = "practice"
    context.user_data["level"] = level
    context.user_data["topic"] = key
    context.user_data["sentences"] = sentences
    context.user_data["index"] = idx
    await send_sentence(update, context, edit=True)


async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_id = update.effective_user.id
    level = context.user_data.get("level")
    key = context.user_data.get("topic")
    sentences = context.user_data.get("sentences")
    idx = context.user_data.get("index", 0)

    if not sentences or level is None or key is None:
        context.user_data["mode"] = None
        await update.message.reply_text("Something went wrong. Send /start to begin again.")
        return

    user_answer = (update.message.text or "").strip()
    cur = sentences[idx]

    # remove buttons from the answered sentence so only the newest one is active
    last_id = context.user_data.get("last_msg_id")
    if last_id:
        try:
            await context.bot.edit_message_reply_markup(
                chat_id=update.effective_chat.id, message_id=last_id, reply_markup=None
            )
        except Exception:  # noqa: BLE001
            pass

    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    feedback = await get_feedback(cur["en"], cur["de"], user_answer, level)
    await update.message.reply_text(feedback)

    idx += 1
    total = len(sentences)
    completed = idx >= total
    context.user_data["index"] = idx
    await save_progress(tg_id, key, level, idx, completed)

    if completed:
        context.user_data["mode"] = None
        await update.message.reply_text(
            f"🎉 Well done! You completed '{TOPIC_TITLE[key]}' at level {level} ({total} sentences).",
            reply_markup=finished_keyboard(level, key),
        )
    else:
        await send_sentence(update, context, edit=False)


async def start_placement(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    if update.callback_query:
        try:
            await update.callback_query.edit_message_text("⏳ Preparing your placement test...")
        except Exception:  # noqa: BLE001
            pass
    else:
        await chat.send_message("⏳ Preparing your placement test...")

    sentences = await get_placement_set()
    if not sentences:
        await chat.send_message("❌ Couldn't prepare the test now. Try /test again in a moment.")
        return

    context.user_data["mode"] = "placement"
    context.user_data["pl_sentences"] = sentences
    context.user_data["pl_index"] = 0
    context.user_data["pl_scores"] = []
    await chat.send_message(
        f"📊 Placement test - {len(sentences)} sentences, easy to hard.\n"
        "Translate each one into German. Let's go!"
    )
    await send_placement_question(update, context)


async def send_placement_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    s = context.user_data["pl_sentences"]
    i = context.user_data["pl_index"]
    en = s[i]["en"]
    await update.effective_chat.send_message(
        f"Q{i + 1}/{len(s)}\n🇬🇧 {en}\n\n✍️ In German:"
    )


def _recommend_level(scores):
    by: Dict[str, list] = {}
    for lvl, sc in scores:
        by.setdefault(lvl, []).append(sc)
    passed = {}
    for lvl in LEVELS:
        vals = by.get(lvl, [])
        passed[lvl] = (sum(vals) / len(vals) >= 7) if vals else False
    for lvl in LEVELS:
        if not passed[lvl]:
            return lvl, passed, by
    return LEVELS[-1], passed, by


async def handle_placement_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    s = context.user_data.get("pl_sentences")
    i = context.user_data.get("pl_index", 0)
    if not s:
        context.user_data["mode"] = None
        await update.message.reply_text("Test reset. Send /test to start again.")
        return
    cur = s[i]
    ans = (update.message.text or "").strip()
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    score = await grade_score(cur["en"], cur["de"], ans)
    context.user_data["pl_scores"].append((cur["level"], score))
    mark = "✅" if score >= 7 else ("⚠️" if score >= 4 else "❌")
    await update.message.reply_text(f"{mark} {score}/10\nCorrect: {cur['de']}")
    i += 1
    context.user_data["pl_index"] = i
    if i >= len(s):
        await finish_placement(update, context)
    else:
        await send_placement_question(update, context)


async def finish_placement(update: Update, context: ContextTypes.DEFAULT_TYPE):
    scores = context.user_data.get("pl_scores", [])
    context.user_data["mode"] = None
    rec, passed, by = _recommend_level(scores)
    lines = ["📊 Your placement result:"]
    for lvl in LEVELS:
        vals = by.get(lvl, [])
        if vals:
            avg = round(sum(vals) / len(vals), 1)
            lines.append(f"{lvl}: {avg}/10 " + ("✅" if passed[lvl] else ""))
    lines.append("")
    lines.append(f"👉 Recommended start: {rec}")
    await update.effective_chat.send_message("\n".join(lines))
    tg_id = update.effective_user.id
    prog = await progress_map(tg_id, rec)
    await update.effective_chat.send_message(
        f"Level {rec} - pick a topic:",
        reply_markup=topics_keyboard(rec, prog),
    )


async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    data = q.data
    tg_id = update.effective_user.id
    await touch_user(tg_id)

    if data == "pl:start":
        await start_placement(update, context)
        return
    if data == "pl:skip":
        context.user_data["mode"] = None
        await show_levels(update, context, greeting="No problem 🇩🇪")
        return

    if data == "back:levels":
        context.user_data["mode"] = None
        await show_levels(update, context, greeting="Choose your level:")
        return

    if data.startswith("lvl:"):
        level = data.split(":", 1)[1]
        prog = await progress_map(tg_id, level)
        await q.edit_message_text(
            f"Level {level} - pick a topic:\n(✅ = completed, a number = where you stopped)",
            reply_markup=topics_keyboard(level, prog),
        )
        return

    if data.startswith("back:topics:"):
        level = data.split(":", 2)[2]
        context.user_data["mode"] = None
        prog = await progress_map(tg_id, level)
        await q.edit_message_text(
            f"Level {level} - pick a topic:",
            reply_markup=topics_keyboard(level, prog),
        )
        return

    if data.startswith("top:"):
        _, level, key = data.split(":", 2)
        await start_topic(update, context, level, key)
        return

    if data.startswith("go:"):
        _, level, key = data.split(":", 2)
        lesson = LESSONS.get((level, key))
        if not lesson:
            return
        questions = lesson["questions"]
        idx, done = await get_progress(tg_id, key, level)
        if done or idx >= len(questions):
            idx = 0
        context.user_data["mode"] = "practice"
        context.user_data["level"] = level
        context.user_data["topic"] = key
        context.user_data["sentences"] = questions
        context.user_data["index"] = idx
        await send_sentence(update, context, edit=True)
        return

    if data.startswith("restart:"):
        _, level, key = data.split(":", 2)
        await save_progress(tg_id, key, level, 0, False)
        await start_topic(update, context, level, key)
        return

    if data.startswith("skip:"):
        _, level, key = data.split(":", 2)
        if context.user_data.get("mode") != "practice":
            return
        idx = context.user_data.get("index", 0) + 1
        sentences = context.user_data.get("sentences", [])
        total = len(sentences)
        completed = idx >= total
        context.user_data["index"] = idx
        await save_progress(tg_id, key, level, idx, completed)
        if completed:
            context.user_data["mode"] = None
            await q.edit_message_text(
                f"Topic '{TOPIC_TITLE[key]}' at level {level} is done ✅",
                reply_markup=finished_keyboard(level, key),
            )
        else:
            await send_sentence(update, context, edit=True)
        return


# ----------------------------- Admin report -----------------------------
def _humanize_seconds(s) -> str:
    s = int(s or 0)
    if s < 60:
        return f"{s}s"
    m, _ = divmod(s, 60)
    if m < 60:
        return f"{m}m"
    h, m = divmod(m, 60)
    return f"{h}h {m}m"


def _humanize_ago(dt) -> str:
    if not dt:
        return "never"
    sec = int((datetime.now(timezone.utc) - dt).total_seconds())
    if sec < 60:
        return "just now"
    if sec < 3600:
        return f"{sec // 60}m ago"
    if sec < 86400:
        return f"{sec // 3600}h ago"
    return f"{sec // 86400}d ago"


async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not ADMIN_ID or update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("This command is for the admin only.")
        return

    async with pool.acquire() as con:
        users = await con.fetch(
            "SELECT telegram_id, name, username, last_seen, active_seconds, created_at "
            "FROM users ORDER BY last_seen DESC NULLS LAST"
        )
        prog = await con.fetch(
            "SELECT telegram_id, topic_key, level, current_index, completed FROM user_progress"
        )

    if not users:
        await update.message.reply_text("No users yet.")
        return

    by_user: Dict[int, list] = {}
    for r in prog:
        by_user.setdefault(r["telegram_id"], []).append(r)

    blocks = [f"📊 Report - {len(users)} user(s)"]
    for u in users:
        rows = by_user.get(u["telegram_id"], [])
        sentences = sum(r["current_index"] for r in rows)
        if rows:
            rows_sorted = sorted(
                rows, key=lambda r: (r["level"], TOPIC_TITLE.get(r["topic_key"], r["topic_key"]))
            )
            visited = ", ".join(
                f"{r['level']}-{TOPIC_TITLE.get(r['topic_key'], r['topic_key'])} "
                + ("DONE" if r["completed"] else f"({r['current_index']}/{SENTENCES_PER_TOPIC})")
                for r in rows_sorted
            )
        else:
            visited = "-"
        uname = f"@{u['username']}" if u["username"] else "(no @)"
        joined = u["created_at"].strftime("%Y-%m-%d") if u["created_at"] else "?"
        blocks.append(
            f"\n👤 {u['name']}  {uname}\n"
            f"   ID: {u['telegram_id']}\n"
            f"   Joined: {joined} · Last: {_humanize_ago(u['last_seen'])}\n"
            f"   Active: {_humanize_seconds(u['active_seconds'])} · Sentences: {sentences}\n"
            f"   Visited: {visited}"
        )

    msg = ""
    for b in blocks:
        if len(msg) + len(b) + 1 > 3500:
            if msg.strip():
                await update.message.reply_text(msg)
            msg = ""
        msg += b + "\n"
    if msg.strip():
        await update.message.reply_text(msg)


# ----------------------------- Main -----------------------------
async def main():
    missing = [n for n, v in [("BOT_TOKEN", BOT_TOKEN), ("DATABASE_URL", DATABASE_URL),
                              ("GEMINI_API_KEY", GEMINI_API_KEY)] if not v]
    if missing:
        raise SystemExit("Missing environment variables: " + ", ".join(missing))

    await init_db()

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("report", report))
    app.add_handler(CommandHandler("test", start_placement))
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))

    # tiny health server so Railway's web service stays happy
    health = web.Application()

    async def ok(_request):
        return web.Response(text="deutschbot ok")

    health.router.add_get("/", ok)
    runner = web.AppRunner(health)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    log.info("health server on :%s", PORT)

    await app.initialize()
    await app.start()
    await app.updater.start_polling(drop_pending_updates=True)
    log.info("bot polling...")
    try:
        await asyncio.Event().wait()
    finally:
        await app.updater.stop()
        await app.stop()
        await app.shutdown()
        await runner.cleanup()
        if pool:
            await pool.close()


if __name__ == "__main__":
    asyncio.run(main())
