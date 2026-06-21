# -*- coding: utf-8 -*-
"""
Pre-authored lessons for the German bot.

Key:   (level, topic_key)   e.g. ("A1", "greeting")
Value: {"note": <grammar/vocab lesson in English>, "questions": [{"en":..., "de":...}, ...]}

Lessons that are NOT listed here automatically fall back to AI generation in the bot,
so the bot keeps working while these are filled in lesson by lesson.
"""

LESSONS = {
    ("A1", "greeting"): {
        "note": (
            "📖 Greeting — A1\n\n"
            "German greetings change with the time of day and how formal you are.\n\n"
            "GREETINGS\n"
            "• Hallo — Hello (anytime)\n"
            "• Guten Morgen — Good morning\n"
            "• Guten Tag — Good day / Hello (daytime)\n"
            "• Guten Abend — Good evening\n"
            "• Gute Nacht — Good night (before bed)\n"
            "• Tschüss — Bye (informal)\n"
            "• Auf Wiedersehen — Goodbye (formal)\n"
            "• Bis bald / Bis später — See you soon / later\n\n"
            "FORMAL vs INFORMAL — \"du\" and \"Sie\"\n"
            "German has two words for \"you\":\n"
            "• du — informal (friends, family)\n"
            "• Sie — formal (strangers, officials); always capitalized.\n"
            "\"How are you?\" → Wie geht es dir? (informal) · Wie geht es Ihnen? (formal) · Wie geht's? (casual)\n\n"
            "INTRODUCING YOURSELF\n"
            "• Ich heiße Anna. — My name is Anna. (heißen = to be called)\n"
            "• Ich bin Anna. — I am Anna.\n"
            "• Mein Name ist Anna. — My name is Anna.\n"
            "• Wie heißt du? / Wie heißen Sie? — What's your name?\n"
            "• Freut mich. — Nice to meet you.\n\n"
            "SHORT ANSWERS\n"
            "• Mir geht es gut. — I'm fine.   • Es geht. — So-so.   • Und dir? — And you?\n\n"
            "GRAMMAR FOCUS — sein & heißen (present tense)\n"
            "sein (to be): ich bin · du bist · er/sie ist · wir sind · ihr seid · sie/Sie sind\n"
            "heißen (to be called): ich heiße · du heißt · er/sie heißt · sie/Sie heißen\n"
            "Word order: the verb is in second position — \"Ich heiße Anna.\"\n"
            "In a question with a question word: question word + verb + subject — \"Wie heißt du?\"\n\n"
            "Tap Start and translate 40 short sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "Hello!", "de": "Hallo!"},
            {"en": "Good morning!", "de": "Guten Morgen!"},
            {"en": "Good day!", "de": "Guten Tag!"},
            {"en": "Good evening!", "de": "Guten Abend!"},
            {"en": "Good night!", "de": "Gute Nacht!"},
            {"en": "Bye!", "de": "Tschüss!"},
            {"en": "Goodbye!", "de": "Auf Wiedersehen!"},
            {"en": "See you soon!", "de": "Bis bald!"},
            {"en": "See you later!", "de": "Bis später!"},
            {"en": "Thank you!", "de": "Danke!"},
            {"en": "Yes, please.", "de": "Ja, bitte."},
            {"en": "No, thank you.", "de": "Nein, danke."},
            {"en": "How are you?", "de": "Wie geht es dir?"},
            {"en": "How are you? (formal)", "de": "Wie geht es Ihnen?"},
            {"en": "I am fine.", "de": "Mir geht es gut."},
            {"en": "Very well, thanks.", "de": "Sehr gut, danke."},
            {"en": "So-so.", "de": "Es geht."},
            {"en": "And you?", "de": "Und dir?"},
            {"en": "What is your name?", "de": "Wie heißt du?"},
            {"en": "What is your name? (formal)", "de": "Wie heißen Sie?"},
            {"en": "My name is Anna.", "de": "Ich heiße Anna."},
            {"en": "I am Thomas.", "de": "Ich bin Thomas."},
            {"en": "My name is Peter.", "de": "Mein Name ist Peter."},
            {"en": "Nice to meet you.", "de": "Freut mich."},
            {"en": "Welcome!", "de": "Willkommen!"},
            {"en": "Where are you from?", "de": "Woher kommst du?"},
            {"en": "I am from Berlin.", "de": "Ich komme aus Berlin."},
            {"en": "I am from Iran.", "de": "Ich komme aus dem Iran."},
            {"en": "Do you speak German?", "de": "Sprichst du Deutsch?"},
            {"en": "I speak a little German.", "de": "Ich spreche ein bisschen Deutsch."},
            {"en": "I don't understand.", "de": "Ich verstehe nicht."},
            {"en": "Please repeat that.", "de": "Wiederhole das bitte."},
            {"en": "How are you today?", "de": "Wie geht es dir heute?"},
            {"en": "I am very happy.", "de": "Ich bin sehr glücklich."},
            {"en": "Have a nice day!", "de": "Schönen Tag noch!"},
            {"en": "This is my friend Lena.", "de": "Das ist meine Freundin Lena."},
            {"en": "How old are you?", "de": "Wie alt bist du?"},
            {"en": "I am twenty years old.", "de": "Ich bin zwanzig Jahre alt."},
            {"en": "Where do you live?", "de": "Wo wohnst du?"},
            {"en": "It was nice to meet you.", "de": "Es war schön, dich kennenzulernen."},
        ],
    },
}
