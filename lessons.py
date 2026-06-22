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

    ("A1", "holiday"): {
        "note": (
            "📖 Holiday — A1\n\n"
            "The present tense (Präsens) is used for now, habits and the near future. "
            "Most verbs are regular: take the stem and add the endings.\n\n"
            "REGULAR PRESENT ENDINGS (machen = to do/make)\n"
            "ich mache · du machst · er/sie/es macht · wir machen · ihr macht · sie/Sie machen\n\n"
            "USEFUL TRAVEL VERBS\n"
            "reisen (travel) · fliegen (fly) · fahren (go/drive) · besuchen (visit) · "
            "buchen (book) · packen (pack) · bleiben (stay) · schwimmen (swim)\n\n"
            "A few verbs change their stem vowel in du/er forms:\n"
            "fahren → du fährst, er fährt   ·   sehen → du siehst, er sieht\n\n"
            "WORD ORDER — verb in position 2\n"
            "Ich fahre im Sommer nach Italien.  ·  Im Sommer fahre ich nach Italien. (verb still 2nd)\n"
            "Question word + verb + subject: Wohin fährst du?\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I travel a lot.", "de": "Ich reise viel."},
            {"en": "We fly to Spain.", "de": "Wir fliegen nach Spanien."},
            {"en": "She books a hotel.", "de": "Sie bucht ein Hotel."},
            {"en": "I pack my suitcase.", "de": "Ich packe meinen Koffer."},
            {"en": "They visit Berlin.", "de": "Sie besuchen Berlin."},
            {"en": "He swims in the sea.", "de": "Er schwimmt im Meer."},
            {"en": "We stay for one week.", "de": "Wir bleiben eine Woche."},
            {"en": "I take many photos.", "de": "Ich mache viele Fotos."},
            {"en": "Where are you going?", "de": "Wohin fährst du?"},
            {"en": "I am going to Italy.", "de": "Ich fahre nach Italien."},
            {"en": "The holiday begins tomorrow.", "de": "Der Urlaub beginnt morgen."},
            {"en": "We travel by train.", "de": "Wir fahren mit dem Zug."},
            {"en": "She flies to Paris.", "de": "Sie fliegt nach Paris."},
            {"en": "Do you visit your family?", "de": "Besuchst du deine Familie?"},
            {"en": "I book a flight.", "de": "Ich buche einen Flug."},
            {"en": "The children swim every day.", "de": "Die Kinder schwimmen jeden Tag."},
            {"en": "We stay overnight at the hotel.", "de": "Wir übernachten im Hotel."},
            {"en": "In summer we travel to Greece.", "de": "Im Sommer reisen wir nach Griechenland."},
            {"en": "He visits a museum.", "de": "Er besucht ein Museum."},
            {"en": "I buy souvenirs.", "de": "Ich kaufe Souvenirs."},
            {"en": "When does the train leave?", "de": "Wann fährt der Zug?"},
            {"en": "We go to the beach.", "de": "Wir gehen an den Strand."},
            {"en": "She sends a postcard.", "de": "Sie schickt eine Postkarte."},
            {"en": "I drink coffee at the airport.", "de": "Ich trinke Kaffee am Flughafen."},
            {"en": "Do you fly often?", "de": "Fliegst du oft?"},
            {"en": "They book a tour.", "de": "Sie buchen eine Tour."},
            {"en": "We visit our grandparents.", "de": "Wir besuchen unsere Großeltern."},
            {"en": "The plane lands at six.", "de": "Das Flugzeug landet um sechs."},
            {"en": "I am looking for my passport.", "de": "Ich suche meinen Pass."},
            {"en": "He drives to the mountains.", "de": "Er fährt in die Berge."},
            {"en": "We spend two weeks in Spain.", "de": "Wir verbringen zwei Wochen in Spanien."},
            {"en": "She takes a lot of photos.", "de": "Sie macht viele Fotos."},
            {"en": "I always travel in summer.", "de": "Ich reise immer im Sommer."},
            {"en": "Do you stay at home?", "de": "Bleibst du zu Hause?"},
            {"en": "The hotel is very nice.", "de": "Das Hotel ist sehr schön."},
            {"en": "We fly home on Sunday.", "de": "Wir fliegen am Sonntag nach Hause."},
            {"en": "He visits a new country every year.", "de": "Er besucht jedes Jahr ein neues Land."},
            {"en": "I love the sea.", "de": "Ich liebe das Meer."},
            {"en": "Where do you spend your holidays?", "de": "Wo verbringst du deinen Urlaub?"},
            {"en": "In winter we go skiing in Austria.", "de": "Im Winter fahren wir in Österreich Ski."},
        ],
    },

    ("A1", "relationship"): {
        "note": (
            "📖 Relationship — A1\n\n"
            "PERSONAL PRONOUNS (subject form — nominative)\n"
            "ich (I) · du (you, informal) · er (he) · sie (she) · es (it)\n"
            "wir (we) · ihr (you, plural) · sie (they) · Sie (you, formal)\n\n"
            "THE VERB haben (to have) — irregular and very common\n"
            "ich habe · du hast · er/sie/es hat · wir haben · ihr habt · sie/Sie haben\n\n"
            "We use haben for family and possessions, and it takes the Akkusativ "
            "(einen/eine/ein):\n"
            "Ich habe einen Bruder.  ·  Sie hat eine große Familie.\n\n"
            "FAMILY VOCAB\n"
            "die Mutter, der Vater, die Eltern, die Schwester, der Bruder, die Tochter, der Sohn, "
            "die Großmutter (Oma), der Großvater (Opa), der Mann, die Frau, das Kind, "
            "der Freund / die Freundin.\n\n"
            "Remember: the verb stays in position 2.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I have a sister.", "de": "Ich habe eine Schwester."},
            {"en": "He has two brothers.", "de": "Er hat zwei Brüder."},
            {"en": "We have a big family.", "de": "Wir haben eine große Familie."},
            {"en": "She has a daughter and a son.", "de": "Sie hat eine Tochter und einen Sohn."},
            {"en": "Do you have children?", "de": "Hast du Kinder?"},
            {"en": "They have a dog.", "de": "Sie haben einen Hund."},
            {"en": "My mother is very nice.", "de": "Meine Mutter ist sehr nett."},
            {"en": "My father is a teacher.", "de": "Mein Vater ist Lehrer."},
            {"en": "I have a brother.", "de": "Ich habe einen Bruder."},
            {"en": "My sister is twelve years old.", "de": "Meine Schwester ist zwölf Jahre alt."},
            {"en": "We have grandparents in Italy.", "de": "Wir haben Großeltern in Italien."},
            {"en": "He has a wife and two children.", "de": "Er hat eine Frau und zwei Kinder."},
            {"en": "Do you have a sister?", "de": "Hast du eine Schwester?"},
            {"en": "She is my friend.", "de": "Sie ist meine Freundin."},
            {"en": "My parents live in Berlin.", "de": "Meine Eltern wohnen in Berlin."},
            {"en": "I love my family.", "de": "Ich liebe meine Familie."},
            {"en": "He has many friends.", "de": "Er hat viele Freunde."},
            {"en": "My grandmother is eighty.", "de": "Meine Großmutter ist achtzig."},
            {"en": "We have a small house.", "de": "Wir haben ein kleines Haus."},
            {"en": "Do you have a brother or a sister?", "de": "Hast du einen Bruder oder eine Schwester?"},
            {"en": "My uncle lives in Austria.", "de": "Mein Onkel wohnt in Österreich."},
            {"en": "She has a cat.", "de": "Sie hat eine Katze."},
            {"en": "My name is Sara and I have one child.", "de": "Ich heiße Sara und ich habe ein Kind."},
            {"en": "They are my cousins.", "de": "Sie sind meine Cousins."},
            {"en": "My brother is married.", "de": "Mein Bruder ist verheiratet."},
            {"en": "I have no children.", "de": "Ich habe keine Kinder."},
            {"en": "Her husband is from Spain.", "de": "Ihr Mann kommt aus Spanien."},
            {"en": "We have a big garden.", "de": "Wir haben einen großen Garten."},
            {"en": "My aunt is very funny.", "de": "Meine Tante ist sehr lustig."},
            {"en": "Do you have a pet?", "de": "Hast du ein Haustier?"},
            {"en": "My son goes to school.", "de": "Mein Sohn geht zur Schule."},
            {"en": "I have two sisters and one brother.", "de": "Ich habe zwei Schwestern und einen Bruder."},
            {"en": "His sister is a doctor.", "de": "Seine Schwester ist Ärztin."},
            {"en": "We often visit our grandparents.", "de": "Wir besuchen oft unsere Großeltern."},
            {"en": "My daughter likes animals.", "de": "Meine Tochter mag Tiere."},
            {"en": "Are you married?", "de": "Bist du verheiratet?"},
            {"en": "My family is very important.", "de": "Meine Familie ist sehr wichtig."},
            {"en": "He has a little brother.", "de": "Er hat einen kleinen Bruder."},
            {"en": "My grandparents have a farm.", "de": "Meine Großeltern haben einen Bauernhof."},
            {"en": "I live with my family.", "de": "Ich wohne bei meiner Familie."},
        ],
    },

    ("A1", "technology"): {
        "note": (
            "📖 Technology — A1\n\n"
            "Every German noun has a gender: masculine (der), feminine (die) or neuter (das). "
            "Always learn the article with the noun.\n\n"
            "DEFINITE ARTICLE (the) — nominative\n"
            "der (m): der Computer, der Drucker · die (f): die Maus, die Kamera · "
            "das (n): das Handy, das Internet\n"
            "Plural is always die: die Computer, die Handys.\n\n"
            "INDEFINITE ARTICLE (a/an)\n"
            "ein (m/n): ein Computer, ein Handy · eine (f): eine Maus, eine Kamera\n"
            "Negative: kein/keine — Das ist kein Drucker.\n\n"
            "NOMINATIVE = the subject (who/what does the action):\n"
            "Der Computer ist neu.  ·  Das ist ein Handy.\n\n"
            "TECH VOCAB\n"
            "der Computer, der Bildschirm, der Drucker, der Akku, das Handy, das Laptop, das Tablet, "
            "das Internet, das Passwort, die Tastatur, die Maus, die App, die E-Mail, die Kamera.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "The computer is new.", "de": "Der Computer ist neu."},
            {"en": "That is a mobile phone.", "de": "Das ist ein Handy."},
            {"en": "The screen is big.", "de": "Der Bildschirm ist groß."},
            {"en": "I have a tablet.", "de": "Ich habe ein Tablet."},
            {"en": "The mouse is small.", "de": "Die Maus ist klein."},
            {"en": "Is that a printer?", "de": "Ist das ein Drucker?"},
            {"en": "No, that is not a printer.", "de": "Nein, das ist kein Drucker."},
            {"en": "The phone is expensive.", "de": "Das Handy ist teuer."},
            {"en": "My computer is slow.", "de": "Mein Computer ist langsam."},
            {"en": "The internet is fast.", "de": "Das Internet ist schnell."},
            {"en": "I need a password.", "de": "Ich brauche ein Passwort."},
            {"en": "The camera takes good photos.", "de": "Die Kamera macht gute Fotos."},
            {"en": "Where is the keyboard?", "de": "Wo ist die Tastatur?"},
            {"en": "The app is free.", "de": "Die App ist kostenlos."},
            {"en": "I write an email.", "de": "Ich schreibe eine E-Mail."},
            {"en": "The battery is empty.", "de": "Der Akku ist leer."},
            {"en": "This is my new phone.", "de": "Das ist mein neues Handy."},
            {"en": "The laptop does not work.", "de": "Das Laptop funktioniert nicht."},
            {"en": "Do you have a charger?", "de": "Hast du ein Ladegerät?"},
            {"en": "The screen is broken.", "de": "Der Bildschirm ist kaputt."},
            {"en": "I install an app.", "de": "Ich installiere eine App."},
            {"en": "The printer is old.", "de": "Der Drucker ist alt."},
            {"en": "My password is secret.", "de": "Mein Passwort ist geheim."},
            {"en": "The mobile phone is on the table.", "de": "Das Handy ist auf dem Tisch."},
            {"en": "I have no internet.", "de": "Ich habe kein Internet."},
            {"en": "The computer is in the office.", "de": "Der Computer ist im Büro."},
            {"en": "Is the wifi free?", "de": "Ist das WLAN kostenlos?"},
            {"en": "The camera is very good.", "de": "Die Kamera ist sehr gut."},
            {"en": "I need a new charger.", "de": "Ich brauche ein neues Ladegerät."},
            {"en": "The smartphone is modern.", "de": "Das Smartphone ist modern."},
            {"en": "Where is my phone?", "de": "Wo ist mein Handy?"},
            {"en": "The keyboard is dirty.", "de": "Die Tastatur ist schmutzig."},
            {"en": "The app is very useful.", "de": "Die App ist sehr nützlich."},
            {"en": "The screen is too small.", "de": "Der Bildschirm ist zu klein."},
            {"en": "I buy a new computer.", "de": "Ich kaufe einen neuen Computer."},
            {"en": "The email is important.", "de": "Die E-Mail ist wichtig."},
            {"en": "My laptop is fast.", "de": "Mein Laptop ist schnell."},
            {"en": "That is not my phone.", "de": "Das ist nicht mein Handy."},
            {"en": "The photos are beautiful.", "de": "Die Fotos sind schön."},
            {"en": "Technology is very important today.", "de": "Technik ist heute sehr wichtig."},
        ],
    },

    ("A1", "sports"): {
        "note": (
            "📖 Sports — A1\n\n"
            "THE ACCUSATIVE CASE (Akkusativ) — the direct object (what receives the action).\n"
            "Only the MASCULINE article changes; die / das / plural stay the same.\n"
            "  der → den    ·    ein → einen\n"
            "  die → die     ·    eine → eine\n"
            "  das → das     ·    ein → ein\n\n"
            "• Wir gewinnen das Spiel.  ·  Ich kaufe einen Ball.\n"
            "• Most sports/games take NO article: Ich spiele Fußball. · Ich mache Sport.\n\n"
            "USEFUL VERBS\n"
            "spielen (play) · machen (do) · trainieren (train) · laufen (run) · "
            "gewinnen (win) · verlieren (lose) · schwimmen (swim)\n\n"
            "VOCAB: der Fußball, der Ball, der Sport, das Spiel, die Mannschaft (team), "
            "das Schwimmbad, das Stadion, das Tor (goal), der Trainer, der Spieler.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I play football.", "de": "Ich spiele Fußball."},
            {"en": "We play tennis.", "de": "Wir spielen Tennis."},
            {"en": "He plays basketball.", "de": "Er spielt Basketball."},
            {"en": "I do sport every day.", "de": "Ich mache jeden Tag Sport."},
            {"en": "She swims very fast.", "de": "Sie schwimmt sehr schnell."},
            {"en": "They train on Mondays.", "de": "Sie trainieren montags."},
            {"en": "I buy a ball.", "de": "Ich kaufe einen Ball."},
            {"en": "We win the game.", "de": "Wir gewinnen das Spiel."},
            {"en": "The team is very good.", "de": "Die Mannschaft ist sehr gut."},
            {"en": "I run in the park.", "de": "Ich laufe im Park."},
            {"en": "Do you play tennis?", "de": "Spielst du Tennis?"},
            {"en": "He has a new trainer.", "de": "Er hat einen neuen Trainer."},
            {"en": "We lose the game.", "de": "Wir verlieren das Spiel."},
            {"en": "I need new shoes.", "de": "Ich brauche neue Schuhe."},
            {"en": "She plays volleyball.", "de": "Sie spielt Volleyball."},
            {"en": "The match starts at three.", "de": "Das Spiel beginnt um drei."},
            {"en": "I watch the game.", "de": "Ich sehe das Spiel."},
            {"en": "We go to the stadium.", "de": "Wir gehen ins Stadion."},
            {"en": "He scores a goal.", "de": "Er schießt ein Tor."},
            {"en": "My brother plays handball.", "de": "Mein Bruder spielt Handball."},
            {"en": "I like sport.", "de": "Ich mag Sport."},
            {"en": "The pool is closed today.", "de": "Das Schwimmbad ist heute geschlossen."},
            {"en": "We train hard.", "de": "Wir trainieren hart."},
            {"en": "She wins the race.", "de": "Sie gewinnt das Rennen."},
            {"en": "Do you do yoga?", "de": "Machst du Yoga?"},
            {"en": "I play football with my friends.", "de": "Ich spiele Fußball mit meinen Freunden."},
            {"en": "The team has a good trainer.", "de": "Die Mannschaft hat einen guten Trainer."},
            {"en": "He runs ten kilometers.", "de": "Er läuft zehn Kilometer."},
            {"en": "We play a game.", "de": "Wir spielen ein Spiel."},
            {"en": "I take my ball.", "de": "Ich nehme meinen Ball."},
            {"en": "They have a big stadium.", "de": "Sie haben ein großes Stadion."},
            {"en": "She trains every evening.", "de": "Sie trainiert jeden Abend."},
            {"en": "I love football.", "de": "Ich liebe Fußball."},
            {"en": "Our team wins often.", "de": "Unsere Mannschaft gewinnt oft."},
            {"en": "He is a good player.", "de": "Er ist ein guter Spieler."},
            {"en": "I play tennis on Sundays.", "de": "Ich spiele sonntags Tennis."},
            {"en": "We need a new ball.", "de": "Wir brauchen einen neuen Ball."},
            {"en": "The game is very exciting.", "de": "Das Spiel ist sehr spannend."},
            {"en": "Do you watch football?", "de": "Schaust du Fußball?"},
            {"en": "Sport keeps me healthy.", "de": "Sport hält mich gesund."},
        ],
    },

    ("A1", "food"): {
        "note": (
            "📖 Food — A1\n\n"
            "Talking about food uses the Akkusativ (the thing you eat / buy / want). "
            "Only masculine changes: der→den, ein→einen.\n\n"
            "KEY VERBS\n"
            "essen: ich esse, du isst, er isst · trinken: ich trinke, du trinkst\n"
            "nehmen: ich nehme, du nimmst, er nimmt · "
            "möchten (would like): ich möchte, du möchtest · mögen (like): ich mag, du magst\n\n"
            "• Ich esse einen Apfel.  ·  Ich trinke einen Kaffee.\n"
            "• Ich möchte ein Wasser, bitte.  ·  Ich mag Schokolade.\n"
            "With möchten, the main verb goes to the end: Ich möchte einen Tee trinken.\n\n"
            "VOCAB: das Brot, der Apfel, der Käse, das Ei, der Reis, die Suppe, das Fleisch, "
            "der Fisch, das Wasser, der Kaffee, der Tee, der Saft, die Milch, das Gemüse, das Obst.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I eat an apple.", "de": "Ich esse einen Apfel."},
            {"en": "I drink water.", "de": "Ich trinke Wasser."},
            {"en": "She eats bread.", "de": "Sie isst Brot."},
            {"en": "We drink coffee.", "de": "Wir trinken Kaffee."},
            {"en": "I would like a tea.", "de": "Ich möchte einen Tee."},
            {"en": "He eats fish.", "de": "Er isst Fisch."},
            {"en": "I like cheese.", "de": "Ich mag Käse."},
            {"en": "Do you eat meat?", "de": "Isst du Fleisch?"},
            {"en": "I would like a water, please.", "de": "Ich möchte ein Wasser, bitte."},
            {"en": "We eat rice.", "de": "Wir essen Reis."},
            {"en": "She drinks milk.", "de": "Sie trinkt Milch."},
            {"en": "I take a coffee.", "de": "Ich nehme einen Kaffee."},
            {"en": "The soup is hot.", "de": "Die Suppe ist heiß."},
            {"en": "Do you like chocolate?", "de": "Magst du Schokolade?"},
            {"en": "I eat vegetables every day.", "de": "Ich esse jeden Tag Gemüse."},
            {"en": "He drinks a juice.", "de": "Er trinkt einen Saft."},
            {"en": "I would like an apple.", "de": "Ich möchte einen Apfel."},
            {"en": "We buy bread and cheese.", "de": "Wir kaufen Brot und Käse."},
            {"en": "She doesn't eat meat.", "de": "Sie isst kein Fleisch."},
            {"en": "I am hungry.", "de": "Ich habe Hunger."},
            {"en": "I am thirsty.", "de": "Ich habe Durst."},
            {"en": "The bread is fresh.", "de": "Das Brot ist frisch."},
            {"en": "Do you want a tea or a coffee?", "de": "Möchtest du einen Tee oder einen Kaffee?"},
            {"en": "I eat an egg in the morning.", "de": "Ich esse morgens ein Ei."},
            {"en": "We like fruit.", "de": "Wir mögen Obst."},
            {"en": "He takes the fish.", "de": "Er nimmt den Fisch."},
            {"en": "The coffee is too hot.", "de": "Der Kaffee ist zu heiß."},
            {"en": "I would like to drink a water.", "de": "Ich möchte ein Wasser trinken."},
            {"en": "She eats a lot of vegetables.", "de": "Sie isst viel Gemüse."},
            {"en": "We cook a soup.", "de": "Wir kochen eine Suppe."},
            {"en": "Do you like fish?", "de": "Magst du Fisch?"},
            {"en": "I drink tea without sugar.", "de": "Ich trinke Tee ohne Zucker."},
            {"en": "The meal is delicious.", "de": "Das Essen ist lecker."},
            {"en": "I buy fruit at the market.", "de": "Ich kaufe Obst auf dem Markt."},
            {"en": "He eats too much chocolate.", "de": "Er isst zu viel Schokolade."},
            {"en": "We would like the menu, please.", "de": "Wir möchten die Speisekarte, bitte."},
            {"en": "I don't drink coffee.", "de": "Ich trinke keinen Kaffee."},
            {"en": "She likes apples and bananas.", "de": "Sie mag Äpfel und Bananen."},
            {"en": "The restaurant is very good.", "de": "Das Restaurant ist sehr gut."},
            {"en": "I would like to order a pizza.", "de": "Ich möchte eine Pizza bestellen."},
        ],
    },

    ("A1", "education"): {
        "note": (
            "📖 Education — A1\n\n"
            "MODAL VERB können (can / to be able to).\n"
            "A modal needs a second verb in the INFINITIVE, which goes to the END.\n"
            "ich kann · du kannst · er/sie kann · wir können · ihr könnt · sie/Sie können\n\n"
            "• Ich kann Deutsch sprechen.  → I can speak German.\n"
            "• Kannst du mir helfen?  → Can you help me?\n"
            "The modal is in position 2; the main verb is last.\n\n"
            "VOCAB: die Schule, die Universität, der Lehrer/die Lehrerin, der Schüler, "
            "der Student, das Fach (subject), die Prüfung (exam), die Hausaufgaben (homework), "
            "lernen, verstehen, lesen, schreiben.\n"
            "SUBJECTS: Mathe, Deutsch, Englisch, Biologie, Geschichte, Kunst, Sport, Musik.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I can speak German.", "de": "Ich kann Deutsch sprechen."},
            {"en": "Can you help me?", "de": "Kannst du mir helfen?"},
            {"en": "She can read well.", "de": "Sie kann gut lesen."},
            {"en": "We learn English at school.", "de": "Wir lernen Englisch in der Schule."},
            {"en": "He can write fast.", "de": "Er kann schnell schreiben."},
            {"en": "I study every evening.", "de": "Ich lerne jeden Abend."},
            {"en": "Can you understand me?", "de": "Kannst du mich verstehen?"},
            {"en": "The teacher is very nice.", "de": "Der Lehrer ist sehr nett."},
            {"en": "I have homework today.", "de": "Ich habe heute Hausaufgaben."},
            {"en": "We can ask a question.", "de": "Wir können eine Frage stellen."},
            {"en": "She studies at the university.", "de": "Sie studiert an der Universität."},
            {"en": "Can I open the window?", "de": "Kann ich das Fenster öffnen?"},
            {"en": "My favorite subject is math.", "de": "Mein Lieblingsfach ist Mathe."},
            {"en": "The exam is on Monday.", "de": "Die Prüfung ist am Montag."},
            {"en": "He cannot come today.", "de": "Er kann heute nicht kommen."},
            {"en": "I want to learn German.", "de": "Ich möchte Deutsch lernen."},
            {"en": "Can you repeat that, please?", "de": "Kannst du das bitte wiederholen?"},
            {"en": "We read a book in class.", "de": "Wir lesen ein Buch im Unterricht."},
            {"en": "She can speak three languages.", "de": "Sie kann drei Sprachen sprechen."},
            {"en": "The students are in the classroom.", "de": "Die Schüler sind im Klassenzimmer."},
            {"en": "I don't understand the question.", "de": "Ich verstehe die Frage nicht."},
            {"en": "Can we work together?", "de": "Können wir zusammenarbeiten?"},
            {"en": "He learns very quickly.", "de": "Er lernt sehr schnell."},
            {"en": "I write the answer.", "de": "Ich schreibe die Antwort."},
            {"en": "Can you explain that?", "de": "Kannst du das erklären?"},
            {"en": "The lesson begins at eight.", "de": "Der Unterricht beginnt um acht."},
            {"en": "I have an exam tomorrow.", "de": "Ich habe morgen eine Prüfung."},
            {"en": "She can help you.", "de": "Sie kann dir helfen."},
            {"en": "We learn a lot.", "de": "Wir lernen viel."},
            {"en": "Can I ask something?", "de": "Kann ich etwas fragen?"},
            {"en": "My teacher speaks English.", "de": "Mein Lehrer spricht Englisch."},
            {"en": "He does his homework.", "de": "Er macht seine Hausaufgaben."},
            {"en": "I cannot find my book.", "de": "Ich kann mein Buch nicht finden."},
            {"en": "Can you read this word?", "de": "Kannst du dieses Wort lesen?"},
            {"en": "The university is very big.", "de": "Die Universität ist sehr groß."},
            {"en": "We study together.", "de": "Wir lernen zusammen."},
            {"en": "She wants to become a teacher.", "de": "Sie möchte Lehrerin werden."},
            {"en": "I can answer the question.", "de": "Ich kann die Frage beantworten."},
            {"en": "The book is very interesting.", "de": "Das Buch ist sehr interessant."},
            {"en": "Education is very important.", "de": "Bildung ist sehr wichtig."},
        ],
    },

    ("A1", "work"): {
        "note": (
            "📖 Work — A1\n\n"
            "MORE MODAL VERBS (second verb → infinitive at the end).\n"
            "müssen (must / have to): ich muss · du musst · er muss · wir müssen · ihr müsst · sie müssen\n"
            "wollen (want to): ich will · du willst · er will · wir wollen · ihr wollt · sie wollen\n\n"
            "• Ich muss um acht arbeiten.  ·  Ich will Geld verdienen.\n\n"
            "TELLING THE TIME\n"
            "Wie spät ist es? — What time is it? · Es ist acht Uhr. · um neun Uhr · halb zehn (9:30).\n\n"
            "VOCAB: die Arbeit, der Job, der Beruf, das Büro, der Chef, der Kollege, die Firma, "
            "arbeiten, verdienen (earn), pünktlich (on time).\n"
            "JOBS: der Arzt/die Ärztin, der Lehrer, der Ingenieur, die Verkäuferin, der Koch.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I work in an office.", "de": "Ich arbeite in einem Büro."},
            {"en": "She is a doctor.", "de": "Sie ist Ärztin."},
            {"en": "I have to work today.", "de": "Ich muss heute arbeiten."},
            {"en": "He wants to earn money.", "de": "Er will Geld verdienen."},
            {"en": "What time is it?", "de": "Wie spät ist es?"},
            {"en": "It is eight o'clock.", "de": "Es ist acht Uhr."},
            {"en": "I start at nine.", "de": "Ich beginne um neun."},
            {"en": "My boss is very nice.", "de": "Mein Chef ist sehr nett."},
            {"en": "We have to work a lot.", "de": "Wir müssen viel arbeiten."},
            {"en": "She wants to be a teacher.", "de": "Sie will Lehrerin werden."},
            {"en": "I work from nine to five.", "de": "Ich arbeite von neun bis fünf."},
            {"en": "He works in a factory.", "de": "Er arbeitet in einer Fabrik."},
            {"en": "Do you have to work tomorrow?", "de": "Musst du morgen arbeiten?"},
            {"en": "I want to find a new job.", "de": "Ich will einen neuen Job finden."},
            {"en": "My colleague is friendly.", "de": "Mein Kollege ist freundlich."},
            {"en": "The meeting starts at ten.", "de": "Das Meeting beginnt um zehn."},
            {"en": "I must call the boss.", "de": "Ich muss den Chef anrufen."},
            {"en": "She works as a nurse.", "de": "Sie arbeitet als Krankenschwester."},
            {"en": "We want to work together.", "de": "Wir wollen zusammenarbeiten."},
            {"en": "I have to go now.", "de": "Ich muss jetzt gehen."},
            {"en": "He earns a lot of money.", "de": "Er verdient viel Geld."},
            {"en": "My job is very interesting.", "de": "Mein Job ist sehr interessant."},
            {"en": "I work every day.", "de": "Ich arbeite jeden Tag."},
            {"en": "She has to write an email.", "de": "Sie muss eine E-Mail schreiben."},
            {"en": "What is your job?", "de": "Was bist du von Beruf?"},
            {"en": "I am an engineer.", "de": "Ich bin Ingenieur."},
            {"en": "We want to start a company.", "de": "Wir wollen eine Firma gründen."},
            {"en": "The office is in the city.", "de": "Das Büro ist in der Stadt."},
            {"en": "He has to work on Saturday.", "de": "Er muss am Samstag arbeiten."},
            {"en": "I want to learn a lot.", "de": "Ich will viel lernen."},
            {"en": "My salary is good.", "de": "Mein Gehalt ist gut."},
            {"en": "She works at a bank.", "de": "Sie arbeitet bei einer Bank."},
            {"en": "I have to be on time.", "de": "Ich muss pünktlich sein."},
            {"en": "Do you want to work here?", "de": "Willst du hier arbeiten?"},
            {"en": "He is a good cook.", "de": "Er ist ein guter Koch."},
            {"en": "We are done at six.", "de": "Wir sind um sechs fertig."},
            {"en": "I want to help my colleagues.", "de": "Ich will meinen Kollegen helfen."},
            {"en": "The work is very hard.", "de": "Die Arbeit ist sehr schwer."},
            {"en": "She must learn German for her job.", "de": "Sie muss für ihren Job Deutsch lernen."},
            {"en": "I want to be successful.", "de": "Ich will erfolgreich sein."},
        ],
    },

    ("A1", "health"): {
        "note": (
            "📖 Health — A1\n\n"
            "TWO WAYS TO SAY \"NO / NOT\"\n"
            "1) kein/keine — negates a NOUN (replaces ein/eine or no article):\n"
            "   Ich habe Zeit. → Ich habe keine Zeit.   ·   Ich trinke keinen Alkohol.\n"
            "2) nicht — negates a verb, adjective or the whole sentence:\n"
            "   Ich komme nicht.   ·   Das ist nicht gut.   ·   Ich bin nicht müde.\n"
            "Rule: kein with nouns, nicht for everything else.\n\n"
            "FEELING / HEALTH\n"
            "Ich bin krank / gesund / müde.   ·   Ich habe Kopfschmerzen.\n"
            "Mir tut der Kopf weh. (My head hurts.)   ·   Ich brauche einen Arzt.\n\n"
            "VOCAB: der Kopf, der Bauch, der Hals, der Arm, das Bein, der Rücken, der Zahn, "
            "krank, gesund, müde, der Arzt, die Apotheke, die Medizin.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I am tired.", "de": "Ich bin müde."},
            {"en": "I am not tired.", "de": "Ich bin nicht müde."},
            {"en": "He is ill.", "de": "Er ist krank."},
            {"en": "She is healthy.", "de": "Sie ist gesund."},
            {"en": "I have a headache.", "de": "Ich habe Kopfschmerzen."},
            {"en": "I have no time.", "de": "Ich habe keine Zeit."},
            {"en": "I don't drink alcohol.", "de": "Ich trinke keinen Alkohol."},
            {"en": "My head hurts.", "de": "Mir tut der Kopf weh."},
            {"en": "I need a doctor.", "de": "Ich brauche einen Arzt."},
            {"en": "He is not here.", "de": "Er ist nicht hier."},
            {"en": "I am not hungry.", "de": "Ich habe keinen Hunger."},
            {"en": "My stomach hurts.", "de": "Mir tut der Bauch weh."},
            {"en": "She has a cold.", "de": "Sie hat eine Erkältung."},
            {"en": "I do not feel well.", "de": "Ich fühle mich nicht gut."},
            {"en": "The medicine is in the bag.", "de": "Die Medizin ist in der Tasche."},
            {"en": "I have no money for the doctor.", "de": "Ich habe kein Geld für den Arzt."},
            {"en": "My back hurts.", "de": "Mir tut der Rücken weh."},
            {"en": "He cannot sleep.", "de": "Er kann nicht schlafen."},
            {"en": "I am not sick.", "de": "Ich bin nicht krank."},
            {"en": "Where is the pharmacy?", "de": "Wo ist die Apotheke?"},
            {"en": "I have a sore throat.", "de": "Ich habe Halsschmerzen."},
            {"en": "She doesn't have a fever.", "de": "Sie hat kein Fieber."},
            {"en": "I drink a lot of water.", "de": "Ich trinke viel Wasser."},
            {"en": "My tooth hurts.", "de": "Mir tut der Zahn weh."},
            {"en": "He is very healthy.", "de": "Er ist sehr gesund."},
            {"en": "I am not afraid.", "de": "Ich habe keine Angst."},
            {"en": "The doctor is not here today.", "de": "Der Arzt ist heute nicht hier."},
            {"en": "I need medicine.", "de": "Ich brauche Medizin."},
            {"en": "She is feeling better.", "de": "Es geht ihr besser."},
            {"en": "My leg hurts.", "de": "Mir tut das Bein weh."},
            {"en": "I do not smoke.", "de": "Ich rauche nicht."},
            {"en": "He has no appetite.", "de": "Er hat keinen Appetit."},
            {"en": "I sleep eight hours.", "de": "Ich schlafe acht Stunden."},
            {"en": "Are you ill?", "de": "Bist du krank?"},
            {"en": "I am not well today.", "de": "Mir geht es heute nicht gut."},
            {"en": "She takes the medicine.", "de": "Sie nimmt die Medizin."},
            {"en": "My arm hurts.", "de": "Mir tut der Arm weh."},
            {"en": "I have no pain.", "de": "Ich habe keine Schmerzen."},
            {"en": "He goes to the doctor.", "de": "Er geht zum Arzt."},
            {"en": "Health is the most important thing.", "de": "Gesundheit ist das Wichtigste."},
        ],
    },

    ("A1", "books_films"): {
        "note": (
            "📖 Books and Films — A1\n\n"
            "NOUN PLURALS — irregular, learn them with the noun. Common patterns:\n"
            "• -e (often + umlaut): der Film → die Filme, das Buch → die Bücher\n"
            "• -n/-en: die Geschichte → die Geschichten\n"
            "• -er: das Kind → die Kinder\n"
            "• -s: das Auto → die Autos, das Kino → die Kinos\n"
            "• no change: der Computer → die Computer\n"
            "The plural article is always die.\n\n"
            "SAYING WHAT YOU LIKE — gern (after the verb)\n"
            "Ich lese gern. (I like reading.)  ·  Ich sehe gern Filme.  ·  "
            "Ich spiele nicht gern Karten.\n"
            "lieber = prefer: Ich lese lieber Bücher.\n\n"
            "VOCAB: das Buch/die Bücher, der Film/die Filme, das Kino, die Geschichte, "
            "der Autor, die Serie, lesen, sehen, langweilig, spannend, lustig, traurig.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I like reading.", "de": "Ich lese gern."},
            {"en": "I read a book.", "de": "Ich lese ein Buch."},
            {"en": "I have many books.", "de": "Ich habe viele Bücher."},
            {"en": "We watch a film.", "de": "Wir sehen einen Film."},
            {"en": "I like watching films.", "de": "Ich sehe gern Filme."},
            {"en": "The film is exciting.", "de": "Der Film ist spannend."},
            {"en": "She reads two books a week.", "de": "Sie liest zwei Bücher pro Woche."},
            {"en": "The book is boring.", "de": "Das Buch ist langweilig."},
            {"en": "We go to the cinema.", "de": "Wir gehen ins Kino."},
            {"en": "I don't like horror films.", "de": "Ich sehe nicht gern Horrorfilme."},
            {"en": "He reads a newspaper.", "de": "Er liest eine Zeitung."},
            {"en": "The films are very long.", "de": "Die Filme sind sehr lang."},
            {"en": "I prefer comedies.", "de": "Ich mag lieber Komödien."},
            {"en": "This story is funny.", "de": "Diese Geschichte ist lustig."},
            {"en": "Do you like reading?", "de": "Liest du gern?"},
            {"en": "The children watch a cartoon.", "de": "Die Kinder sehen einen Zeichentrickfilm."},
            {"en": "I read every evening.", "de": "Ich lese jeden Abend."},
            {"en": "She likes romantic films.", "de": "Sie sieht gern Liebesfilme."},
            {"en": "The author is famous.", "de": "Der Autor ist berühmt."},
            {"en": "We watch a series.", "de": "Wir sehen eine Serie."},
            {"en": "I have no time to read.", "de": "Ich habe keine Zeit zum Lesen."},
            {"en": "The cinema is new.", "de": "Das Kino ist neu."},
            {"en": "He reads science fiction.", "de": "Er liest Science-Fiction."},
            {"en": "The book is very interesting.", "de": "Das Buch ist sehr interessant."},
            {"en": "I watch films in German.", "de": "Ich sehe Filme auf Deutsch."},
            {"en": "She tells a story.", "de": "Sie erzählt eine Geschichte."},
            {"en": "We like the same films.", "de": "Wir mögen die gleichen Filme."},
            {"en": "The story is sad.", "de": "Die Geschichte ist traurig."},
            {"en": "I buy two tickets.", "de": "Ich kaufe zwei Karten."},
            {"en": "The film starts at eight.", "de": "Der Film beginnt um acht."},
            {"en": "He doesn't read much.", "de": "Er liest nicht viel."},
            {"en": "I love good books.", "de": "Ich liebe gute Bücher."},
            {"en": "The series has many episodes.", "de": "Die Serie hat viele Folgen."},
            {"en": "Do you watch films often?", "de": "Siehst du oft Filme?"},
            {"en": "I read the book twice.", "de": "Ich lese das Buch zweimal."},
            {"en": "My sister likes comics.", "de": "Meine Schwester mag Comics."},
            {"en": "The actor is very good.", "de": "Der Schauspieler ist sehr gut."},
            {"en": "We watch a film together.", "de": "Wir sehen zusammen einen Film."},
            {"en": "I prefer reading.", "de": "Ich lese lieber."},
            {"en": "Books are my hobby.", "de": "Bücher sind mein Hobby."},
        ],
    },

    ("A1", "accommodation"): {
        "note": (
            "📖 Accommodation — A1\n\n"
            "WHERE THINGS ARE — prepositions + Dativ (location, with \"wo?\")\n"
            "in, an (at/on a wall), auf (on top), unter (under), neben (next to), "
            "vor (in front of), hinter (behind), zwischen (between), über (above).\n"
            "Dativ articles: der/das → dem, die → der, plural → den (+n).\n"
            "Contractions: in dem → im, an dem → am.\n"
            "• Das Buch ist auf dem Tisch.  ·  Die Lampe ist neben dem Bett.  ·  Ich bin im Wohnzimmer.\n\n"
            "es gibt = there is / there are (+ Akkusativ):\n"
            "• Es gibt einen Balkon.  ·  Es gibt zwei Schlafzimmer.\n\n"
            "VOCAB: die Wohnung, das Haus, das Zimmer, die Küche, das Bad, das Wohnzimmer, "
            "das Schlafzimmer, der Tisch, der Stuhl, das Bett, das Sofa, der Schrank, die Lampe.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "The book is on the table.", "de": "Das Buch ist auf dem Tisch."},
            {"en": "I am in the kitchen.", "de": "Ich bin in der Küche."},
            {"en": "The lamp is next to the bed.", "de": "Die Lampe ist neben dem Bett."},
            {"en": "We live in a flat.", "de": "Wir wohnen in einer Wohnung."},
            {"en": "There is a balcony.", "de": "Es gibt einen Balkon."},
            {"en": "The chair is in front of the table.", "de": "Der Stuhl ist vor dem Tisch."},
            {"en": "My room is very small.", "de": "Mein Zimmer ist sehr klein."},
            {"en": "The cat is under the sofa.", "de": "Die Katze ist unter dem Sofa."},
            {"en": "There are two bedrooms.", "de": "Es gibt zwei Schlafzimmer."},
            {"en": "The kitchen is big.", "de": "Die Küche ist groß."},
            {"en": "The picture is on the wall.", "de": "Das Bild ist an der Wand."},
            {"en": "I sit on the sofa.", "de": "Ich sitze auf dem Sofa."},
            {"en": "The bathroom is next to the bedroom.", "de": "Das Bad ist neben dem Schlafzimmer."},
            {"en": "We have a garden.", "de": "Wir haben einen Garten."},
            {"en": "The keys are on the table.", "de": "Die Schlüssel sind auf dem Tisch."},
            {"en": "There is no elevator.", "de": "Es gibt keinen Aufzug."},
            {"en": "The flat is on the third floor.", "de": "Die Wohnung ist im dritten Stock."},
            {"en": "My bed is by the window.", "de": "Mein Bett ist am Fenster."},
            {"en": "The wardrobe is in the bedroom.", "de": "Der Schrank ist im Schlafzimmer."},
            {"en": "We are in the living room.", "de": "Wir sind im Wohnzimmer."},
            {"en": "The car is in front of the house.", "de": "Das Auto ist vor dem Haus."},
            {"en": "There is a big kitchen.", "de": "Es gibt eine große Küche."},
            {"en": "The dog sleeps under the table.", "de": "Der Hund schläft unter dem Tisch."},
            {"en": "My flat has three rooms.", "de": "Meine Wohnung hat drei Zimmer."},
            {"en": "The lamp is over the table.", "de": "Die Lampe ist über dem Tisch."},
            {"en": "The bag is behind the door.", "de": "Die Tasche ist hinter der Tür."},
            {"en": "We need a new sofa.", "de": "Wir brauchen ein neues Sofa."},
            {"en": "The kitchen is between the rooms.", "de": "Die Küche ist zwischen den Zimmern."},
            {"en": "There is a small bathroom.", "de": "Es gibt ein kleines Bad."},
            {"en": "The flat is very bright.", "de": "Die Wohnung ist sehr hell."},
            {"en": "My desk is by the window.", "de": "Mein Schreibtisch ist am Fenster."},
            {"en": "The plant is on the floor.", "de": "Die Pflanze ist auf dem Boden."},
            {"en": "There are many windows.", "de": "Es gibt viele Fenster."},
            {"en": "The rent is too high.", "de": "Die Miete ist zu hoch."},
            {"en": "We live on the ground floor.", "de": "Wir wohnen im Erdgeschoss."},
            {"en": "The chairs are in the kitchen.", "de": "Die Stühle sind in der Küche."},
            {"en": "There is a garage.", "de": "Es gibt eine Garage."},
            {"en": "My room is on the left.", "de": "Mein Zimmer ist links."},
            {"en": "The house has a garden.", "de": "Das Haus hat einen Garten."},
            {"en": "I am looking for a new flat.", "de": "Ich suche eine neue Wohnung."},
        ],
    },

    ("A1", "clothes_fashion"): {
        "note": (
            "📖 Clothes & Fashion — A1\n\n"
            "ADJECTIVES AFTER THE VERB (predicative) — NO ending!\n"
            "After sein / werden / bleiben, the adjective never changes:\n"
            "• Die Jacke ist neu.  ·  Die Schuhe sind teuer.  ·  Das Kleid ist schön.\n"
            "(Endings before a noun come later, at A2.)\n\n"
            "COLOURS: rot, blau, grün, gelb, schwarz, weiß, braun, grau, orange, rosa.\n"
            "• Der Pullover ist blau.  ·  Meine Schuhe sind schwarz.\n\n"
            "CLOTHES VOCAB\n"
            "die Jacke, die Hose, das Hemd, das T-Shirt, der Pullover, das Kleid, der Rock, "
            "die Schuhe, die Mütze, der Schal, die Socken, der Mantel.\n"
            "tragen (to wear): ich trage, du trägst, er trägt.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "The jacket is new.", "de": "Die Jacke ist neu."},
            {"en": "The shoes are black.", "de": "Die Schuhe sind schwarz."},
            {"en": "My shirt is white.", "de": "Mein Hemd ist weiß."},
            {"en": "The dress is beautiful.", "de": "Das Kleid ist schön."},
            {"en": "I wear a jacket.", "de": "Ich trage eine Jacke."},
            {"en": "The trousers are too big.", "de": "Die Hose ist zu groß."},
            {"en": "The T-shirt is red.", "de": "Das T-Shirt ist rot."},
            {"en": "My socks are green.", "de": "Meine Socken sind grün."},
            {"en": "Do you wear a hat?", "de": "Trägst du eine Mütze?"},
            {"en": "The coat is very warm.", "de": "Der Mantel ist sehr warm."},
            {"en": "The skirt is too short.", "de": "Der Rock ist zu kurz."},
            {"en": "Her dress is yellow.", "de": "Ihr Kleid ist gelb."},
            {"en": "I wear a scarf in winter.", "de": "Ich trage im Winter einen Schal."},
            {"en": "The shoes are expensive.", "de": "Die Schuhe sind teuer."},
            {"en": "My jacket is brown.", "de": "Meine Jacke ist braun."},
            {"en": "The shirt is dirty.", "de": "Das Hemd ist schmutzig."},
            {"en": "His coat is black.", "de": "Sein Mantel ist schwarz."},
            {"en": "The pullover is too small.", "de": "Der Pullover ist zu klein."},
            {"en": "I like the colour blue.", "de": "Ich mag die Farbe Blau."},
            {"en": "The clothes are cheap.", "de": "Die Kleidung ist billig."},
            {"en": "My shoes are new.", "de": "Meine Schuhe sind neu."},
            {"en": "The hat is grey.", "de": "Die Mütze ist grau."},
            {"en": "She wears a dress.", "de": "Sie trägt ein Kleid."},
            {"en": "The trousers are black.", "de": "Die Hose ist schwarz."},
            {"en": "This jacket is too expensive.", "de": "Diese Jacke ist zu teuer."},
            {"en": "My T-shirt is orange.", "de": "Mein T-Shirt ist orange."},
            {"en": "He wears glasses.", "de": "Er trägt eine Brille."},
            {"en": "The socks are white.", "de": "Die Socken sind weiß."},
            {"en": "The skirt is pink.", "de": "Der Rock ist rosa."},
            {"en": "I need new shoes.", "de": "Ich brauche neue Schuhe."},
            {"en": "The coat is long.", "de": "Der Mantel ist lang."},
            {"en": "Her shirt is light blue.", "de": "Ihr Hemd ist hellblau."},
            {"en": "The clothes are comfortable.", "de": "Die Kleidung ist bequem."},
            {"en": "The colour is very nice.", "de": "Die Farbe ist sehr schön."},
            {"en": "My jacket is too big.", "de": "Meine Jacke ist zu groß."},
            {"en": "The dress is green.", "de": "Das Kleid ist grün."},
            {"en": "I buy a shirt.", "de": "Ich kaufe ein Hemd."},
            {"en": "The shoes are very comfortable.", "de": "Die Schuhe sind sehr bequem."},
            {"en": "What are you wearing today?", "de": "Was trägst du heute?"},
            {"en": "Red is my favorite color.", "de": "Rot ist meine Lieblingsfarbe."},
        ],
    },

    ("A1", "personality"): {
        "note": (
            "📖 Personality — A1\n\n"
            "DESCRIBING PEOPLE — sein + adjective (predicative, no ending)\n"
            "• Er ist freundlich.  ·  Sie ist sehr nett.  ·  Wir sind glücklich.\n\n"
            "INTENSIFIERS (placed before the adjective)\n"
            "sehr (very) · ziemlich (quite) · total (totally) · wirklich (really) · "
            "ein bisschen (a bit) · nicht so (not so) · zu (too).\n"
            "• Sie ist ziemlich ruhig.  ·  Er ist ein bisschen schüchtern.  ·  Das ist nicht so wichtig.\n\n"
            "PERSONALITY ADJECTIVES\n"
            "nett, freundlich, ruhig, laut, lustig, ernst (serious), fleißig (hard-working), "
            "faul (lazy), höflich (polite), ehrlich (honest), geduldig (patient), "
            "nervös, schüchtern (shy), offen (open).\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "He is friendly.", "de": "Er ist freundlich."},
            {"en": "She is very nice.", "de": "Sie ist sehr nett."},
            {"en": "I am happy.", "de": "Ich bin glücklich."},
            {"en": "He is quite quiet.", "de": "Er ist ziemlich ruhig."},
            {"en": "She is funny.", "de": "Sie ist lustig."},
            {"en": "We are very patient.", "de": "Wir sind sehr geduldig."},
            {"en": "He is a bit shy.", "de": "Er ist ein bisschen schüchtern."},
            {"en": "My friend is honest.", "de": "Mein Freund ist ehrlich."},
            {"en": "She is hard-working.", "de": "Sie ist fleißig."},
            {"en": "He is sometimes lazy.", "de": "Er ist manchmal faul."},
            {"en": "You are very polite.", "de": "Du bist sehr höflich."},
            {"en": "The teacher is strict.", "de": "Der Lehrer ist streng."},
            {"en": "I am a little nervous.", "de": "Ich bin ein bisschen nervös."},
            {"en": "She is really friendly.", "de": "Sie ist wirklich freundlich."},
            {"en": "He is not so serious.", "de": "Er ist nicht so ernst."},
            {"en": "My sister is very loud.", "de": "Meine Schwester ist sehr laut."},
            {"en": "They are very kind.", "de": "Sie sind sehr freundlich."},
            {"en": "He is always happy.", "de": "Er ist immer glücklich."},
            {"en": "She is quite open.", "de": "Sie ist ziemlich offen."},
            {"en": "My boss is impatient.", "de": "Mein Chef ist ungeduldig."},
            {"en": "I am calm.", "de": "Ich bin ruhig."},
            {"en": "He is reliable.", "de": "Er ist zuverlässig."},
            {"en": "She is totally relaxed.", "de": "Sie ist total entspannt."},
            {"en": "You are too serious.", "de": "Du bist zu ernst."},
            {"en": "My brother is funny.", "de": "Mein Bruder ist lustig."},
            {"en": "The child is shy.", "de": "Das Kind ist schüchtern."},
            {"en": "She is very intelligent.", "de": "Sie ist sehr intelligent."},
            {"en": "He is friendly and polite.", "de": "Er ist freundlich und höflich."},
            {"en": "I am not lazy.", "de": "Ich bin nicht faul."},
            {"en": "She is always honest.", "de": "Sie ist immer ehrlich."},
            {"en": "My colleague is helpful.", "de": "Mein Kollege ist hilfsbereit."},
            {"en": "He is quite serious today.", "de": "Er ist heute ziemlich ernst."},
            {"en": "They are very hard-working.", "de": "Sie sind sehr fleißig."},
            {"en": "She is a bit nervous.", "de": "Sie ist ein bisschen nervös."},
            {"en": "You are very kind.", "de": "Du bist sehr nett."},
            {"en": "He is rarely angry.", "de": "Er ist selten wütend."},
            {"en": "My mother is patient.", "de": "Meine Mutter ist geduldig."},
            {"en": "The man is unfriendly.", "de": "Der Mann ist unfreundlich."},
            {"en": "She is really funny.", "de": "Sie ist wirklich lustig."},
            {"en": "I am proud of you.", "de": "Ich bin stolz auf dich."},
        ],
    },

    ("A1", "business"): {
        "note": (
            "📖 Business and Money — A1\n\n"
            "NUMBERS\n"
            "0 null · 1 eins · 2 zwei · 3 drei · 4 vier · 5 fünf · 6 sechs · 7 sieben · "
            "8 acht · 9 neun · 10 zehn · 11 elf · 12 zwölf · 20 zwanzig · "
            "21 einundzwanzig · 30 dreißig · 100 hundert · 1000 tausend.\n"
            "Order: 21 = ein-und-zwanzig (one-and-twenty).\n\n"
            "MONEY & PRICES\n"
            "der Euro, der Cent, das Geld, der Preis, kosten, bezahlen, kaufen, verkaufen, billig, teuer.\n"
            "• Was kostet das? — How much is that?\n"
            "• Das kostet zehn Euro.  ·  Das ist zu teuer.  ·  Ich bezahle mit Karte.\n\n"
            "VOCAB: die Bank, das Konto, die Rechnung (bill), das Bargeld (cash), "
            "die Karte (card), günstig (good value), das Angebot (offer).\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "How much is that?", "de": "Was kostet das?"},
            {"en": "That costs ten euros.", "de": "Das kostet zehn Euro."},
            {"en": "It is too expensive.", "de": "Das ist zu teuer."},
            {"en": "I pay with card.", "de": "Ich bezahle mit Karte."},
            {"en": "I have no cash.", "de": "Ich habe kein Bargeld."},
            {"en": "The book costs twelve euros.", "de": "Das Buch kostet zwölf Euro."},
            {"en": "That is very cheap.", "de": "Das ist sehr billig."},
            {"en": "I would like to pay.", "de": "Ich möchte bezahlen."},
            {"en": "The price is good.", "de": "Der Preis ist gut."},
            {"en": "I buy a ticket.", "de": "Ich kaufe eine Karte."},
            {"en": "We sell our car.", "de": "Wir verkaufen unser Auto."},
            {"en": "The bill is twenty euros.", "de": "Die Rechnung ist zwanzig Euro."},
            {"en": "Do you have change?", "de": "Hast du Kleingeld?"},
            {"en": "The coffee costs three euros.", "de": "Der Kaffee kostet drei Euro."},
            {"en": "I have one hundred euros.", "de": "Ich habe hundert Euro."},
            {"en": "The offer is good.", "de": "Das Angebot ist gut."},
            {"en": "The shoes cost fifty euros.", "de": "Die Schuhe kosten fünfzig Euro."},
            {"en": "I need money.", "de": "Ich brauche Geld."},
            {"en": "Can I pay here?", "de": "Kann ich hier bezahlen?"},
            {"en": "The bank is closed.", "de": "Die Bank ist geschlossen."},
            {"en": "It costs twenty-one euros.", "de": "Es kostet einundzwanzig Euro."},
            {"en": "We have no money.", "de": "Wir haben kein Geld."},
            {"en": "The price is too high.", "de": "Der Preis ist zu hoch."},
            {"en": "I buy two tickets.", "de": "Ich kaufe zwei Karten."},
            {"en": "That is good value.", "de": "Das ist günstig."},
            {"en": "The phone costs three hundred euros.", "de": "Das Handy kostet dreihundert Euro."},
            {"en": "I pay in cash.", "de": "Ich bezahle bar."},
            {"en": "How much does the bag cost?", "de": "Was kostet die Tasche?"},
            {"en": "The hotel is expensive.", "de": "Das Hotel ist teuer."},
            {"en": "I have a bank account.", "de": "Ich habe ein Konto."},
            {"en": "The rent is eight hundred euros.", "de": "Die Miete ist achthundert Euro."},
            {"en": "We pay the bill.", "de": "Wir bezahlen die Rechnung."},
            {"en": "The price is fair.", "de": "Der Preis ist fair."},
            {"en": "I save my money.", "de": "Ich spare mein Geld."},
            {"en": "The ticket costs nine euros.", "de": "Die Karte kostet neun Euro."},
            {"en": "Do you accept cards?", "de": "Nehmt ihr Karten?"},
            {"en": "It is on offer.", "de": "Es ist im Angebot."},
            {"en": "I earn enough money.", "de": "Ich verdiene genug Geld."},
            {"en": "The shop is cheap.", "de": "Der Laden ist billig."},
            {"en": "Time is money.", "de": "Zeit ist Geld."},
        ],
    },

    ("A1", "physical_appearance"): {
        "note": (
            "📖 Physical Appearance — A1\n\n"
            "DESCRIBING HOW SOMEONE LOOKS — two easy patterns:\n"
            "1) sein + adjective (predicative, no ending):\n"
            "   Er ist groß.  ·  Sie ist klein.  ·  Er ist jung.  ·  Sie ist schlank.\n"
            "2) haben + a feature:\n"
            "   Er hat eine Brille.  ·  Sie hat lange Haare.  ·  Er hat einen Bart.\n"
            "Also: Seine Augen sind blau.  ·  Ihre Haare sind kurz.\n\n"
            "VOCAB: groß (tall), klein (short), jung (young), alt (old), schlank (slim), "
            "die Haare (hair), die Augen (eyes), der Bart (beard), die Brille (glasses), "
            "blond, dunkel (dark), kurz (short), lang (long), schön, hübsch (pretty).\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "He is tall.", "de": "Er ist groß."},
            {"en": "She is small.", "de": "Sie ist klein."},
            {"en": "He is young.", "de": "Er ist jung."},
            {"en": "She is old.", "de": "Sie ist alt."},
            {"en": "He wears glasses.", "de": "Er trägt eine Brille."},
            {"en": "Her hair is long.", "de": "Ihre Haare sind lang."},
            {"en": "His eyes are blue.", "de": "Seine Augen sind blau."},
            {"en": "She is very pretty.", "de": "Sie ist sehr hübsch."},
            {"en": "He has a beard.", "de": "Er hat einen Bart."},
            {"en": "My brother is slim.", "de": "Mein Bruder ist schlank."},
            {"en": "Her hair is short.", "de": "Ihre Haare sind kurz."},
            {"en": "He is quite tall.", "de": "Er ist ziemlich groß."},
            {"en": "She has blonde hair.", "de": "Sie hat blonde Haare."},
            {"en": "His eyes are dark.", "de": "Seine Augen sind dunkel."},
            {"en": "The man is old.", "de": "Der Mann ist alt."},
            {"en": "She is beautiful.", "de": "Sie ist schön."},
            {"en": "He is not very tall.", "de": "Er ist nicht sehr groß."},
            {"en": "My sister is young.", "de": "Meine Schwester ist jung."},
            {"en": "He has short hair.", "de": "Er hat kurze Haare."},
            {"en": "Her eyes are green.", "de": "Ihre Augen sind grün."},
            {"en": "She wears glasses.", "de": "Sie trägt eine Brille."},
            {"en": "He is strong.", "de": "Er ist stark."},
            {"en": "The child is small.", "de": "Das Kind ist klein."},
            {"en": "She has long hair.", "de": "Sie hat lange Haare."},
            {"en": "His hair is dark.", "de": "Seine Haare sind dunkel."},
            {"en": "He looks young.", "de": "Er sieht jung aus."},
            {"en": "She is a little older.", "de": "Sie ist ein bisschen älter."},
            {"en": "My father has a beard.", "de": "Mein Vater hat einen Bart."},
            {"en": "He is tall and slim.", "de": "Er ist groß und schlank."},
            {"en": "Her hair is blonde.", "de": "Ihre Haare sind blond."},
            {"en": "The woman is pretty.", "de": "Die Frau ist hübsch."},
            {"en": "He has brown eyes.", "de": "Er hat braune Augen."},
            {"en": "She is taller than me.", "de": "Sie ist größer als ich."},
            {"en": "My grandmother is old.", "de": "Meine Großmutter ist alt."},
            {"en": "He looks tired.", "de": "Er sieht müde aus."},
            {"en": "She has beautiful eyes.", "de": "Sie hat schöne Augen."},
            {"en": "He is handsome.", "de": "Er ist gutaussehend."},
            {"en": "Her smile is beautiful.", "de": "Ihr Lächeln ist schön."},
            {"en": "His beard is long.", "de": "Sein Bart ist lang."},
            {"en": "She looks like her mother.", "de": "Sie sieht wie ihre Mutter aus."},
        ],
    },

    ("A1", "town_city"): {
        "note": (
            "📖 Town and City — A1\n\n"
            "SEPARABLE VERBS\n"
            "Some verbs have a prefix that SPLITS OFF and jumps to the END in a main clause.\n"
            "Infinitive: ankommen → Der Zug kommt um acht an.\n"
            "Common ones: aufstehen (get up), einkaufen (shop), abfahren (depart), "
            "ankommen (arrive), anrufen (call), aufmachen (open), zumachen (close), "
            "mitkommen (come along), aussteigen (get off), umsteigen (change/transfer).\n"
            "• Ich stehe um sieben auf.  ·  Wir kaufen im Supermarkt ein.  ·  Der Bus fährt gleich ab.\n"
            "After a modal it stays together: Ich muss früh aufstehen.\n\n"
            "VOCAB: die Stadt, das Dorf, die Straße, der Platz, der Bahnhof, die Haltestelle, "
            "der Bus, die U-Bahn, der Zug, das Rathaus, der Markt, die Brücke, "
            "links, rechts, geradeaus.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I get up at seven.", "de": "Ich stehe um sieben auf."},
            {"en": "The train arrives at eight.", "de": "Der Zug kommt um acht an."},
            {"en": "We shop at the supermarket.", "de": "Wir kaufen im Supermarkt ein."},
            {"en": "The bus departs soon.", "de": "Der Bus fährt gleich ab."},
            {"en": "I call my friend.", "de": "Ich rufe meinen Freund an."},
            {"en": "Do you come along?", "de": "Kommst du mit?"},
            {"en": "The shop opens at nine.", "de": "Der Laden macht um neun auf."},
            {"en": "I get off at the station.", "de": "Ich steige am Bahnhof aus."},
            {"en": "The city is very big.", "de": "Die Stadt ist sehr groß."},
            {"en": "We change at the next stop.", "de": "Wir steigen an der nächsten Haltestelle um."},
            {"en": "Go straight ahead.", "de": "Gehen Sie geradeaus."},
            {"en": "The bus stop is on the left.", "de": "Die Haltestelle ist links."},
            {"en": "I get up early.", "de": "Ich stehe früh auf."},
            {"en": "She calls the doctor.", "de": "Sie ruft den Arzt an."},
            {"en": "The train leaves at ten.", "de": "Der Zug fährt um zehn ab."},
            {"en": "We go shopping today.", "de": "Wir kaufen heute ein."},
            {"en": "The town hall is in the centre.", "de": "Das Rathaus ist im Zentrum."},
            {"en": "Turn right at the bridge.", "de": "Biegen Sie an der Brücke rechts ab."},
            {"en": "I have to get up early.", "de": "Ich muss früh aufstehen."},
            {"en": "The museum opens at ten.", "de": "Das Museum macht um zehn auf."},
            {"en": "Where is the station?", "de": "Wo ist der Bahnhof?"},
            {"en": "The market is on the square.", "de": "Der Markt ist auf dem Platz."},
            {"en": "We arrive in the evening.", "de": "Wir kommen am Abend an."},
            {"en": "He closes the window.", "de": "Er macht das Fenster zu."},
            {"en": "I take the subway.", "de": "Ich nehme die U-Bahn."},
            {"en": "The street is very long.", "de": "Die Straße ist sehr lang."},
            {"en": "Do you want to come along?", "de": "Willst du mitkommen?"},
            {"en": "The bus arrives late.", "de": "Der Bus kommt spät an."},
            {"en": "She gets off here.", "de": "Sie steigt hier aus."},
            {"en": "We buy fruit at the market.", "de": "Wir kaufen Obst auf dem Markt."},
            {"en": "The train departs from platform two.", "de": "Der Zug fährt von Gleis zwei ab."},
            {"en": "I get up at six every day.", "de": "Ich stehe jeden Tag um sechs auf."},
            {"en": "The bridge is very old.", "de": "Die Brücke ist sehr alt."},
            {"en": "Please open the door.", "de": "Machen Sie bitte die Tür auf."},
            {"en": "The city has a beautiful park.", "de": "Die Stadt hat einen schönen Park."},
            {"en": "We change trains in Berlin.", "de": "Wir steigen in Berlin um."},
            {"en": "The bank is next to the post office.", "de": "Die Bank ist neben der Post."},
            {"en": "I call you tomorrow.", "de": "Ich rufe dich morgen an."},
            {"en": "The supermarket closes at eight.", "de": "Der Supermarkt macht um acht zu."},
            {"en": "The village is small and quiet.", "de": "Das Dorf ist klein und ruhig."},
        ],
    },

    ("A1", "music"): {
        "note": (
            "📖 Music — A1\n\n"
            "COORDINATING CONJUNCTIONS — they join two main clauses WITHOUT changing word "
            "order. The verb still stays in position 2.\n"
            "und (and) · aber (but) · oder (or) · denn (because).\n"
            "• Ich höre Musik und ich tanze.\n"
            "• Ich spiele Gitarre, aber ich singe nicht.\n"
            "• Magst du Rock oder magst du Pop?\n"
            "• Ich bleibe zu Hause, denn ich bin müde.\n"
            "With und/oder you can drop the repeated subject: Ich singe und tanze.\n\n"
            "VOCAB: die Musik, das Lied (song), die Band, das Konzert, das Instrument, "
            "die Gitarre, das Klavier (piano), die Geige (violin), das Schlagzeug (drums), "
            "singen, spielen, hören, tanzen, laut, leise (quiet).\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I listen to music.", "de": "Ich höre Musik."},
            {"en": "I sing and I dance.", "de": "Ich singe und ich tanze."},
            {"en": "I play guitar.", "de": "Ich spiele Gitarre."},
            {"en": "She sings well.", "de": "Sie singt gut."},
            {"en": "I like rock, but I don't like jazz.", "de": "Ich mag Rock, aber ich mag keinen Jazz."},
            {"en": "Do you play piano or guitar?", "de": "Spielst du Klavier oder Gitarre?"},
            {"en": "We go to a concert.", "de": "Wir gehen zu einem Konzert."},
            {"en": "The music is too loud.", "de": "Die Musik ist zu laut."},
            {"en": "I stay home because I am tired.", "de": "Ich bleibe zu Hause, denn ich bin müde."},
            {"en": "He plays the violin.", "de": "Er spielt Geige."},
            {"en": "I sing and dance.", "de": "Ich singe und tanze."},
            {"en": "She listens to music and reads a book.", "de": "Sie hört Musik und liest ein Buch."},
            {"en": "I like pop, but he likes rock.", "de": "Ich mag Pop, aber er mag Rock."},
            {"en": "The band is very famous.", "de": "Die Band ist sehr berühmt."},
            {"en": "Do you sing or do you play an instrument?", "de": "Singst du oder spielst du ein Instrument?"},
            {"en": "I learn the piano.", "de": "Ich lerne Klavier."},
            {"en": "The song is beautiful.", "de": "Das Lied ist schön."},
            {"en": "We dance because the music is good.", "de": "Wir tanzen, denn die Musik ist gut."},
            {"en": "He plays drums in a band.", "de": "Er spielt Schlagzeug in einer Band."},
            {"en": "I like the song, but it is too long.", "de": "Ich mag das Lied, aber es ist zu lang."},
            {"en": "She sings in a choir.", "de": "Sie singt in einem Chor."},
            {"en": "Do you listen to the radio or to CDs?", "de": "Hörst du Radio oder CDs?"},
            {"en": "The concert starts at eight.", "de": "Das Konzert beginnt um acht."},
            {"en": "I play guitar and he sings.", "de": "Ich spiele Gitarre und er singt."},
            {"en": "I am happy because I love music.", "de": "Ich bin glücklich, denn ich liebe Musik."},
            {"en": "The music is quiet.", "de": "Die Musik ist leise."},
            {"en": "She has a beautiful voice.", "de": "Sie hat eine schöne Stimme."},
            {"en": "We sing together.", "de": "Wir singen zusammen."},
            {"en": "I don't dance, but I sing.", "de": "Ich tanze nicht, aber ich singe."},
            {"en": "He buys a new guitar.", "de": "Er kauft eine neue Gitarre."},
            {"en": "The concert is sold out.", "de": "Das Konzert ist ausverkauft."},
            {"en": "I listen to music every day.", "de": "Ich höre jeden Tag Musik."},
            {"en": "Do you like classical music?", "de": "Magst du klassische Musik?"},
            {"en": "She plays piano and guitar.", "de": "Sie spielt Klavier und Gitarre."},
            {"en": "The song is on the radio.", "de": "Das Lied läuft im Radio."},
            {"en": "I sing because I am happy.", "de": "Ich singe, denn ich bin glücklich."},
            {"en": "The musicians are very good.", "de": "Die Musiker sind sehr gut."},
            {"en": "I like the melody, but not the lyrics.", "de": "Ich mag die Melodie, aber nicht den Text."},
            {"en": "We listen to music and relax.", "de": "Wir hören Musik und entspannen uns."},
            {"en": "Music makes me happy.", "de": "Musik macht mich glücklich."},
        ],
    },

    ("A1", "weather"): {
        "note": (
            "📖 Weather — A1\n\n"
            "THE IMPERSONAL \"es\"\n"
            "German weather uses es (\"it\") as a dummy subject, like English \"it is raining\".\n"
            "• Es regnet.  ·  Es schneit.  ·  Es ist kalt / warm / heiß / sonnig / windig.\n"
            "• Es gibt ein Gewitter. (There is a storm.)\n"
            "The verb stays in position 2: Heute ist es kalt.  ·  Im Sommer ist es heiß.\n\n"
            "ASKING\n"
            "Wie ist das Wetter? — What is the weather like?\n\n"
            "VOCAB: das Wetter, die Sonne, der Regen, der Schnee, der Wind, die Wolke, "
            "der Himmel, das Gewitter (storm), der Nebel (fog), das Grad (degree), "
            "sonnig, bewölkt (cloudy), kalt, warm, heiß.\n"
            "SEASONS: der Frühling, der Sommer, der Herbst, der Winter.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "It is raining.", "de": "Es regnet."},
            {"en": "It is cold.", "de": "Es ist kalt."},
            {"en": "It is warm today.", "de": "Heute ist es warm."},
            {"en": "It is snowing.", "de": "Es schneit."},
            {"en": "The sun is shining.", "de": "Die Sonne scheint."},
            {"en": "It is very hot.", "de": "Es ist sehr heiß."},
            {"en": "What is the weather like?", "de": "Wie ist das Wetter?"},
            {"en": "It is windy.", "de": "Es ist windig."},
            {"en": "The sky is blue.", "de": "Der Himmel ist blau."},
            {"en": "It is cloudy.", "de": "Es ist bewölkt."},
            {"en": "It rains a lot in autumn.", "de": "Im Herbst regnet es viel."},
            {"en": "It is sunny.", "de": "Es ist sonnig."},
            {"en": "It is ten degrees.", "de": "Es ist zehn Grad."},
            {"en": "It is foggy.", "de": "Es ist neblig."},
            {"en": "In summer it is hot.", "de": "Im Sommer ist es heiß."},
            {"en": "It is snowing in the mountains.", "de": "In den Bergen schneit es."},
            {"en": "There is a storm.", "de": "Es gibt ein Gewitter."},
            {"en": "The weather is nice.", "de": "Das Wetter ist schön."},
            {"en": "It is raining again.", "de": "Es regnet wieder."},
            {"en": "In winter it is very cold.", "de": "Im Winter ist es sehr kalt."},
            {"en": "The wind is strong.", "de": "Der Wind ist stark."},
            {"en": "It is too hot for me.", "de": "Es ist mir zu heiß."},
            {"en": "The weather is bad.", "de": "Das Wetter ist schlecht."},
            {"en": "It is getting dark.", "de": "Es wird dunkel."},
            {"en": "The sun is warm.", "de": "Die Sonne ist warm."},
            {"en": "It is cold outside.", "de": "Draußen ist es kalt."},
            {"en": "In spring the weather is nice.", "de": "Im Frühling ist das Wetter schön."},
            {"en": "It is twenty degrees today.", "de": "Heute ist es zwanzig Grad."},
            {"en": "It often rains here.", "de": "Hier regnet es oft."},
            {"en": "The clouds are grey.", "de": "Die Wolken sind grau."},
            {"en": "It is freezing.", "de": "Es friert."},
            {"en": "The weather is changing.", "de": "Das Wetter ändert sich."},
            {"en": "It is warm in the house.", "de": "Im Haus ist es warm."},
            {"en": "It is a beautiful day.", "de": "Es ist ein schöner Tag."},
            {"en": "The rain is cold.", "de": "Der Regen ist kalt."},
            {"en": "It will rain tomorrow.", "de": "Morgen regnet es."},
            {"en": "The summer is hot.", "de": "Der Sommer ist heiß."},
            {"en": "It is snowing all day.", "de": "Es schneit den ganzen Tag."},
            {"en": "I like the autumn.", "de": "Ich mag den Herbst."},
            {"en": "The weather is warm and sunny.", "de": "Das Wetter ist warm und sonnig."},
        ],
    },

    ("A1", "shopping"): {
        "note": (
            "📖 Shopping — A1\n\n"
            "THE IMPERATIVE (instructions / requests)\n"
            "du-form: take the du-form, drop -st and \"du\": du nimmst → Nimm! · du kaufst → Kauf!\n"
            "Sie-form (polite): verb + Sie: Nehmen Sie! · Kommen Sie! · Warten Sie!\n"
            "Add bitte to soften: Warten Sie bitte einen Moment.\n\n"
            "dieser / diese / dieses = this (follows the der/die/das pattern):\n"
            "  dieser Mantel (m) · diese Jacke (f) · dieses Hemd (n) · diese Schuhe (pl).\n"
            "Masculine Akkusativ → diesen: Ich nehme diesen Mantel.\n\n"
            "VOCAB: das Geschäft / der Laden (shop), der Supermarkt, die Kasse (checkout), "
            "die Größe (size), die Tüte (bag), kaufen, nehmen, brauchen, suchen, zahlen.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I buy bread.", "de": "Ich kaufe Brot."},
            {"en": "Take this jacket.", "de": "Nimm diese Jacke."},
            {"en": "How much does this cost?", "de": "Was kostet das?"},
            {"en": "I need a bag.", "de": "Ich brauche eine Tüte."},
            {"en": "Come in, please.", "de": "Kommen Sie bitte herein."},
            {"en": "I take this shirt.", "de": "Ich nehme dieses Hemd."},
            {"en": "Where is the checkout?", "de": "Wo ist die Kasse?"},
            {"en": "This dress is beautiful.", "de": "Dieses Kleid ist schön."},
            {"en": "Wait a moment, please.", "de": "Warten Sie bitte einen Moment."},
            {"en": "I am looking for shoes.", "de": "Ich suche Schuhe."},
            {"en": "Buy the apples.", "de": "Kauf die Äpfel."},
            {"en": "This coat is too expensive.", "de": "Dieser Mantel ist zu teuer."},
            {"en": "What size do you need?", "de": "Welche Größe brauchst du?"},
            {"en": "Give me the receipt, please.", "de": "Geben Sie mir bitte den Kassenbon."},
            {"en": "I pay at the checkout.", "de": "Ich zahle an der Kasse."},
            {"en": "These shoes are cheap.", "de": "Diese Schuhe sind billig."},
            {"en": "Take this one.", "de": "Nimm diesen."},
            {"en": "The shop is open.", "de": "Das Geschäft ist offen."},
            {"en": "I would like this jacket.", "de": "Ich möchte diese Jacke."},
            {"en": "Try the pullover on.", "de": "Probier den Pullover an."},
            {"en": "Do you have this in blue?", "de": "Haben Sie das in Blau?"},
            {"en": "I buy two bottles of water.", "de": "Ich kaufe zwei Flaschen Wasser."},
            {"en": "This is on offer.", "de": "Das ist im Angebot."},
            {"en": "Pay at the counter.", "de": "Zahlen Sie an der Kasse."},
            {"en": "I need a new bag.", "de": "Ich brauche eine neue Tasche."},
            {"en": "This T-shirt is too small.", "de": "Dieses T-Shirt ist zu klein."},
            {"en": "Show me the menu, please.", "de": "Zeigen Sie mir bitte die Karte."},
            {"en": "We go shopping.", "de": "Wir gehen einkaufen."},
            {"en": "Take this jacket, it is cheap.", "de": "Nimm diese Jacke, sie ist billig."},
            {"en": "The supermarket is closed.", "de": "Der Supermarkt ist geschlossen."},
            {"en": "I look for a present.", "de": "Ich suche ein Geschenk."},
            {"en": "Give me two, please.", "de": "Geben Sie mir bitte zwei."},
            {"en": "This bag is very practical.", "de": "Diese Tasche ist sehr praktisch."},
            {"en": "Do you need a bag?", "de": "Brauchen Sie eine Tüte?"},
            {"en": "I buy this coat.", "de": "Ich kaufe diesen Mantel."},
            {"en": "The price is good.", "de": "Der Preis ist gut."},
            {"en": "Come to the shop.", "de": "Komm in den Laden."},
            {"en": "This shop is new.", "de": "Dieser Laden ist neu."},
            {"en": "I take these shoes.", "de": "Ich nehme diese Schuhe."},
            {"en": "Have a nice day!", "de": "Schönen Tag noch!"},
        ],
    },

    ("A1", "environment"): {
        "note": (
            "📖 Environment — A1 (review + sollen / dürfen)\n\n"
            "This lesson reviews negation (kein / nicht) and adds two more modals.\n"
            "sollen (should): ich soll, du sollst, er soll, wir sollen …\n"
            "dürfen (be allowed to): ich darf, du darfst, er darf, wir dürfen …\n"
            "The second verb goes to the END, like all modals.\n"
            "• Wir sollen Energie sparen.  ·  Man darf hier nicht parken.\n"
            "\"man\" = \"one / you in general\" — very common in rules.\n\n"
            "NEGATION REVIEW: kein + noun (Es gibt keine Lösung) · nicht + rest (Das ist nicht gut).\n\n"
            "VOCAB: die Umwelt, die Natur, der Müll (rubbish), das Wasser, die Luft (air), "
            "der Baum, das Plastik, recyceln, sparen (save), schützen (protect), "
            "sauber (clean), schmutzig (dirty), wichtig.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "We should save water.", "de": "Wir sollen Wasser sparen."},
            {"en": "You are not allowed to park here.", "de": "Man darf hier nicht parken."},
            {"en": "We protect the environment.", "de": "Wir schützen die Umwelt."},
            {"en": "I don't throw rubbish on the floor.", "de": "Ich werfe keinen Müll auf den Boden."},
            {"en": "The air is clean.", "de": "Die Luft ist sauber."},
            {"en": "We should recycle plastic.", "de": "Wir sollen Plastik recyceln."},
            {"en": "The water is dirty.", "de": "Das Wasser ist schmutzig."},
            {"en": "You may not smoke here.", "de": "Hier darf man nicht rauchen."},
            {"en": "Nature is beautiful.", "de": "Die Natur ist schön."},
            {"en": "We have no time to lose.", "de": "Wir haben keine Zeit zu verlieren."},
            {"en": "The environment is important.", "de": "Die Umwelt ist wichtig."},
            {"en": "We should use less plastic.", "de": "Wir sollen weniger Plastik benutzen."},
            {"en": "The river is not clean.", "de": "Der Fluss ist nicht sauber."},
            {"en": "You are allowed to swim here.", "de": "Hier darf man schwimmen."},
            {"en": "I separate the rubbish.", "de": "Ich trenne den Müll."},
            {"en": "We must protect the trees.", "de": "Wir müssen die Bäume schützen."},
            {"en": "There is too much rubbish.", "de": "Es gibt zu viel Müll."},
            {"en": "We should switch off the light.", "de": "Wir sollen das Licht ausschalten."},
            {"en": "The air is not good.", "de": "Die Luft ist nicht gut."},
            {"en": "You should save energy.", "de": "Du sollst Energie sparen."},
            {"en": "We don't use plastic bags.", "de": "Wir benutzen keine Plastiktüten."},
            {"en": "The forest is very big.", "de": "Der Wald ist sehr groß."},
            {"en": "We should drink tap water.", "de": "Wir sollen Leitungswasser trinken."},
            {"en": "You may not feed the animals.", "de": "Man darf die Tiere nicht füttern."},
            {"en": "Recycling is important.", "de": "Recycling ist wichtig."},
            {"en": "The beach is clean.", "de": "Der Strand ist sauber."},
            {"en": "We have no clean water.", "de": "Wir haben kein sauberes Wasser."},
            {"en": "We should ride a bike.", "de": "Wir sollen Fahrrad fahren."},
            {"en": "The city is dirty.", "de": "Die Stadt ist schmutzig."},
            {"en": "You are not allowed to make noise.", "de": "Man darf keinen Lärm machen."},
            {"en": "We plant a tree.", "de": "Wir pflanzen einen Baum."},
            {"en": "The sea is not clean.", "de": "Das Meer ist nicht sauber."},
            {"en": "We should waste less.", "de": "Wir sollen weniger verschwenden."},
            {"en": "Plastic is a big problem.", "de": "Plastik ist ein großes Problem."},
            {"en": "We can save energy.", "de": "Wir können Energie sparen."},
            {"en": "There is no rubbish here.", "de": "Hier gibt es keinen Müll."},
            {"en": "We should walk more.", "de": "Wir sollen mehr zu Fuß gehen."},
            {"en": "The environment needs our help.", "de": "Die Umwelt braucht unsere Hilfe."},
            {"en": "We don't have much time.", "de": "Wir haben nicht viel Zeit."},
            {"en": "Every person can help.", "de": "Jeder Mensch kann helfen."},
        ],
    },

    ("A1", "advertising"): {
        "note": (
            "📖 Advertising — A1\n\n"
            "POSSESSIVE ARTICLES (my, your, his, her, our …) — same endings as ein/kein.\n"
            "  ich → mein     ·  wir → unser\n"
            "  du → dein      ·  ihr → euer\n"
            "  er → sein      ·  sie (they) → ihr\n"
            "  sie (she) → ihr ·  Sie (formal) → Ihr\n"
            "Endings: + e for feminine/plural; + en for masculine Akkusativ.\n"
            "• Das ist mein Auto. (n)  ·  meine Firma (f)  ·  Ich liebe meinen Job. (m, Akk)\n"
            "• Kaufen Sie unser Produkt!  ·  Entdecken Sie Ihre Vorteile!\n\n"
            "VOCAB: die Werbung (advertising), das Produkt, das Angebot, der Preis, "
            "die Marke (brand), der Kunde (customer), neu, günstig, kostenlos (free), "
            "das Geschenk, kaufen, sparen.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "This is my car.", "de": "Das ist mein Auto."},
            {"en": "Buy our product!", "de": "Kaufen Sie unser Produkt!"},
            {"en": "I love my job.", "de": "Ich liebe meinen Job."},
            {"en": "Where is your bag?", "de": "Wo ist deine Tasche?"},
            {"en": "Our prices are low.", "de": "Unsere Preise sind niedrig."},
            {"en": "Discover your advantages!", "de": "Entdecken Sie Ihre Vorteile!"},
            {"en": "Her idea is good.", "de": "Ihre Idee ist gut."},
            {"en": "His product is new.", "de": "Sein Produkt ist neu."},
            {"en": "Try our new offer!", "de": "Probieren Sie unser neues Angebot!"},
            {"en": "My brand is famous.", "de": "Meine Marke ist berühmt."},
            {"en": "Your shoes are nice.", "de": "Deine Schuhe sind schön."},
            {"en": "We love our customers.", "de": "Wir lieben unsere Kunden."},
            {"en": "This is his money.", "de": "Das ist sein Geld."},
            {"en": "Save with our offer!", "de": "Sparen Sie mit unserem Angebot!"},
            {"en": "Your gift is free.", "de": "Ihr Geschenk ist kostenlos."},
            {"en": "My phone is new.", "de": "Mein Handy ist neu."},
            {"en": "Their house is big.", "de": "Ihr Haus ist groß."},
            {"en": "I like your idea.", "de": "Ich mag deine Idee."},
            {"en": "Our shop is open.", "de": "Unser Geschäft ist offen."},
            {"en": "Buy your ticket now!", "de": "Kaufen Sie jetzt Ihre Karte!"},
            {"en": "Her car is red.", "de": "Ihr Auto ist rot."},
            {"en": "My family is small.", "de": "Meine Familie ist klein."},
            {"en": "His job is interesting.", "de": "Sein Job ist interessant."},
            {"en": "Visit our website!", "de": "Besuchen Sie unsere Webseite!"},
            {"en": "Your order is ready.", "de": "Ihre Bestellung ist fertig."},
            {"en": "We protect your data.", "de": "Wir schützen Ihre Daten."},
            {"en": "My favorite brand is here.", "de": "Meine Lieblingsmarke ist hier."},
            {"en": "Their products are cheap.", "de": "Ihre Produkte sind günstig."},
            {"en": "Our team is the best.", "de": "Unser Team ist das beste."},
            {"en": "I take my coffee with me.", "de": "Ich nehme meinen Kaffee mit."},
            {"en": "Your opinion is important.", "de": "Deine Meinung ist wichtig."},
            {"en": "His company is new.", "de": "Seine Firma ist neu."},
            {"en": "We need your help.", "de": "Wir brauchen Ihre Hilfe."},
            {"en": "My answer is clear.", "de": "Meine Antwort ist klar."},
            {"en": "Their offer is good.", "de": "Ihr Angebot ist gut."},
            {"en": "Choose your gift!", "de": "Wählen Sie Ihr Geschenk!"},
            {"en": "Our service is free.", "de": "Unser Service ist kostenlos."},
            {"en": "Your time is valuable.", "de": "Ihre Zeit ist wertvoll."},
            {"en": "I love my city.", "de": "Ich liebe meine Stadt."},
            {"en": "Discover our world!", "de": "Entdecken Sie unsere Welt!"},
        ],
    },

    ("A1", "government"): {
        "note": (
            "📖 Government and Society — A1 (consolidation)\n\n"
            "This final A1 lesson brings everything together, focusing on QUESTION WORDS "
            "(W-Fragen) and the formal Sie.\n\n"
            "W-QUESTIONS (verb in position 2)\n"
            "wer (who) · was (what) · wo (where) · wohin (where to) · woher (where from) · "
            "wann (when) · warum (why) · wie (how) · wie viel / wie viele (how much/many) · "
            "welcher/welche/welches (which).\n"
            "• Woher kommen Sie?  ·  Wo wohnen Sie?  ·  Was machen Sie beruflich?\n"
            "Yes/No questions put the verb first: Sprechen Sie Deutsch?\n"
            "The formal Sie is used with officials, on forms, and with strangers.\n\n"
            "VOCAB: der Staat, die Regierung (government), das Land, der Bürger (citizen), "
            "der Pass (passport), das Amt (office), das Formular (form), die Steuer (tax), "
            "wählen (vote/choose), wohnen, anmelden (register).\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "Where do you live?", "de": "Wo wohnen Sie?"},
            {"en": "Where do you come from?", "de": "Woher kommen Sie?"},
            {"en": "What is your name?", "de": "Wie heißen Sie?"},
            {"en": "Do you speak German?", "de": "Sprechen Sie Deutsch?"},
            {"en": "When does the office open?", "de": "Wann öffnet das Amt?"},
            {"en": "I need a passport.", "de": "Ich brauche einen Pass."},
            {"en": "Why do you need the form?", "de": "Warum brauchen Sie das Formular?"},
            {"en": "Who is the chancellor?", "de": "Wer ist der Kanzler?"},
            {"en": "How can I help you?", "de": "Wie kann ich Ihnen helfen?"},
            {"en": "Where is the office?", "de": "Wo ist das Amt?"},
            {"en": "I want to register.", "de": "Ich möchte mich anmelden."},
            {"en": "Which form do I need?", "de": "Welches Formular brauche ich?"},
            {"en": "How much does it cost?", "de": "Wie viel kostet es?"},
            {"en": "Please fill out the form.", "de": "Füllen Sie bitte das Formular aus."},
            {"en": "Where do I have to sign?", "de": "Wo muss ich unterschreiben?"},
            {"en": "Citizens pay taxes.", "de": "Bürger zahlen Steuern."},
            {"en": "When is the election?", "de": "Wann ist die Wahl?"},
            {"en": "I live in Germany.", "de": "Ich wohne in Deutschland."},
            {"en": "What do you do for a living?", "de": "Was machen Sie beruflich?"},
            {"en": "Do you have an appointment?", "de": "Haben Sie einen Termin?"},
            {"en": "The government is in Berlin.", "de": "Die Regierung ist in Berlin."},
            {"en": "How many people live here?", "de": "Wie viele Menschen wohnen hier?"},
            {"en": "Please wait here.", "de": "Warten Sie bitte hier."},
            {"en": "I have an appointment at ten.", "de": "Ich habe um zehn einen Termin."},
            {"en": "Where can I vote?", "de": "Wo kann ich wählen?"},
            {"en": "Show me your passport, please.", "de": "Zeigen Sie mir bitte Ihren Pass."},
            {"en": "The country is very big.", "de": "Das Land ist sehr groß."},
            {"en": "What time does the office close?", "de": "Wann schließt das Amt?"},
            {"en": "I don't understand the form.", "de": "Ich verstehe das Formular nicht."},
            {"en": "Can you help me, please?", "de": "Können Sie mir bitte helfen?"},
            {"en": "Every citizen can vote.", "de": "Jeder Bürger kann wählen."},
            {"en": "Where is the town hall?", "de": "Wo ist das Rathaus?"},
            {"en": "I would like to apply for a visa.", "de": "Ich möchte ein Visum beantragen."},
            {"en": "What is your address?", "de": "Wie ist Ihre Adresse?"},
            {"en": "The taxes are high.", "de": "Die Steuern sind hoch."},
            {"en": "Please come tomorrow.", "de": "Kommen Sie bitte morgen."},
            {"en": "Who is responsible?", "de": "Wer ist verantwortlich?"},
            {"en": "I have all the documents.", "de": "Ich habe alle Dokumente."},
            {"en": "Where do I have to go?", "de": "Wohin muss ich gehen?"},
            {"en": "Thank you for your help.", "de": "Danke für Ihre Hilfe."},
        ],
    },

    ("A2", "greeting"): {
        "note": (
            "📖 Greeting — A2\n\n"
            "THE PERFECT TENSE (Perfekt) — the spoken past. It has TWO parts:\n"
            "  haben (conjugated, position 2)  +  past participle (at the END)\n"
            "Regular (weak) verbs: ge + stem + t →\n"
            "  machen → gemacht · lernen → gelernt · arbeiten → gearbeitet\n"
            "Verbs in -ieren and most with be-/ver- take NO ge-:\n"
            "  studieren → studiert · besuchen → besucht\n"
            "• Ich habe Deutsch gelernt.  → I learned German.\n"
            "• Was hast du gestern gemacht?\n\n"
            "TIME WORDS: gestern (yesterday), letzte Woche, schon (already), "
            "noch nicht (not yet), gerade (just now).\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I learned German.", "de": "Ich habe Deutsch gelernt."},
            {"en": "What did you do yesterday?", "de": "Was hast du gestern gemacht?"},
            {"en": "We worked a lot.", "de": "Wir haben viel gearbeitet."},
            {"en": "She asked a question.", "de": "Sie hat eine Frage gestellt."},
            {"en": "I said hello.", "de": "Ich habe Hallo gesagt."},
            {"en": "He played football.", "de": "Er hat Fußball gespielt."},
            {"en": "Have you already had breakfast?", "de": "Hast du schon gefrühstückt?"},
            {"en": "I listened to music.", "de": "Ich habe Musik gehört."},
            {"en": "We learned a lot.", "de": "Wir haben viel gelernt."},
            {"en": "She lived in Berlin.", "de": "Sie hat in Berlin gewohnt."},
            {"en": "I bought bread.", "de": "Ich habe Brot gekauft."},
            {"en": "Did you work yesterday?", "de": "Hast du gestern gearbeitet?"},
            {"en": "He cooked dinner.", "de": "Er hat das Abendessen gekocht."},
            {"en": "They danced all night.", "de": "Sie haben die ganze Nacht getanzt."},
            {"en": "I made tea.", "de": "Ich habe Tee gemacht."},
            {"en": "She studied medicine.", "de": "Sie hat Medizin studiert."},
            {"en": "We visited a museum.", "de": "Wir haben ein Museum besucht."},
            {"en": "I already paid.", "de": "Ich habe schon bezahlt."},
            {"en": "He answered the email.", "de": "Er hat die E-Mail beantwortet."},
            {"en": "Did you hear that?", "de": "Hast du das gehört?"},
            {"en": "I waited an hour.", "de": "Ich habe eine Stunde gewartet."},
            {"en": "We celebrated her birthday.", "de": "Wir haben ihren Geburtstag gefeiert."},
            {"en": "She greeted the guests.", "de": "Sie hat die Gäste begrüßt."},
            {"en": "I learned the words.", "de": "Ich habe die Wörter gelernt."},
            {"en": "He showed me the photos.", "de": "Er hat mir die Fotos gezeigt."},
            {"en": "We talked for hours.", "de": "Wir haben stundenlang geredet."},
            {"en": "I cooked yesterday.", "de": "Ich habe gestern gekocht."},
            {"en": "Did she say something?", "de": "Hat sie etwas gesagt?"},
            {"en": "They lived here for ten years.", "de": "Sie haben zehn Jahre hier gewohnt."},
            {"en": "I have not paid yet.", "de": "Ich habe noch nicht bezahlt."},
            {"en": "We laughed a lot.", "de": "Wir haben viel gelacht."},
            {"en": "He worked at a bank.", "de": "Er hat bei einer Bank gearbeitet."},
            {"en": "I packed my bag.", "de": "Ich habe meine Tasche gepackt."},
            {"en": "She practiced the piano.", "de": "Sie hat Klavier geübt."},
            {"en": "Did you buy the tickets?", "de": "Hast du die Karten gekauft?"},
            {"en": "I just made a coffee.", "de": "Ich habe gerade einen Kaffee gemacht."},
            {"en": "They thanked me.", "de": "Sie haben mir gedankt."},
            {"en": "I learned a new word today.", "de": "Ich habe heute ein neues Wort gelernt."},
            {"en": "He greeted me kindly.", "de": "Er hat mich freundlich begrüßt."},
            {"en": "We have learned so much.", "de": "Wir haben so viel gelernt."},
        ],
    },

    ("A2", "holiday"): {
        "note": (
            "📖 Holiday — A2\n\n"
            "PERFECT TENSE with sein\n"
            "Some verbs use sein (not haben) in the Perfekt. Mostly:\n"
            "• MOTION (A → B): gehen → gegangen, fahren → gefahren, fliegen → geflogen, "
            "kommen → gekommen, reisen → gereist\n"
            "• CHANGE OF STATE: aufstehen → aufgestanden, einschlafen → eingeschlafen\n"
            "• sein → gewesen, bleiben → geblieben, werden → geworden\n"
            "Structure: sein (position 2) + participle (END).\n"
            "• Ich bin nach Italien gefahren.  → I went to Italy.\n"
            "• Wir sind am Meer geblieben.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I went to Italy.", "de": "Ich bin nach Italien gefahren."},
            {"en": "We flew to Spain.", "de": "Wir sind nach Spanien geflogen."},
            {"en": "She went home.", "de": "Sie ist nach Hause gegangen."},
            {"en": "They stayed at the sea.", "de": "Sie sind am Meer geblieben."},
            {"en": "I traveled a lot.", "de": "Ich bin viel gereist."},
            {"en": "He came late.", "de": "Er ist spät gekommen."},
            {"en": "We drove to the mountains.", "de": "Wir sind in die Berge gefahren."},
            {"en": "I got up early.", "de": "Ich bin früh aufgestanden."},
            {"en": "The holiday was great.", "de": "Der Urlaub ist toll gewesen."},
            {"en": "She flew to Berlin yesterday.", "de": "Sie ist gestern nach Berlin geflogen."},
            {"en": "We went to the beach.", "de": "Wir sind an den Strand gegangen."},
            {"en": "I stayed at home.", "de": "Ich bin zu Hause geblieben."},
            {"en": "They traveled through Europe.", "de": "Sie sind durch Europa gereist."},
            {"en": "He went swimming.", "de": "Er ist schwimmen gegangen."},
            {"en": "We came back on Sunday.", "de": "Wir sind am Sonntag zurückgekommen."},
            {"en": "I fell asleep on the train.", "de": "Ich bin im Zug eingeschlafen."},
            {"en": "She went on holiday.", "de": "Sie ist in den Urlaub gefahren."},
            {"en": "The flight was long.", "de": "Der Flug ist lang gewesen."},
            {"en": "We walked to the hotel.", "de": "Wir sind zum Hotel gegangen."},
            {"en": "I have never been to Paris.", "de": "Ich bin noch nie in Paris gewesen."},
            {"en": "He drove to the airport.", "de": "Er ist zum Flughafen gefahren."},
            {"en": "They flew home.", "de": "Sie sind nach Hause geflogen."},
            {"en": "We arrived in the evening.", "de": "Wir sind am Abend angekommen."},
            {"en": "I went out yesterday.", "de": "Ich bin gestern ausgegangen."},
            {"en": "She stayed one week.", "de": "Sie ist eine Woche geblieben."},
            {"en": "The children ran to the sea.", "de": "Die Kinder sind ans Meer gelaufen."},
            {"en": "We traveled by train.", "de": "Wir sind mit dem Zug gefahren."},
            {"en": "He has gone already.", "de": "Er ist schon gegangen."},
            {"en": "I flew for the first time.", "de": "Ich bin zum ersten Mal geflogen."},
            {"en": "We went into the city.", "de": "Wir sind in die Stadt gegangen."},
            {"en": "She came to the party.", "de": "Sie ist zur Party gekommen."},
            {"en": "They drove home late.", "de": "Sie sind spät nach Hause gefahren."},
            {"en": "I have been to Greece.", "de": "Ich bin in Griechenland gewesen."},
            {"en": "We got up at six.", "de": "Wir sind um sechs aufgestanden."},
            {"en": "He traveled alone.", "de": "Er ist allein gereist."},
            {"en": "The bus arrived on time.", "de": "Der Bus ist pünktlich angekommen."},
            {"en": "We stayed in a hotel.", "de": "Wir sind in einem Hotel geblieben."},
            {"en": "She flew to New York.", "de": "Sie ist nach New York geflogen."},
            {"en": "I came back yesterday.", "de": "Ich bin gestern zurückgekommen."},
            {"en": "The holiday went by quickly.", "de": "Der Urlaub ist schnell vergangen."},
        ],
    },

    ("A2", "relationship"): {
        "note": (
            "📖 Relationship — A2\n\n"
            "THE DATIVE OBJECT (Dativ) — usually the person who receives something.\n"
            "Articles: der→dem, das→dem, die→der, plural→den (+n).\n"
            "Pronouns: ich→mir, du→dir, er→ihm, sie→ihr, wir→uns, ihr→euch, sie→ihnen, Sie→Ihnen.\n"
            "• Ich gebe meinem Bruder ein Buch.  ·  Kannst du mir helfen?\n\n"
            "DATIVE VERBS (take a dative object):\n"
            "helfen, danken, gefallen (to please), gehören (belong to), gratulieren, "
            "antworten, glauben, vertrauen.\n"
            "• Das Geschenk gefällt mir.  ·  Das Auto gehört meinem Vater.\n"
            "Word order: subject – verb – DATIVE – ACCUSATIVE.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "Can you help me?", "de": "Kannst du mir helfen?"},
            {"en": "I help my friend.", "de": "Ich helfe meinem Freund."},
            {"en": "The present pleases me.", "de": "Das Geschenk gefällt mir."},
            {"en": "The car belongs to my father.", "de": "Das Auto gehört meinem Vater."},
            {"en": "I give my brother a book.", "de": "Ich gebe meinem Bruder ein Buch."},
            {"en": "She thanks her teacher.", "de": "Sie dankt ihrer Lehrerin."},
            {"en": "I believe you.", "de": "Ich glaube dir."},
            {"en": "He gives her flowers.", "de": "Er gibt ihr Blumen."},
            {"en": "Can you answer me?", "de": "Kannst du mir antworten?"},
            {"en": "The book belongs to him.", "de": "Das Buch gehört ihm."},
            {"en": "I congratulate you.", "de": "Ich gratuliere dir."},
            {"en": "The city pleases us.", "de": "Die Stadt gefällt uns."},
            {"en": "I show my friend the photos.", "de": "Ich zeige meinem Freund die Fotos."},
            {"en": "She helps her mother.", "de": "Sie hilft ihrer Mutter."},
            {"en": "We thank you.", "de": "Wir danken euch."},
            {"en": "The jacket belongs to me.", "de": "Die Jacke gehört mir."},
            {"en": "He tells me a story.", "de": "Er erzählt mir eine Geschichte."},
            {"en": "I give my sister a gift.", "de": "Ich gebe meiner Schwester ein Geschenk."},
            {"en": "Does the film please you?", "de": "Gefällt dir der Film?"},
            {"en": "I write him a letter.", "de": "Ich schreibe ihm einen Brief."},
            {"en": "She helps the children.", "de": "Sie hilft den Kindern."},
            {"en": "The house belongs to my parents.", "de": "Das Haus gehört meinen Eltern."},
            {"en": "Can I help you?", "de": "Kann ich Ihnen helfen?"},
            {"en": "He gives the dog food.", "de": "Er gibt dem Hund Futter."},
            {"en": "I thank my friends.", "de": "Ich danke meinen Freunden."},
            {"en": "The idea pleases me.", "de": "Die Idee gefällt mir."},
            {"en": "She answers her boss.", "de": "Sie antwortet ihrem Chef."},
            {"en": "We give the guests coffee.", "de": "Wir geben den Gästen Kaffee."},
            {"en": "I believe my sister.", "de": "Ich glaube meiner Schwester."},
            {"en": "The colour suits you.", "de": "Die Farbe steht dir."},
            {"en": "He brings me a coffee.", "de": "Er bringt mir einen Kaffee."},
            {"en": "I trust you.", "de": "Ich vertraue dir."},
            {"en": "The shoes belong to her.", "de": "Die Schuhe gehören ihr."},
            {"en": "She gives her son money.", "de": "Sie gibt ihrem Sohn Geld."},
            {"en": "Can you lend me the book?", "de": "Kannst du mir das Buch leihen?"},
            {"en": "We congratulate the couple.", "de": "Wir gratulieren dem Paar."},
            {"en": "The food pleases the children.", "de": "Das Essen gefällt den Kindern."},
            {"en": "I send my grandmother a card.", "de": "Ich schicke meiner Großmutter eine Karte."},
            {"en": "He helps me every day.", "de": "Er hilft mir jeden Tag."},
            {"en": "Family is important to me.", "de": "Familie ist mir wichtig."},
        ],
    },

    ("A2", "technology"): {
        "note": (
            "📖 Technology — A2\n\n"
            "PERFECT with STRONG (irregular) verbs\n"
            "Strong verbs form the participle with ge- … -en, often with a vowel change. "
            "Learn them as a set:\n"
            "  schreiben → geschrieben · lesen → gelesen · sehen → gesehen · "
            "sprechen → gesprochen · nehmen → genommen · finden → gefunden · "
            "geben → gegeben · halten → gehalten\n"
            "No ge- with be-/ver-: bekommen → bekommen · verstehen → verstanden.\n"
            "Most take haben.\n"
            "• Ich habe eine E-Mail geschrieben.  ·  Hast du die Nachricht gelesen?\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I wrote an email.", "de": "Ich habe eine E-Mail geschrieben."},
            {"en": "Have you read the message?", "de": "Hast du die Nachricht gelesen?"},
            {"en": "I saw the video.", "de": "Ich habe das Video gesehen."},
            {"en": "We spoke on the phone.", "de": "Wir haben am Telefon gesprochen."},
            {"en": "He found the file.", "de": "Er hat die Datei gefunden."},
            {"en": "I took the phone.", "de": "Ich habe das Handy genommen."},
            {"en": "She got a new laptop.", "de": "Sie hat einen neuen Laptop bekommen."},
            {"en": "I did not understand the question.", "de": "Ich habe die Frage nicht verstanden."},
            {"en": "We watched a film.", "de": "Wir haben einen Film gesehen."},
            {"en": "He wrote a program.", "de": "Er hat ein Programm geschrieben."},
            {"en": "I read the news online.", "de": "Ich habe die Nachrichten online gelesen."},
            {"en": "Have you seen my message?", "de": "Hast du meine Nachricht gesehen?"},
            {"en": "She gave me her number.", "de": "Sie hat mir ihre Nummer gegeben."},
            {"en": "We found a good app.", "de": "Wir haben eine gute App gefunden."},
            {"en": "I spoke with the technician.", "de": "Ich habe mit dem Techniker gesprochen."},
            {"en": "He took my charger.", "de": "Er hat mein Ladegerät genommen."},
            {"en": "I have already read the email.", "de": "Ich habe die E-Mail schon gelesen."},
            {"en": "They understood the problem.", "de": "Sie haben das Problem verstanden."},
            {"en": "She wrote a long text.", "de": "Sie hat einen langen Text geschrieben."},
            {"en": "I saw your photos.", "de": "Ich habe deine Fotos gesehen."},
            {"en": "We received the file.", "de": "Wir haben die Datei bekommen."},
            {"en": "He read the instructions.", "de": "Er hat die Anleitung gelesen."},
            {"en": "I gave him my password.", "de": "Ich habe ihm mein Passwort gegeben."},
            {"en": "Have you spoken to her?", "de": "Hast du mit ihr gesprochen?"},
            {"en": "She found the mistake.", "de": "Sie hat den Fehler gefunden."},
            {"en": "I have not seen the film.", "de": "Ich habe den Film nicht gesehen."},
            {"en": "We wrote the report together.", "de": "Wir haben den Bericht zusammen geschrieben."},
            {"en": "He read a lot.", "de": "Er hat viel gelesen."},
            {"en": "I understood you well.", "de": "Ich habe dich gut verstanden."},
            {"en": "She gave a presentation.", "de": "Sie hat eine Präsentation gehalten."},
            {"en": "We saw each other yesterday.", "de": "Wir haben uns gestern gesehen."},
            {"en": "I read your message twice.", "de": "Ich habe deine Nachricht zweimal gelesen."},
            {"en": "He got an answer.", "de": "Er hat eine Antwort bekommen."},
            {"en": "They spoke about the project.", "de": "Sie haben über das Projekt gesprochen."},
            {"en": "I found your email.", "de": "Ich habe deine E-Mail gefunden."},
            {"en": "She wrote to me.", "de": "Sie hat mir geschrieben."},
            {"en": "We understood the lesson.", "de": "Wir haben die Lektion verstanden."},
            {"en": "He has seen this before.", "de": "Er hat das schon einmal gesehen."},
            {"en": "I gave her the laptop.", "de": "Ich habe ihr den Laptop gegeben."},
            {"en": "Technology has changed our lives.", "de": "Die Technik hat unser Leben verändert."},
        ],
    },

    ("A2", "sports"): {
        "note": (
            "📖 Sports — A2\n\n"
            "PERFECT of SEPARABLE & INSEPARABLE verbs\n"
            "SEPARABLE verbs put -ge- BETWEEN prefix and participle:\n"
            "  einkaufen → eingekauft · anrufen → angerufen · anfangen → angefangen · "
            "teilnehmen → teilgenommen · fernsehen → ferngesehen\n"
            "INSEPARABLE prefixes (be-, ver-, er-, ent-, ge-) take NO ge-:\n"
            "  besuchen → besucht · verlieren → verloren · gewinnen → gewonnen · "
            "erreichen → erreicht · beginnen → begonnen\n"
            "• Ich habe gestern trainiert und gewonnen.\n"
            "• Wir haben am Turnier teilgenommen.\n"
            "(Motion/sein verbs still take sein: aufstehen → ist aufgestanden.)\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "We won the game.", "de": "Wir haben das Spiel gewonnen."},
            {"en": "They lost the match.", "de": "Sie haben das Spiel verloren."},
            {"en": "I trained yesterday.", "de": "Ich habe gestern trainiert."},
            {"en": "He called the trainer.", "de": "Er hat den Trainer angerufen."},
            {"en": "We took part in the tournament.", "de": "Wir haben am Turnier teilgenommen."},
            {"en": "She bought new shoes.", "de": "Sie hat neue Schuhe gekauft."},
            {"en": "I watched the game on TV.", "de": "Ich habe das Spiel im Fernsehen gesehen."},
            {"en": "The team won again.", "de": "Die Mannschaft hat wieder gewonnen."},
            {"en": "We started at six.", "de": "Wir haben um sechs angefangen."},
            {"en": "He scored two goals.", "de": "Er hat zwei Tore geschossen."},
            {"en": "I got up early for training.", "de": "Ich bin früh zum Training aufgestanden."},
            {"en": "She joined in.", "de": "Sie hat mitgemacht."},
            {"en": "We played for two hours.", "de": "Wir haben zwei Stunden gespielt."},
            {"en": "He won the race.", "de": "Er hat das Rennen gewonnen."},
            {"en": "The match started late.", "de": "Das Spiel hat spät angefangen."},
            {"en": "I forgot my sports bag.", "de": "Ich habe meine Sporttasche vergessen."},
            {"en": "We met at the stadium.", "de": "Wir haben uns am Stadion getroffen."},
            {"en": "She called me after the game.", "de": "Sie hat mich nach dem Spiel angerufen."},
            {"en": "They reached the final.", "de": "Sie haben das Finale erreicht."},
            {"en": "I took part too.", "de": "Ich habe auch mitgemacht."},
            {"en": "He lost his keys.", "de": "Er hat seine Schlüssel verloren."},
            {"en": "We watched TV after sport.", "de": "Wir haben nach dem Sport ferngesehen."},
            {"en": "The coach explained the rules.", "de": "Der Trainer hat die Regeln erklärt."},
            {"en": "I signed up for the course.", "de": "Ich habe mich für den Kurs angemeldet."},
            {"en": "She won a medal.", "de": "Sie hat eine Medaille gewonnen."},
            {"en": "We invited the other team.", "de": "Wir haben das andere Team eingeladen."},
            {"en": "He prepared everything.", "de": "Er hat alles vorbereitet."},
            {"en": "I bought a ticket for the game.", "de": "Ich habe eine Karte für das Spiel gekauft."},
            {"en": "They started the season well.", "de": "Sie haben die Saison gut begonnen."},
            {"en": "We lost in the end.", "de": "Wir haben am Ende verloren."},
            {"en": "She has already left.", "de": "Sie ist schon weggegangen."},
            {"en": "He picked me up.", "de": "Er hat mich abgeholt."},
            {"en": "I called the doctor after the injury.", "de": "Ich habe nach der Verletzung den Arzt angerufen."},
            {"en": "We celebrated the victory.", "de": "Wir haben den Sieg gefeiert."},
            {"en": "The game has finished.", "de": "Das Spiel ist zu Ende gegangen."},
            {"en": "He missed the training.", "de": "Er hat das Training verpasst."},
            {"en": "I have understood the rules.", "de": "Ich habe die Regeln verstanden."},
            {"en": "They booked the field.", "de": "Sie haben den Platz reserviert."},
            {"en": "She has come back.", "de": "Sie ist zurückgekommen."},
            {"en": "We have won the championship.", "de": "Wir haben die Meisterschaft gewonnen."},
        ],
    },

    ("A2", "food"): {
        "note": (
            "📖 Food — A2\n\n"
            "COMPARATIVE & SUPERLATIVE\n"
            "Comparative: adjective + -er … als (than)\n"
            "  billig → billiger · schnell → schneller →  Pizza ist billiger als Sushi.\n"
            "Superlative (predicative): am + adjective + -sten\n"
            "  Das ist am billigsten.  ·  Kaffee schmeckt am besten.\n"
            "Short adjectives often add an umlaut:\n"
            "  alt → älter, groß → größer, jung → jünger, gesund → gesünder\n"
            "IRREGULAR (learn them!):\n"
            "  gut → besser → am besten · viel → mehr → am meisten · "
            "gern → lieber → am liebsten\n"
            "• Ich esse lieber Fisch als Fleisch.  ·  Schokolade mag ich am liebsten.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "Pizza is cheaper than sushi.", "de": "Pizza ist billiger als Sushi."},
            {"en": "Tea is healthier than cola.", "de": "Tee ist gesünder als Cola."},
            {"en": "I like fish more than meat.", "de": "Ich mag Fisch lieber als Fleisch."},
            {"en": "Coffee tastes best.", "de": "Kaffee schmeckt am besten."},
            {"en": "This restaurant is more expensive.", "de": "Dieses Restaurant ist teurer."},
            {"en": "Apples are cheaper than mangoes.", "de": "Äpfel sind billiger als Mangos."},
            {"en": "She eats more than me.", "de": "Sie isst mehr als ich."},
            {"en": "Water is the healthiest.", "de": "Wasser ist am gesündesten."},
            {"en": "The soup is hotter than the tea.", "de": "Die Suppe ist heißer als der Tee."},
            {"en": "I prefer to drink tea.", "de": "Ich trinke lieber Tee."},
            {"en": "This cake is the best.", "de": "Dieser Kuchen ist am besten."},
            {"en": "Vegetables are healthier than chips.", "de": "Gemüse ist gesünder als Chips."},
            {"en": "He eats the most.", "de": "Er isst am meisten."},
            {"en": "Bread is cheaper here.", "de": "Brot ist hier billiger."},
            {"en": "I like chocolate the most.", "de": "Ich mag Schokolade am liebsten."},
            {"en": "The fish is fresher than the meat.", "de": "Der Fisch ist frischer als das Fleisch."},
            {"en": "This wine is better.", "de": "Dieser Wein ist besser."},
            {"en": "Lemons are more sour than oranges.", "de": "Zitronen sind saurer als Orangen."},
            {"en": "The pizza is bigger than the salad.", "de": "Die Pizza ist größer als der Salat."},
            {"en": "I eat fruit more often now.", "de": "Ich esse jetzt öfter Obst."},
            {"en": "Cooking at home is cheaper.", "de": "Zu Hause kochen ist billiger."},
            {"en": "This is the most delicious meal.", "de": "Das ist das leckerste Essen."},
            {"en": "Honey is sweeter than sugar.", "de": "Honig ist süßer als Zucker."},
            {"en": "She drinks more coffee than I do.", "de": "Sie trinkt mehr Kaffee als ich."},
            {"en": "The new café is better.", "de": "Das neue Café ist besser."},
            {"en": "I prefer cooking myself.", "de": "Ich koche lieber selbst."},
            {"en": "This dish is spicier.", "de": "Dieses Gericht ist schärfer."},
            {"en": "Milk is healthier than soda.", "de": "Milch ist gesünder als Limonade."},
            {"en": "That was the best dinner.", "de": "Das war das beste Abendessen."},
            {"en": "Rice is cheaper than potatoes.", "de": "Reis ist billiger als Kartoffeln."},
            {"en": "He likes tea less than coffee.", "de": "Er mag Tee weniger als Kaffee."},
            {"en": "The market is cheaper than the supermarket.", "de": "Der Markt ist billiger als der Supermarkt."},
            {"en": "Fresh food tastes better.", "de": "Frisches Essen schmeckt besser."},
            {"en": "This is my favorite dish.", "de": "Das ist mein Lieblingsgericht."},
            {"en": "The portion is bigger here.", "de": "Die Portion ist hier größer."},
            {"en": "I eat less sugar now.", "de": "Ich esse jetzt weniger Zucker."},
            {"en": "Strawberries are sweeter than lemons.", "de": "Erdbeeren sind süßer als Zitronen."},
            {"en": "The breakfast was the best.", "de": "Das Frühstück war am besten."},
            {"en": "I like vegetables more and more.", "de": "Ich mag Gemüse immer mehr."},
            {"en": "Good food makes life better.", "de": "Gutes Essen macht das Leben besser."},
        ],
    },

    ("A2", "education"): {
        "note": (
            "📖 Education — A2\n\n"
            "SUBORDINATE CLAUSES with weil (because)\n"
            "weil gives a reason. In the weil-clause the conjugated verb goes to the VERY END.\n"
            "  Main clause , weil + … + VERB.\n"
            "• Ich lerne Deutsch, weil ich in Berlin wohne.  (wohne → end)\n"
            "• Sie ist müde, weil sie viel gearbeitet hat.  (hat → end, after the participle)\n"
            "A comma always separates the two clauses.\n\n"
            "Compare denn (same meaning, NORMAL order):\n"
            "  Ich lerne Deutsch, denn ich wohne in Berlin.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I learn German because I live in Berlin.", "de": "Ich lerne Deutsch, weil ich in Berlin wohne."},
            {"en": "She is tired because she worked a lot.", "de": "Sie ist müde, weil sie viel gearbeitet hat."},
            {"en": "I study because I want a good job.", "de": "Ich lerne, weil ich einen guten Job will."},
            {"en": "He is happy because he passed the exam.", "de": "Er ist glücklich, weil er die Prüfung bestanden hat."},
            {"en": "We stay home because it is raining.", "de": "Wir bleiben zu Hause, weil es regnet."},
            {"en": "I am learning because I have an exam.", "de": "Ich lerne, weil ich eine Prüfung habe."},
            {"en": "She cannot come because she is sick.", "de": "Sie kann nicht kommen, weil sie krank ist."},
            {"en": "I like the course because the teacher is good.", "de": "Ich mag den Kurs, weil der Lehrer gut ist."},
            {"en": "He reads a lot because he loves books.", "de": "Er liest viel, weil er Bücher liebt."},
            {"en": "We are late because the bus did not come.", "de": "Wir sind spät, weil der Bus nicht gekommen ist."},
            {"en": "I drink coffee because I am tired.", "de": "Ich trinke Kaffee, weil ich müde bin."},
            {"en": "She studies medicine because she wants to help people.", "de": "Sie studiert Medizin, weil sie Menschen helfen will."},
            {"en": "I cannot answer because I do not understand the question.", "de": "Ich kann nicht antworten, weil ich die Frage nicht verstehe."},
            {"en": "He learns English because he needs it for work.", "de": "Er lernt Englisch, weil er es für die Arbeit braucht."},
            {"en": "We are happy because the holidays start.", "de": "Wir sind glücklich, weil die Ferien beginnen."},
            {"en": "I take the bus because my car is broken.", "de": "Ich nehme den Bus, weil mein Auto kaputt ist."},
            {"en": "She is nervous because she has a test.", "de": "Sie ist nervös, weil sie einen Test hat."},
            {"en": "I stay because I want to learn more.", "de": "Ich bleibe, weil ich mehr lernen will."},
            {"en": "He is proud because he did well.", "de": "Er ist stolz, weil er es gut gemacht hat."},
            {"en": "We practice because we want to improve.", "de": "Wir üben, weil wir besser werden wollen."},
            {"en": "I am hungry because I did not eat.", "de": "Ich habe Hunger, weil ich nicht gegessen habe."},
            {"en": "She is at home because she is ill.", "de": "Sie ist zu Hause, weil sie krank ist."},
            {"en": "I read the book because it is interesting.", "de": "Ich lese das Buch, weil es interessant ist."},
            {"en": "He works hard because he needs money.", "de": "Er arbeitet viel, weil er Geld braucht."},
            {"en": "We are quiet because the baby is sleeping.", "de": "Wir sind leise, weil das Baby schläft."},
            {"en": "I ask the teacher because I have a question.", "de": "Ich frage den Lehrer, weil ich eine Frage habe."},
            {"en": "She is happy because she got good grades.", "de": "Sie ist glücklich, weil sie gute Noten bekommen hat."},
            {"en": "I learn the words because I want to remember them.", "de": "Ich lerne die Wörter, weil ich sie behalten will."},
            {"en": "He is tired because he got up early.", "de": "Er ist müde, weil er früh aufgestanden ist."},
            {"en": "We cancel the trip because the weather is bad.", "de": "Wir sagen die Reise ab, weil das Wetter schlecht ist."},
            {"en": "I am glad because you came.", "de": "Ich bin froh, weil du gekommen bist."},
            {"en": "She writes notes because she wants to learn.", "de": "Sie schreibt Notizen, weil sie lernen will."},
            {"en": "I do not go out because I have to study.", "de": "Ich gehe nicht aus, weil ich lernen muss."},
            {"en": "He is late because he missed the train.", "de": "Er ist spät, weil er den Zug verpasst hat."},
            {"en": "We like the school because it is modern.", "de": "Wir mögen die Schule, weil sie modern ist."},
            {"en": "I am tired because I studied all night.", "de": "Ich bin müde, weil ich die ganze Nacht gelernt habe."},
            {"en": "She helps me because I am her friend.", "de": "Sie hilft mir, weil ich ihr Freund bin."},
            {"en": "I close the window because it is cold.", "de": "Ich mache das Fenster zu, weil es kalt ist."},
            {"en": "He smiles because he is happy.", "de": "Er lächelt, weil er glücklich ist."},
            {"en": "Learning is important because it opens doors.", "de": "Lernen ist wichtig, weil es Türen öffnet."},
        ],
    },

    ("A2", "work"): {
        "note": (
            "📖 Work — A2\n\n"
            "SUBORDINATE CLAUSES with dass (that)\n"
            "dass introduces a reported fact or opinion. Like weil, the conjugated verb "
            "goes to the END, after a comma.\n"
            "• Ich glaube, dass der Job interessant ist.\n"
            "• Er sagt, dass er morgen arbeiten muss.  (muss → last)\n"
            "• Ich weiß, dass du viel gearbeitet hast.  (hast → last)\n\n"
            "Common starters: Ich glaube/denke/weiß/hoffe, dass … · "
            "Es ist gut/wichtig, dass …\n"
            "• Es ist wichtig, dass du pünktlich bist.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I think that the job is interesting.", "de": "Ich glaube, dass der Job interessant ist."},
            {"en": "He says that he has to work tomorrow.", "de": "Er sagt, dass er morgen arbeiten muss."},
            {"en": "I know that you worked a lot.", "de": "Ich weiß, dass du viel gearbeitet hast."},
            {"en": "It is important that you are on time.", "de": "Es ist wichtig, dass du pünktlich bist."},
            {"en": "I hope that the meeting is short.", "de": "Ich hoffe, dass das Meeting kurz ist."},
            {"en": "She thinks that the boss is nice.", "de": "Sie denkt, dass der Chef nett ist."},
            {"en": "I believe that he is right.", "de": "Ich glaube, dass er recht hat."},
            {"en": "We know that the work is hard.", "de": "Wir wissen, dass die Arbeit schwer ist."},
            {"en": "He hopes that he gets the job.", "de": "Er hofft, dass er den Job bekommt."},
            {"en": "It is good that you are here.", "de": "Es ist gut, dass du hier bist."},
            {"en": "I think that she is a good colleague.", "de": "Ich glaube, dass sie eine gute Kollegin ist."},
            {"en": "She says that the office is closed.", "de": "Sie sagt, dass das Büro geschlossen ist."},
            {"en": "I know that you can do it.", "de": "Ich weiß, dass du es kannst."},
            {"en": "He believes that the project is important.", "de": "Er glaubt, dass das Projekt wichtig ist."},
            {"en": "It is true that the salary is good.", "de": "Es ist wahr, dass das Gehalt gut ist."},
            {"en": "I hope that we finish early.", "de": "Ich hoffe, dass wir früh fertig sind."},
            {"en": "She thinks that the work is interesting.", "de": "Sie denkt, dass die Arbeit interessant ist."},
            {"en": "I am sure that he comes.", "de": "Ich bin sicher, dass er kommt."},
            {"en": "We hope that the customer is happy.", "de": "Wir hoffen, dass der Kunde zufrieden ist."},
            {"en": "He says that he likes his job.", "de": "Er sagt, dass er seinen Job mag."},
            {"en": "I think that we need more time.", "de": "Ich glaube, dass wir mehr Zeit brauchen."},
            {"en": "It is clear that she works hard.", "de": "Es ist klar, dass sie viel arbeitet."},
            {"en": "I know that the meeting starts at ten.", "de": "Ich weiß, dass das Meeting um zehn beginnt."},
            {"en": "She hopes that she can stay.", "de": "Sie hofft, dass sie bleiben kann."},
            {"en": "I believe that the plan works.", "de": "Ich glaube, dass der Plan funktioniert."},
            {"en": "He says that he is tired.", "de": "Er sagt, dass er müde ist."},
            {"en": "It is good that you asked.", "de": "Es ist gut, dass du gefragt hast."},
            {"en": "I think that the idea is great.", "de": "Ich glaube, dass die Idee toll ist."},
            {"en": "We know that the deadline is tomorrow.", "de": "Wir wissen, dass die Frist morgen ist."},
            {"en": "She says that she helps.", "de": "Sie sagt, dass sie hilft."},
            {"en": "I hope that everything is okay.", "de": "Ich hoffe, dass alles in Ordnung ist."},
            {"en": "He thinks that the price is too high.", "de": "Er denkt, dass der Preis zu hoch ist."},
            {"en": "I am glad that you came.", "de": "Ich bin froh, dass du gekommen bist."},
            {"en": "It is possible that he is late.", "de": "Es ist möglich, dass er zu spät kommt."},
            {"en": "She knows that I am busy.", "de": "Sie weiß, dass ich beschäftigt bin."},
            {"en": "I think that we start now.", "de": "Ich glaube, dass wir jetzt anfangen."},
            {"en": "He hopes that the team wins.", "de": "Er hofft, dass das Team gewinnt."},
            {"en": "I know that you are honest.", "de": "Ich weiß, dass du ehrlich bist."},
            {"en": "It is important that we work together.", "de": "Es ist wichtig, dass wir zusammenarbeiten."},
            {"en": "I believe that hard work pays off.", "de": "Ich glaube, dass sich harte Arbeit lohnt."},
        ],
    },

    ("A2", "health"): {
        "note": (
            "📖 Health — A2\n\n"
            "REFLEXIVE VERBS (sich)\n"
            "Some verbs need a reflexive pronoun referring back to the subject.\n"
            "Akkusative pronouns: mich, dich, sich, uns, euch, sich.\n"
            "  sich fühlen: Ich fühle mich gut.\n"
            "  sich ausruhen: Er ruht sich aus.\n"
            "  sich erkälten: Ich habe mich erkältet.\n"
            "In the Perfekt the pronoun comes right after haben:\n"
            "  Ich habe mich erkältet.  ·  Sie hat sich ausgeruht.\n\n"
            "DATIVE reflexive (with another object):\n"
            "  Ich putze mir die Zähne.  ·  Ich wasche mir die Hände.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I feel good.", "de": "Ich fühle mich gut."},
            {"en": "I do not feel well.", "de": "Ich fühle mich nicht gut."},
            {"en": "He rests.", "de": "Er ruht sich aus."},
            {"en": "I caught a cold.", "de": "Ich habe mich erkältet."},
            {"en": "She feels tired.", "de": "Sie fühlt sich müde."},
            {"en": "We relax at home.", "de": "Wir entspannen uns zu Hause."},
            {"en": "How do you feel?", "de": "Wie fühlst du dich?"},
            {"en": "I have to rest.", "de": "Ich muss mich ausruhen."},
            {"en": "He feels better today.", "de": "Er fühlt sich heute besser."},
            {"en": "I brush my teeth.", "de": "Ich putze mir die Zähne."},
            {"en": "She rested all day.", "de": "Sie hat sich den ganzen Tag ausgeruht."},
            {"en": "Do you feel sick?", "de": "Fühlst du dich krank?"},
            {"en": "I am looking forward to the holiday.", "de": "Ich freue mich auf den Urlaub."},
            {"en": "We move too little.", "de": "Wir bewegen uns zu wenig."},
            {"en": "He caught a cold last week.", "de": "Er hat sich letzte Woche erkältet."},
            {"en": "I need to relax.", "de": "Ich muss mich entspannen."},
            {"en": "She feels healthy.", "de": "Sie fühlt sich gesund."},
            {"en": "I washed my hands.", "de": "Ich habe mir die Hände gewaschen."},
            {"en": "We feel comfortable here.", "de": "Wir fühlen uns hier wohl."},
            {"en": "He rests after work.", "de": "Er ruht sich nach der Arbeit aus."},
            {"en": "I feel weak.", "de": "Ich fühle mich schwach."},
            {"en": "Don't worry.", "de": "Mach dir keine Sorgen."},
            {"en": "She is glad about the news.", "de": "Sie freut sich über die Nachricht."},
            {"en": "I feel much better now.", "de": "Ich fühle mich jetzt viel besser."},
            {"en": "We should move more.", "de": "Wir sollen uns mehr bewegen."},
            {"en": "He did not feel well yesterday.", "de": "Er hat sich gestern nicht wohl gefühlt."},
            {"en": "I relax with music.", "de": "Ich entspanne mich mit Musik."},
            {"en": "Take care of yourself.", "de": "Pass auf dich auf."},
            {"en": "She feels at home here.", "de": "Sie fühlt sich hier zu Hause."},
            {"en": "I rested for an hour.", "de": "Ich habe mich eine Stunde ausgeruht."},
            {"en": "We are looking forward to the weekend.", "de": "Wir freuen uns auf das Wochenende."},
            {"en": "He feels stressed.", "de": "Er fühlt sich gestresst."},
            {"en": "I catch a cold every winter.", "de": "Ich erkälte mich jeden Winter."},
            {"en": "She takes care of her health.", "de": "Sie kümmert sich um ihre Gesundheit."},
            {"en": "I feel fit again.", "de": "Ich fühle mich wieder fit."},
            {"en": "Relax a little!", "de": "Entspann dich ein bisschen!"},
            {"en": "He hurt himself.", "de": "Er hat sich verletzt."},
            {"en": "I feel calm.", "de": "Ich fühle mich ruhig."},
            {"en": "We rested well.", "de": "Wir haben uns gut ausgeruht."},
            {"en": "If you rest, you feel better.", "de": "Wenn du dich ausruhst, fühlst du dich besser."},
        ],
    },

    ("A2", "books_films"): {
        "note": (
            "📖 Books and Films — A2\n\n"
            "SUBORDINATE CLAUSES with wenn (when / if)\n"
            "wenn introduces a condition or a repeated/future time. The verb goes to the END.\n"
            "If the wenn-clause comes FIRST, the main clause starts with its verb (verb, verb):\n"
            "• Wenn ich Zeit habe, lese ich ein Buch.\n"
            "   (habe = end of wenn-clause; lese = first word of the main clause)\n"
            "• Ich sehe einen Film, wenn ich müde bin.\n"
            "wenn = \"if\" (condition) AND \"when(ever)\" (repeated time).\n"
            "For a SINGLE past event use als instead:\n"
            "• Als ich jung war, habe ich viel gelesen.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "When I have time, I read a book.", "de": "Wenn ich Zeit habe, lese ich ein Buch."},
            {"en": "I watch a film when I am tired.", "de": "Ich sehe einen Film, wenn ich müde bin."},
            {"en": "If it rains, we stay home.", "de": "Wenn es regnet, bleiben wir zu Hause."},
            {"en": "When she is sad, she watches a comedy.", "de": "Wenn sie traurig ist, sieht sie eine Komödie."},
            {"en": "If you want, we can watch a film.", "de": "Wenn du willst, können wir einen Film sehen."},
            {"en": "When I read, I forget the time.", "de": "Wenn ich lese, vergesse ich die Zeit."},
            {"en": "I am happy when the film is good.", "de": "Ich bin glücklich, wenn der Film gut ist."},
            {"en": "If the book is boring, I stop reading.", "de": "Wenn das Buch langweilig ist, höre ich auf zu lesen."},
            {"en": "When he has money, he buys books.", "de": "Wenn er Geld hat, kauft er Bücher."},
            {"en": "We go to the cinema when there is a good film.", "de": "Wir gehen ins Kino, wenn es einen guten Film gibt."},
            {"en": "If you like the book, I lend it to you.", "de": "Wenn dir das Buch gefällt, leihe ich es dir."},
            {"en": "When I was young, I read a lot.", "de": "Als ich jung war, habe ich viel gelesen."},
            {"en": "I relax when I watch a series.", "de": "Ich entspanne mich, wenn ich eine Serie sehe."},
            {"en": "If the story is sad, I cry.", "de": "Wenn die Geschichte traurig ist, weine ich."},
            {"en": "When the children sleep, we watch a film.", "de": "Wenn die Kinder schlafen, sehen wir einen Film."},
            {"en": "I read in the evening when I am free.", "de": "Ich lese am Abend, wenn ich frei bin."},
            {"en": "If you have questions, ask me.", "de": "Wenn du Fragen hast, frag mich."},
            {"en": "When I travel, I always take a book.", "de": "Wenn ich reise, nehme ich immer ein Buch mit."},
            {"en": "We are quiet when the film starts.", "de": "Wir sind leise, wenn der Film beginnt."},
            {"en": "If the cinema is full, we go home.", "de": "Wenn das Kino voll ist, gehen wir nach Hause."},
            {"en": "When he reads, he drinks tea.", "de": "Wenn er liest, trinkt er Tee."},
            {"en": "I am bored when the film is long.", "de": "Mir ist langweilig, wenn der Film lang ist."},
            {"en": "If you finish the book, tell me.", "de": "Wenn du das Buch zu Ende liest, sag mir Bescheid."},
            {"en": "When she has time, she writes stories.", "de": "Wenn sie Zeit hat, schreibt sie Geschichten."},
            {"en": "We laugh when the film is funny.", "de": "Wir lachen, wenn der Film lustig ist."},
            {"en": "If it is cold, I read under a blanket.", "de": "Wenn es kalt ist, lese ich unter einer Decke."},
            {"en": "When I was a child, I loved cartoons.", "de": "Als ich ein Kind war, habe ich Zeichentrickfilme geliebt."},
            {"en": "I buy the book if it is cheap.", "de": "Ich kaufe das Buch, wenn es billig ist."},
            {"en": "When the season ends, I am sad.", "de": "Wenn die Staffel endet, bin ich traurig."},
            {"en": "If you come, we watch it together.", "de": "Wenn du kommst, sehen wir ihn zusammen."},
            {"en": "I read the news when I wake up.", "de": "Ich lese die Nachrichten, wenn ich aufwache."},
            {"en": "When the music plays, I relax.", "de": "Wenn die Musik spielt, entspanne ich mich."},
            {"en": "If the film is boring, we leave.", "de": "Wenn der Film langweilig ist, gehen wir."},
            {"en": "When he writes, he needs quiet.", "de": "Wenn er schreibt, braucht er Ruhe."},
            {"en": "I watch a documentary when I want to learn.", "de": "Ich sehe eine Dokumentation, wenn ich lernen will."},
            {"en": "If you press play, the film starts.", "de": "Wenn du auf Play drückst, beginnt der Film."},
            {"en": "When I finish work, I read.", "de": "Wenn ich mit der Arbeit fertig bin, lese ich."},
            {"en": "We celebrate when our team wins.", "de": "Wir feiern, wenn unser Team gewinnt."},
            {"en": "If you read every day, you learn fast.", "de": "Wenn du jeden Tag liest, lernst du schnell."},
            {"en": "When a book is good, I cannot stop.", "de": "Wenn ein Buch gut ist, kann ich nicht aufhören."},
        ],
    },

    ("A2", "accommodation"): {
        "note": (
            "📖 Accommodation — A2\n\n"
            "TWO-WAY PREPOSITIONS (Wechselpräpositionen)\n"
            "Nine prepositions take EITHER the Akkusativ OR the Dativ:\n"
            "  in, an, auf, über, unter, vor, hinter, neben, zwischen.\n"
            "• MOVEMENT / direction (wohin?) → AKKUSATIV\n"
            "  Ich gehe in die Küche.  ·  Ich stelle die Lampe auf den Tisch.\n"
            "• LOCATION (wo?) → DATIV\n"
            "  Ich bin in der Küche.  ·  Die Lampe steht auf dem Tisch.\n\n"
            "Test: change of place = Akkusativ; staying put = Dativ.\n"
            "Putting: stellen / legen / hängen (+ Akk). Being: stehen / liegen / hängen (+ Dat).\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I go into the kitchen.", "de": "Ich gehe in die Küche."},
            {"en": "I am in the kitchen.", "de": "Ich bin in der Küche."},
            {"en": "I put the lamp on the table.", "de": "Ich stelle die Lampe auf den Tisch."},
            {"en": "The lamp is on the table.", "de": "Die Lampe steht auf dem Tisch."},
            {"en": "He hangs the picture on the wall.", "de": "Er hängt das Bild an die Wand."},
            {"en": "The picture hangs on the wall.", "de": "Das Bild hängt an der Wand."},
            {"en": "I put the book on the shelf.", "de": "Ich stelle das Buch ins Regal."},
            {"en": "The book is on the shelf.", "de": "Das Buch steht im Regal."},
            {"en": "We go into the living room.", "de": "Wir gehen ins Wohnzimmer."},
            {"en": "We are in the living room.", "de": "Wir sind im Wohnzimmer."},
            {"en": "She puts the keys on the table.", "de": "Sie legt die Schlüssel auf den Tisch."},
            {"en": "The keys are on the table.", "de": "Die Schlüssel liegen auf dem Tisch."},
            {"en": "I hang the jacket behind the door.", "de": "Ich hänge die Jacke hinter die Tür."},
            {"en": "The jacket hangs behind the door.", "de": "Die Jacke hängt hinter der Tür."},
            {"en": "He goes into the bathroom.", "de": "Er geht ins Bad."},
            {"en": "He is in the bathroom.", "de": "Er ist im Bad."},
            {"en": "I put the plant in front of the window.", "de": "Ich stelle die Pflanze vor das Fenster."},
            {"en": "The plant is in front of the window.", "de": "Die Pflanze steht vor dem Fenster."},
            {"en": "We put the sofa next to the wall.", "de": "Wir stellen das Sofa neben die Wand."},
            {"en": "The sofa is next to the wall.", "de": "Das Sofa steht neben der Wand."},
            {"en": "The cat goes under the bed.", "de": "Die Katze geht unter das Bett."},
            {"en": "The cat is under the bed.", "de": "Die Katze ist unter dem Bett."},
            {"en": "I put the bag on the chair.", "de": "Ich lege die Tasche auf den Stuhl."},
            {"en": "The bag is on the chair.", "de": "Die Tasche liegt auf dem Stuhl."},
            {"en": "She goes onto the balcony.", "de": "Sie geht auf den Balkon."},
            {"en": "She is on the balcony.", "de": "Sie ist auf dem Balkon."},
            {"en": "We hang the lamp over the table.", "de": "Wir hängen die Lampe über den Tisch."},
            {"en": "The lamp hangs over the table.", "de": "Die Lampe hängt über dem Tisch."},
            {"en": "I put the shoes in front of the door.", "de": "Ich stelle die Schuhe vor die Tür."},
            {"en": "The shoes are in front of the door.", "de": "Die Schuhe stehen vor der Tür."},
            {"en": "He puts the car in the garage.", "de": "Er stellt das Auto in die Garage."},
            {"en": "The car is in the garage.", "de": "Das Auto steht in der Garage."},
            {"en": "The children run into the garden.", "de": "Die Kinder laufen in den Garten."},
            {"en": "The children are in the garden.", "de": "Die Kinder sind im Garten."},
            {"en": "I put the cup between the plates.", "de": "Ich stelle die Tasse zwischen die Teller."},
            {"en": "The cup is between the plates.", "de": "Die Tasse steht zwischen den Tellern."},
            {"en": "We move the table into the corner.", "de": "Wir stellen den Tisch in die Ecke."},
            {"en": "The table is in the corner.", "de": "Der Tisch steht in der Ecke."},
            {"en": "She hangs the mirror over the sink.", "de": "Sie hängt den Spiegel über das Waschbecken."},
            {"en": "If you put the lamp here, the room is brighter.", "de": "Wenn du die Lampe hierhin stellst, ist das Zimmer heller."},
        ],
    },

    ("A2", "clothes_fashion"): {
        "note": (
            "📖 Clothes & Fashion — A2\n\n"
            "ADJECTIVE ENDINGS after the DEFINITE article (der/die/das)\n"
            "An adjective BEFORE a noun needs an ending. After der/die/das/die(pl):\n\n"
            "             Nominative          Akkusative\n"
            "  masc.   der rote Mantel    den roten Mantel\n"
            "  fem.    die rote Jacke     die rote Jacke\n"
            "  neut.   das rote Hemd      das rote Hemd\n"
            "  plural  die roten Schuhe   die roten Schuhe\n\n"
            "Rule: -e in the singular nominative (and fem/neut Akk); "
            "-en for masculine Akkusativ and ALL plurals.\n"
            "• Der blaue Pullover ist warm.  ·  Ich nehme den blauen Pullover.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "The red jacket is beautiful.", "de": "Die rote Jacke ist schön."},
            {"en": "I take the blue pullover.", "de": "Ich nehme den blauen Pullover."},
            {"en": "The white shirt is clean.", "de": "Das weiße Hemd ist sauber."},
            {"en": "The black shoes are expensive.", "de": "Die schwarzen Schuhe sind teuer."},
            {"en": "I like the green dress.", "de": "Mir gefällt das grüne Kleid."},
            {"en": "The new coat is warm.", "de": "Der neue Mantel ist warm."},
            {"en": "I wear the black trousers.", "de": "Ich trage die schwarze Hose."},
            {"en": "The red shoes are nice.", "de": "Die roten Schuhe sind schön."},
            {"en": "She buys the yellow skirt.", "de": "Sie kauft den gelben Rock."},
            {"en": "The old jacket is too small.", "de": "Die alte Jacke ist zu klein."},
            {"en": "I want the warm pullover.", "de": "Ich möchte den warmen Pullover."},
            {"en": "The blue dress fits well.", "de": "Das blaue Kleid passt gut."},
            {"en": "The expensive shoes are comfortable.", "de": "Die teuren Schuhe sind bequem."},
            {"en": "He takes the grey coat.", "de": "Er nimmt den grauen Mantel."},
            {"en": "The pretty hat is new.", "de": "Die schöne Mütze ist neu."},
            {"en": "I like the long coat.", "de": "Mir gefällt der lange Mantel."},
            {"en": "The small shirt does not fit.", "de": "Das kleine Hemd passt nicht."},
            {"en": "She wears the red scarf.", "de": "Sie trägt den roten Schal."},
            {"en": "The cheap shoes are not good.", "de": "Die billigen Schuhe sind nicht gut."},
            {"en": "I buy the warm jacket.", "de": "Ich kaufe die warme Jacke."},
            {"en": "The white dress is elegant.", "de": "Das weiße Kleid ist elegant."},
            {"en": "He likes the dark suit.", "de": "Ihm gefällt der dunkle Anzug."},
            {"en": "I take the comfortable shoes.", "de": "Ich nehme die bequemen Schuhe."},
            {"en": "The green pullover is too big.", "de": "Der grüne Pullover ist zu groß."},
            {"en": "She buys the blue jeans.", "de": "Sie kauft die blaue Jeans."},
            {"en": "The new shoes are great.", "de": "Die neuen Schuhe sind toll."},
            {"en": "I wear the warm socks.", "de": "Ich trage die warmen Socken."},
            {"en": "The black jacket is cool.", "de": "Die schwarze Jacke ist cool."},
            {"en": "He takes the cheap shirt.", "de": "Er nimmt das billige Hemd."},
            {"en": "The red dress is my favorite.", "de": "Das rote Kleid ist mein Lieblingskleid."},
            {"en": "I like the soft pullover.", "de": "Mir gefällt der weiche Pullover."},
            {"en": "The big hat is funny.", "de": "Der große Hut ist lustig."},
            {"en": "She wears the elegant shoes.", "de": "Sie trägt die eleganten Schuhe."},
            {"en": "I want the dark trousers.", "de": "Ich möchte die dunkle Hose."},
            {"en": "The warm coat is perfect for winter.", "de": "Der warme Mantel ist perfekt für den Winter."},
            {"en": "He buys the white sneakers.", "de": "Er kauft die weißen Sneaker."},
            {"en": "The light jacket is for spring.", "de": "Die leichte Jacke ist für den Frühling."},
            {"en": "I take the long dress.", "de": "Ich nehme das lange Kleid."},
            {"en": "The new collection is beautiful.", "de": "Die neue Kollektion ist schön."},
            {"en": "If you wear the red shirt, you look great.", "de": "Wenn du das rote Hemd trägst, siehst du toll aus."},
        ],
    },

    ("A2", "personality"): {
        "note": (
            "📖 Personality — A2\n\n"
            "ADJECTIVE ENDINGS after ein / kein / mein (indefinite & possessive)\n"
            "Because ein has no ending in some forms, the adjective must show the gender. "
            "Watch the masculine nominative (-er) and neuter (-es):\n\n"
            "             Nominative              Akkusative\n"
            "  masc.   ein netter Mann        einen netten Mann\n"
            "  fem.    eine nette Frau        eine nette Frau\n"
            "  neut.   ein nettes Kind        ein nettes Kind\n"
            "  plural  meine netten Freunde   meine netten Freunde\n\n"
            "After der/die/das the article shows gender, so the ending is mostly -e; "
            "here the adjective takes over (-er / -es).\n"
            "• Er ist ein freundlicher Mensch.  ·  Ich habe einen guten Freund.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "He is a friendly man.", "de": "Er ist ein freundlicher Mann."},
            {"en": "She is a nice woman.", "de": "Sie ist eine nette Frau."},
            {"en": "It is a quiet child.", "de": "Es ist ein ruhiges Kind."},
            {"en": "I have a good friend.", "de": "Ich habe einen guten Freund."},
            {"en": "He is a funny person.", "de": "Er ist ein lustiger Mensch."},
            {"en": "She has a kind heart.", "de": "Sie hat ein gutes Herz."},
            {"en": "My best friend is honest.", "de": "Mein bester Freund ist ehrlich."},
            {"en": "He is a serious student.", "de": "Er ist ein ernster Student."},
            {"en": "I know a patient teacher.", "de": "Ich kenne einen geduldigen Lehrer."},
            {"en": "She is a hard-working colleague.", "de": "Sie ist eine fleißige Kollegin."},
            {"en": "He has a difficult character.", "de": "Er hat einen schwierigen Charakter."},
            {"en": "It is a happy family.", "de": "Es ist eine glückliche Familie."},
            {"en": "I have a polite neighbor.", "de": "Ich habe einen höflichen Nachbarn."},
            {"en": "She is an open person.", "de": "Sie ist ein offener Mensch."},
            {"en": "He is a shy boy.", "de": "Er ist ein schüchterner Junge."},
            {"en": "My old friend lives here.", "de": "Mein alter Freund wohnt hier."},
            {"en": "She has a strong personality.", "de": "Sie hat eine starke Persönlichkeit."},
            {"en": "He is a reliable man.", "de": "Er ist ein zuverlässiger Mann."},
            {"en": "I met a friendly woman.", "de": "Ich habe eine freundliche Frau getroffen."},
            {"en": "It is a curious child.", "de": "Es ist ein neugieriges Kind."},
            {"en": "He is a generous person.", "de": "Er ist ein großzügiger Mensch."},
            {"en": "She is a calm woman.", "de": "Sie ist eine ruhige Frau."},
            {"en": "I have a clever brother.", "de": "Ich habe einen klugen Bruder."},
            {"en": "He is a brave man.", "de": "Er ist ein mutiger Mann."},
            {"en": "My new colleague is nice.", "de": "Mein neuer Kollege ist nett."},
            {"en": "She is a creative student.", "de": "Sie ist eine kreative Studentin."},
            {"en": "He has a positive attitude.", "de": "Er hat eine positive Einstellung."},
            {"en": "I know an honest man.", "de": "Ich kenne einen ehrlichen Mann."},
            {"en": "It is a friendly dog.", "de": "Es ist ein freundlicher Hund."},
            {"en": "She is a strict mother.", "de": "Sie ist eine strenge Mutter."},
            {"en": "He is a lazy student.", "de": "Er ist ein fauler Student."},
            {"en": "I have a funny uncle.", "de": "Ich habe einen lustigen Onkel."},
            {"en": "She is a confident woman.", "de": "Sie ist eine selbstbewusste Frau."},
            {"en": "He is a helpful neighbor.", "de": "Er ist ein hilfsbereiter Nachbar."},
            {"en": "My little sister is shy.", "de": "Meine kleine Schwester ist schüchtern."},
            {"en": "He is a good listener.", "de": "Er ist ein guter Zuhörer."},
            {"en": "She has a warm smile.", "de": "Sie hat ein warmes Lächeln."},
            {"en": "I have a true friend.", "de": "Ich habe einen wahren Freund."},
            {"en": "He is an interesting man.", "de": "Er ist ein interessanter Mann."},
            {"en": "A good friend is a treasure.", "de": "Ein guter Freund ist ein Schatz."},
        ],
    },

    ("A2", "business"): {
        "note": (
            "📖 Business and Money — A2\n\n"
            "PREPOSITIONS that ALWAYS take the DATIV\n"
            "aus (from/out of) · bei (at/with/near) · mit (with) · nach (after/to) · "
            "seit (since/for) · von (from/of) · zu (to).\n"
            "Articles become: der/das→dem, die→der, plural→den (+n).\n"
            "Contractions: bei dem→beim, von dem→vom, zu dem→zum, zu der→zur.\n"
            "• Ich arbeite bei einer Bank.  ·  Ich fahre mit dem Bus zur Arbeit.\n"
            "• Nach der Arbeit gehe ich nach Hause.  ·  Ich kenne ihn seit einem Jahr.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I work at a bank.", "de": "Ich arbeite bei einer Bank."},
            {"en": "I go to work by bus.", "de": "Ich fahre mit dem Bus zur Arbeit."},
            {"en": "After work I go home.", "de": "Nach der Arbeit gehe ich nach Hause."},
            {"en": "I have known him for a year.", "de": "Ich kenne ihn seit einem Jahr."},
            {"en": "The money is from the bank.", "de": "Das Geld ist von der Bank."},
            {"en": "I come from Germany.", "de": "Ich komme aus Deutschland."},
            {"en": "She lives with her parents.", "de": "Sie wohnt bei ihren Eltern."},
            {"en": "We go to the meeting.", "de": "Wir gehen zum Meeting."},
            {"en": "I pay with a card.", "de": "Ich bezahle mit einer Karte."},
            {"en": "He works for a big company.", "de": "Er arbeitet bei einer großen Firma."},
            {"en": "I walk to the bank.", "de": "Ich gehe zur Bank."},
            {"en": "I get the email from my boss.", "de": "Ich bekomme die E-Mail von meinem Chef."},
            {"en": "Since Monday I have a new job.", "de": "Seit Montag habe ich einen neuen Job."},
            {"en": "I come from the office.", "de": "Ich komme aus dem Büro."},
            {"en": "After the meeting we eat.", "de": "Nach dem Meeting essen wir."},
            {"en": "I live near the company.", "de": "Ich wohne bei der Firma."},
            {"en": "He drives to the airport.", "de": "Er fährt zum Flughafen."},
            {"en": "The train comes from Berlin.", "de": "Der Zug kommt aus Berlin."},
            {"en": "I work with my colleagues.", "de": "Ich arbeite mit meinen Kollegen."},
            {"en": "She has worked here since 2020.", "de": "Sie arbeitet seit 2020 hier."},
            {"en": "We go to the bank together.", "de": "Wir gehen zusammen zur Bank."},
            {"en": "The gift is from my friend.", "de": "Das Geschenk ist von meinem Freund."},
            {"en": "After the call I write an email.", "de": "Nach dem Anruf schreibe ich eine E-Mail."},
            {"en": "I travel with my family.", "de": "Ich reise mit meiner Familie."},
            {"en": "He comes from a small town.", "de": "Er kommt aus einer kleinen Stadt."},
            {"en": "I have been waiting for an hour.", "de": "Ich warte seit einer Stunde."},
            {"en": "We drive to the customer.", "de": "Wir fahren zum Kunden."},
            {"en": "The money comes from the company.", "de": "Das Geld kommt von der Firma."},
            {"en": "She lives with a friend.", "de": "Sie wohnt bei einer Freundin."},
            {"en": "I go to the doctor after work.", "de": "Ich gehe nach der Arbeit zum Arzt."},
            {"en": "The package is from the supplier.", "de": "Das Paket ist vom Lieferanten."},
            {"en": "We pay by bank transfer.", "de": "Wir zahlen mit Überweisung."},
            {"en": "He has lived here since 2015.", "de": "Er wohnt seit 2015 hier."},
            {"en": "I take the money from the account.", "de": "Ich nehme das Geld vom Konto."},
            {"en": "After the holiday I start the new job.", "de": "Nach dem Urlaub fange ich den neuen Job an."},
            {"en": "She works with modern tools.", "de": "Sie arbeitet mit modernen Werkzeugen."},
            {"en": "I go from the office to the station.", "de": "Ich gehe vom Büro zum Bahnhof."},
            {"en": "He learns from his mistakes.", "de": "Er lernt aus seinen Fehlern."},
            {"en": "We meet at the entrance.", "de": "Wir treffen uns beim Eingang."},
            {"en": "Good business starts with trust.", "de": "Gutes Geschäft beginnt mit Vertrauen."},
        ],
    },

    ("A2", "physical_appearance"): {
        "note": (
            "📖 Physical Appearance — A2\n\n"
            "COMPARING PEOPLE (comparative & superlative)\n"
            "Comparative: -er … als (than)  ·  Superlative: am + -sten / der/die/das + -ste.\n"
            "  groß → größer → am größten · alt → älter → am ältesten · jung → jünger\n"
            "• Mein Bruder ist größer als ich.\n"
            "• Sie ist die jüngste in der Familie.\n"
            "With a noun, the comparative/superlative also takes an adjective ending:\n"
            "• Er hat die längeren Haare.  ·  Sie ist die schönste Frau.\n"
            "Equality: so … wie (as … as). Irregular: gut → besser → am besten.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "My brother is taller than me.", "de": "Mein Bruder ist größer als ich."},
            {"en": "She is younger than her sister.", "de": "Sie ist jünger als ihre Schwester."},
            {"en": "He is the oldest in the family.", "de": "Er ist der älteste in der Familie."},
            {"en": "I am smaller than you.", "de": "Ich bin kleiner als du."},
            {"en": "Her hair is longer than mine.", "de": "Ihre Haare sind länger als meine."},
            {"en": "He is the tallest in the class.", "de": "Er ist der größte in der Klasse."},
            {"en": "She is older than me.", "de": "Sie ist älter als ich."},
            {"en": "My sister is prettier than me.", "de": "Meine Schwester ist hübscher als ich."},
            {"en": "He has shorter hair now.", "de": "Er hat jetzt kürzere Haare."},
            {"en": "She is the youngest child.", "de": "Sie ist das jüngste Kind."},
            {"en": "He looks younger than his brother.", "de": "Er sieht jünger aus als sein Bruder."},
            {"en": "I am as tall as my father.", "de": "Ich bin so groß wie mein Vater."},
            {"en": "Her eyes are darker than his.", "de": "Ihre Augen sind dunkler als seine."},
            {"en": "He is the strongest man here.", "de": "Er ist der stärkste Mann hier."},
            {"en": "She is more beautiful than ever.", "de": "Sie ist schöner als je zuvor."},
            {"en": "My hair is shorter than yours.", "de": "Meine Haare sind kürzer als deine."},
            {"en": "He is taller than all his friends.", "de": "Er ist größer als alle seine Freunde."},
            {"en": "She has the longest hair.", "de": "Sie hat die längsten Haare."},
            {"en": "I am older than my cousin.", "de": "Ich bin älter als mein Cousin."},
            {"en": "He looks the best in a suit.", "de": "Er sieht im Anzug am besten aus."},
            {"en": "She is slimmer than before.", "de": "Sie ist schlanker als vorher."},
            {"en": "My grandfather is the oldest.", "de": "Mein Großvater ist der älteste."},
            {"en": "He is bigger than his father.", "de": "Er ist größer als sein Vater."},
            {"en": "She is the prettiest girl.", "de": "Sie ist das hübscheste Mädchen."},
            {"en": "I am younger than my brother.", "de": "Ich bin jünger als mein Bruder."},
            {"en": "His beard is longer now.", "de": "Sein Bart ist jetzt länger."},
            {"en": "She looks younger than me.", "de": "Sie sieht jünger aus als ich."},
            {"en": "He is the most handsome man.", "de": "Er ist der schönste Mann."},
            {"en": "My sister is taller than I thought.", "de": "Meine Schwester ist größer als ich dachte."},
            {"en": "Her smile is the most beautiful.", "de": "Ihr Lächeln ist am schönsten."},
            {"en": "He is stronger than his brother.", "de": "Er ist stärker als sein Bruder."},
            {"en": "She has darker eyes than me.", "de": "Sie hat dunklere Augen als ich."},
            {"en": "I am the smallest in my family.", "de": "Ich bin der kleinste in meiner Familie."},
            {"en": "He looks older with a beard.", "de": "Mit einem Bart sieht er älter aus."},
            {"en": "She is the most elegant woman.", "de": "Sie ist die eleganteste Frau."},
            {"en": "My hair is darker in winter.", "de": "Meine Haare sind im Winter dunkler."},
            {"en": "He is taller than average.", "de": "Er ist größer als der Durchschnitt."},
            {"en": "She is the friendliest of all.", "de": "Sie ist die freundlichste von allen."},
            {"en": "I feel younger than I am.", "de": "Ich fühle mich jünger, als ich bin."},
            {"en": "Good health makes you look younger.", "de": "Gute Gesundheit lässt dich jünger aussehen."},
        ],
    },

    ("A2", "town_city"): {
        "note": (
            "📖 Town and City — A2\n\n"
            "GETTING AROUND — movement in the past (Perfekt + sein) & two-way prepositions\n"
            "Motion verbs (gehen, fahren, laufen) use sein in the Perfekt, and movement "
            "TOWARD a place takes the AKKUSATIV:\n"
            "• Ich bin in die Stadt gefahren.  ·  Wir sind zum Markt gelaufen.\n"
            "Separable verbs put -ge- in the middle:\n"
            "• Der Zug ist um acht angekommen.  ·  Ich bin am Bahnhof ausgestiegen.\n\n"
            "Reminder: in/an/auf/vor … + AKK for direction, + DAT for location.\n"
            "• Ich bin auf den Platz gegangen. (direction)  vs.  Ich war auf dem Platz. (location)\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I drove into town.", "de": "Ich bin in die Stadt gefahren."},
            {"en": "We walked to the market.", "de": "Wir sind zum Markt gelaufen."},
            {"en": "The train arrived at eight.", "de": "Der Zug ist um acht angekommen."},
            {"en": "I got off at the station.", "de": "Ich bin am Bahnhof ausgestiegen."},
            {"en": "She went to the town hall.", "de": "Sie ist zum Rathaus gegangen."},
            {"en": "We drove to the city center.", "de": "Wir sind ins Zentrum gefahren."},
            {"en": "The bus departed late.", "de": "Der Bus ist spät abgefahren."},
            {"en": "I got on the train.", "de": "Ich bin in den Zug eingestiegen."},
            {"en": "They went into the museum.", "de": "Sie sind ins Museum gegangen."},
            {"en": "We changed at the main station.", "de": "Wir sind am Hauptbahnhof umgestiegen."},
            {"en": "He walked across the square.", "de": "Er ist über den Platz gelaufen."},
            {"en": "I came back late.", "de": "Ich bin spät zurückgekommen."},
            {"en": "We went to the park.", "de": "Wir sind in den Park gegangen."},
            {"en": "She got up and went out.", "de": "Sie ist aufgestanden und ausgegangen."},
            {"en": "The train came from Munich.", "de": "Der Zug ist aus München gekommen."},
            {"en": "I walked to the bridge.", "de": "Ich bin zur Brücke gelaufen."},
            {"en": "We drove over the bridge.", "de": "Wir sind über die Brücke gefahren."},
            {"en": "He went into the shop.", "de": "Er ist in den Laden gegangen."},
            {"en": "They arrived in the evening.", "de": "Sie sind am Abend angekommen."},
            {"en": "I got off at the next stop.", "de": "Ich bin an der nächsten Haltestelle ausgestiegen."},
            {"en": "We went home on foot.", "de": "Wir sind zu Fuß nach Hause gegangen."},
            {"en": "The bus stopped in front of the bank.", "de": "Der Bus hat vor der Bank gehalten."},
            {"en": "She went to the post office.", "de": "Sie ist zur Post gegangen."},
            {"en": "We walked through the old town.", "de": "Wir sind durch die Altstadt gelaufen."},
            {"en": "I drove to the airport.", "de": "Ich bin zum Flughafen gefahren."},
            {"en": "He came into the room.", "de": "Er ist ins Zimmer gekommen."},
            {"en": "We arrived at the hotel.", "de": "Wir sind am Hotel angekommen."},
            {"en": "They went up the stairs.", "de": "Sie sind die Treppe hochgegangen."},
            {"en": "I walked into the garden.", "de": "Ich bin in den Garten gegangen."},
            {"en": "She got out of the car.", "de": "Sie ist aus dem Auto ausgestiegen."},
            {"en": "We drove to the village.", "de": "Wir sind ins Dorf gefahren."},
            {"en": "The plane landed on time.", "de": "Das Flugzeug ist pünktlich gelandet."},
            {"en": "I went to the bus stop.", "de": "Ich bin zur Haltestelle gegangen."},
            {"en": "He ran across the street.", "de": "Er ist über die Straße gelaufen."},
            {"en": "We came back from the trip.", "de": "Wir sind von der Reise zurückgekommen."},
            {"en": "She went onto the balcony.", "de": "Sie ist auf den Balkon gegangen."},
            {"en": "I got up early and went to the market.", "de": "Ich bin früh aufgestanden und zum Markt gegangen."},
            {"en": "The train left the station.", "de": "Der Zug ist aus dem Bahnhof gefahren."},
            {"en": "We walked around the lake.", "de": "Wir sind um den See gelaufen."},
            {"en": "If you go straight ahead, you reach the church.", "de": "Wenn du geradeaus gehst, kommst du zur Kirche."},
        ],
    },

    ("A2", "music"): {
        "note": (
            "📖 Music — A2\n\n"
            "THE SIMPLE PAST of MODAL VERBS (Präteritum)\n"
            "Modals are normally used in the Präteritum (not Perfekt) for the past. "
            "They lose the umlaut and add -te:\n"
            "  können → konnte · müssen → musste · wollen → wollte · "
            "dürfen → durfte · sollen → sollte · mögen → mochte\n"
            "ich konnte, du konntest, er konnte, wir konnten, ihr konntet, sie konnten.\n"
            "The second verb stays an infinitive at the END:\n"
            "• Früher konnte ich Gitarre spielen.\n"
            "• Als Kind wollte ich Sängerin werden.\n"
            "früher = used to · als Kind = as a child.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I used to play the guitar.", "de": "Früher konnte ich Gitarre spielen."},
            {"en": "As a child I wanted to be a singer.", "de": "Als Kind wollte ich Sängerin werden."},
            {"en": "He could sing very well.", "de": "Er konnte sehr gut singen."},
            {"en": "We had to practice every day.", "de": "Wir mussten jeden Tag üben."},
            {"en": "She wanted to learn the piano.", "de": "Sie wollte Klavier lernen."},
            {"en": "I could not come to the concert.", "de": "Ich konnte nicht zum Konzert kommen."},
            {"en": "We were allowed to stay late.", "de": "Wir durften lange bleiben."},
            {"en": "He had to sell his guitar.", "de": "Er musste seine Gitarre verkaufen."},
            {"en": "I wanted to go to the concert.", "de": "Ich wollte zum Konzert gehen."},
            {"en": "She could play three instruments.", "de": "Sie konnte drei Instrumente spielen."},
            {"en": "We wanted to start a band.", "de": "Wir wollten eine Band gründen."},
            {"en": "I had to wait outside.", "de": "Ich musste draußen warten."},
            {"en": "As a child he liked rock music.", "de": "Als Kind mochte er Rockmusik."},
            {"en": "They could not find tickets.", "de": "Sie konnten keine Karten finden."},
            {"en": "We were not allowed to take photos.", "de": "Wir durften keine Fotos machen."},
            {"en": "I had to learn the lyrics.", "de": "Ich musste den Text lernen."},
            {"en": "She wanted to sing in a choir.", "de": "Sie wollte in einem Chor singen."},
            {"en": "He could dance very well.", "de": "Er konnte sehr gut tanzen."},
            {"en": "We had to be quiet during the concert.", "de": "Wir mussten beim Konzert leise sein."},
            {"en": "I wanted to buy a new guitar.", "de": "Ich wollte eine neue Gitarre kaufen."},
            {"en": "As a child I could not read music.", "de": "Als Kind konnte ich keine Noten lesen."},
            {"en": "She had to cancel the concert.", "de": "Sie musste das Konzert absagen."},
            {"en": "We were allowed to go backstage.", "de": "Wir durften hinter die Bühne gehen."},
            {"en": "He wanted to become famous.", "de": "Er wollte berühmt werden."},
            {"en": "I could hear the music from far away.", "de": "Ich konnte die Musik von weitem hören."},
            {"en": "They had to leave early.", "de": "Sie mussten früh gehen."},
            {"en": "She wanted to play in a concert.", "de": "Sie wollte in einem Konzert spielen."},
            {"en": "We could not hear the singer.", "de": "Wir konnten den Sänger nicht hören."},
            {"en": "I liked classical music as a teenager.", "de": "Als Teenager mochte ich klassische Musik."},
            {"en": "He had to repair his instrument.", "de": "Er musste sein Instrument reparieren."},
            {"en": "We wanted to dance all night.", "de": "Wir wollten die ganze Nacht tanzen."},
            {"en": "I could not afford the tickets.", "de": "Ich konnte mir die Karten nicht leisten."},
            {"en": "She had to practice for the show.", "de": "Sie musste für die Show üben."},
            {"en": "They were allowed to choose the songs.", "de": "Sie durften die Lieder aussuchen."},
            {"en": "As a child she wanted to play violin.", "de": "Als Kind wollte sie Geige spielen."},
            {"en": "We had to buy the tickets online.", "de": "Wir mussten die Karten online kaufen."},
            {"en": "He could write his own songs.", "de": "Er konnte eigene Lieder schreiben."},
            {"en": "I wanted to see my favorite band.", "de": "Ich wollte meine Lieblingsband sehen."},
            {"en": "We could not stay until the end.", "de": "Wir konnten nicht bis zum Ende bleiben."},
            {"en": "Music was always important to me.", "de": "Musik war mir immer wichtig."},
        ],
    },

    ("A2", "weather"): {
        "note": (
            "📖 Weather — A2\n\n"
            "SIMPLE PAST of sein, haben, es (Präteritum)\n"
            "For sein, haben and weather \"es\", the Präteritum is preferred:\n"
            "  sein → war (ich war, du warst, er war, wir waren …)\n"
            "  haben → hatte (ich hatte, du hattest, er hatte …)\n"
            "  es gibt → es gab · es regnet → es regnete\n"
            "• Gestern war es kalt.  ·  Wir hatten schönes Wetter.  ·  Es gab ein Gewitter.\n\n"
            "THE FUTURE with werden + infinitive (END):\n"
            "  ich werde, du wirst, er wird, wir werden, ihr werdet, sie werden\n"
            "• Morgen wird es regnen.  ·  Es wird kälter werden.\n"
            "(German often uses the present for the future too: Morgen regnet es.)\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "Yesterday it was cold.", "de": "Gestern war es kalt."},
            {"en": "We had nice weather.", "de": "Wir hatten schönes Wetter."},
            {"en": "There was a storm.", "de": "Es gab ein Gewitter."},
            {"en": "Tomorrow it will rain.", "de": "Morgen wird es regnen."},
            {"en": "It was very hot in summer.", "de": "Im Sommer war es sehr heiß."},
            {"en": "The weather was bad.", "de": "Das Wetter war schlecht."},
            {"en": "It will get colder.", "de": "Es wird kälter werden."},
            {"en": "We had a lot of snow.", "de": "Wir hatten viel Schnee."},
            {"en": "It was sunny yesterday.", "de": "Gestern war es sonnig."},
            {"en": "It will be warm tomorrow.", "de": "Morgen wird es warm sein."},
            {"en": "There was a lot of wind.", "de": "Es gab viel Wind."},
            {"en": "The sky was grey.", "de": "Der Himmel war grau."},
            {"en": "It will snow next week.", "de": "Nächste Woche wird es schneien."},
            {"en": "We had no rain for weeks.", "de": "Wir hatten wochenlang keinen Regen."},
            {"en": "It was foggy in the morning.", "de": "Am Morgen war es neblig."},
            {"en": "The summer will be hot.", "de": "Der Sommer wird heiß werden."},
            {"en": "It was ten degrees yesterday.", "de": "Gestern waren es zehn Grad."},
            {"en": "There was ice on the streets.", "de": "Es gab Eis auf den Straßen."},
            {"en": "The weather will improve.", "de": "Das Wetter wird besser werden."},
            {"en": "It rained all day.", "de": "Es regnete den ganzen Tag."},
            {"en": "We had a beautiful spring.", "de": "Wir hatten einen schönen Frühling."},
            {"en": "It will be cloudy tomorrow.", "de": "Morgen wird es bewölkt sein."},
            {"en": "The winter was very long.", "de": "Der Winter war sehr lang."},
            {"en": "There will be a thunderstorm.", "de": "Es wird ein Gewitter geben."},
            {"en": "It was warm at the beach.", "de": "Am Strand war es warm."},
            {"en": "We had storms last week.", "de": "Letzte Woche hatten wir Stürme."},
            {"en": "It will rain in the evening.", "de": "Am Abend wird es regnen."},
            {"en": "The night was cold.", "de": "Die Nacht war kalt."},
            {"en": "There was no sun today.", "de": "Heute gab es keine Sonne."},
            {"en": "The weather will stay nice.", "de": "Das Wetter wird schön bleiben."},
            {"en": "It was windy on the mountain.", "de": "Auf dem Berg war es windig."},
            {"en": "We had a mild winter.", "de": "Wir hatten einen milden Winter."},
            {"en": "Tomorrow it will be sunny.", "de": "Morgen wird es sonnig sein."},
            {"en": "The rain was very heavy.", "de": "Der Regen war sehr stark."},
            {"en": "There will be more rain.", "de": "Es wird mehr Regen geben."},
            {"en": "It was already dark at five.", "de": "Um fünf war es schon dunkel."},
            {"en": "The weather was perfect.", "de": "Das Wetter war perfekt."},
            {"en": "It will get warmer in March.", "de": "Im März wird es wärmer werden."},
            {"en": "We had wonderful weather on holiday.", "de": "Im Urlaub hatten wir wunderbares Wetter."},
            {"en": "If it rains tomorrow, we will stay home.", "de": "Wenn es morgen regnet, bleiben wir zu Hause."},
        ],
    },

    ("A2", "shopping"): {
        "note": (
            "📖 Shopping — A2\n\n"
            "INDIRECT QUESTIONS (verb to the END)\n"
            "Put a question inside a sentence to be polite or to report it. "
            "The conjugated verb moves to the END.\n"
            "• Yes/No question → use ob (whether/if):\n"
            "   Kostet das viel? → Ich weiß nicht, ob das viel kostet.\n"
            "   Können Sie mir sagen, ob es das in Blau gibt?\n"
            "• W-question → keep the question word (wo, wann, wie viel …):\n"
            "   Wo ist die Kasse? → Können Sie mir sagen, wo die Kasse ist?\n"
            "Openers: Ich weiß nicht, … · Können Sie mir sagen, … · Ich frage mich, …\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I don't know if that is expensive.", "de": "Ich weiß nicht, ob das teuer ist."},
            {"en": "Can you tell me where the checkout is?", "de": "Können Sie mir sagen, wo die Kasse ist?"},
            {"en": "I don't know if they have it in blue.", "de": "Ich weiß nicht, ob sie es in Blau haben."},
            {"en": "Can you tell me how much it costs?", "de": "Können Sie mir sagen, wie viel es kostet?"},
            {"en": "I wonder if the shop is open.", "de": "Ich frage mich, ob das Geschäft offen ist."},
            {"en": "Do you know where the shoes are?", "de": "Wissen Sie, wo die Schuhe sind?"},
            {"en": "I don't know if this is my size.", "de": "Ich weiß nicht, ob das meine Größe ist."},
            {"en": "Can you tell me when you close?", "de": "Können Sie mir sagen, wann Sie schließen?"},
            {"en": "I am not sure if it fits.", "de": "Ich bin nicht sicher, ob es passt."},
            {"en": "Do you know if it is on offer?", "de": "Wissen Sie, ob es im Angebot ist?"},
            {"en": "I don't know what I should buy.", "de": "Ich weiß nicht, was ich kaufen soll."},
            {"en": "Can you tell me where the exit is?", "de": "Können Sie mir sagen, wo der Ausgang ist?"},
            {"en": "I wonder if we have enough money.", "de": "Ich frage mich, ob wir genug Geld haben."},
            {"en": "Do you know how much the bag costs?", "de": "Wissen Sie, wie viel die Tasche kostet?"},
            {"en": "I don't know if they accept cards.", "de": "Ich weiß nicht, ob sie Karten nehmen."},
            {"en": "Can you tell me which size this is?", "de": "Können Sie mir sagen, welche Größe das ist?"},
            {"en": "I am not sure if I need it.", "de": "Ich bin nicht sicher, ob ich es brauche."},
            {"en": "Do you know when the sale starts?", "de": "Wissen Sie, wann der Schlussverkauf beginnt?"},
            {"en": "I wonder if the price is fair.", "de": "Ich frage mich, ob der Preis fair ist."},
            {"en": "Can you tell me where I can pay?", "de": "Können Sie mir sagen, wo ich bezahlen kann?"},
            {"en": "I don't know if this colour suits me.", "de": "Ich weiß nicht, ob mir diese Farbe steht."},
            {"en": "Do you know if there is a discount?", "de": "Wissen Sie, ob es einen Rabatt gibt?"},
            {"en": "I am not sure where my receipt is.", "de": "Ich bin nicht sicher, wo mein Kassenbon ist."},
            {"en": "Can you tell me how I get there?", "de": "Können Sie mir sagen, wie ich dorthin komme?"},
            {"en": "I wonder if they have my size.", "de": "Ich frage mich, ob sie meine Größe haben."},
            {"en": "I don't know if I should take it.", "de": "Ich weiß nicht, ob ich es nehmen soll."},
            {"en": "Do you know where the fitting room is?", "de": "Wissen Sie, wo die Umkleidekabine ist?"},
            {"en": "Can you tell me if this is new?", "de": "Können Sie mir sagen, ob das neu ist?"},
            {"en": "I am not sure how much I can spend.", "de": "Ich bin nicht sicher, wie viel ich ausgeben kann."},
            {"en": "I wonder why it is so expensive.", "de": "Ich frage mich, warum es so teuer ist."},
            {"en": "Do you know if the shop has a website?", "de": "Wissen Sie, ob das Geschäft eine Webseite hat?"},
            {"en": "I don't know which one is better.", "de": "Ich weiß nicht, welches besser ist."},
            {"en": "Can you tell me when it will arrive?", "de": "Können Sie mir sagen, wann es ankommt?"},
            {"en": "I wonder if I can return it.", "de": "Ich frage mich, ob ich es zurückgeben kann."},
            {"en": "Do you know how the machine works?", "de": "Wissen Sie, wie die Maschine funktioniert?"},
            {"en": "I am not sure if the size is right.", "de": "Ich bin nicht sicher, ob die Größe richtig ist."},
            {"en": "I don't know if they deliver.", "de": "Ich weiß nicht, ob sie liefern."},
            {"en": "Can you tell me where I find the offers?", "de": "Können Sie mir sagen, wo ich die Angebote finde?"},
            {"en": "I wonder whether it is worth it.", "de": "Ich frage mich, ob es sich lohnt."},
            {"en": "I want to know if the shop is still open.", "de": "Ich möchte wissen, ob das Geschäft noch offen ist."},
        ],
    },

    ("A2", "environment"): {
        "note": (
            "📖 Environment — A2\n\n"
            "THE FUTURE with werden (review) + PURPOSE with um … zu\n"
            "FUTURE: werden + infinitive (END).\n"
            "• Wir werden mehr recyceln.  ·  Die Welt wird sich verändern.\n\n"
            "PURPOSE: um … zu + infinitive = \"in order to / to\". "
            "The verb goes to the END after zu, and the subject is the SAME in both parts.\n"
            "• Wir trennen den Müll, um die Umwelt zu schützen.\n"
            "• Ich fahre Fahrrad, um Benzin zu sparen.\n"
            "With separable verbs, zu goes inside: um Gemüse anzubauen.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "We will recycle more.", "de": "Wir werden mehr recyceln."},
            {"en": "The world will change.", "de": "Die Welt wird sich verändern."},
            {"en": "We separate the rubbish to protect the environment.", "de": "Wir trennen den Müll, um die Umwelt zu schützen."},
            {"en": "I ride a bike to save petrol.", "de": "Ich fahre Fahrrad, um Benzin zu sparen."},
            {"en": "We will use less plastic.", "de": "Wir werden weniger Plastik benutzen."},
            {"en": "I turn off the light to save energy.", "de": "Ich schalte das Licht aus, um Energie zu sparen."},
            {"en": "The climate will get warmer.", "de": "Das Klima wird wärmer werden."},
            {"en": "We plant trees to help nature.", "de": "Wir pflanzen Bäume, um der Natur zu helfen."},
            {"en": "People will drive electric cars.", "de": "Die Menschen werden Elektroautos fahren."},
            {"en": "I buy local food to protect the climate.", "de": "Ich kaufe lokale Lebensmittel, um das Klima zu schützen."},
            {"en": "We will save water.", "de": "Wir werden Wasser sparen."},
            {"en": "He walks to work to stay healthy.", "de": "Er geht zu Fuß zur Arbeit, um gesund zu bleiben."},
            {"en": "We must act to save the planet.", "de": "Wir müssen handeln, um den Planeten zu retten."},
            {"en": "The air will become cleaner.", "de": "Die Luft wird sauberer werden."},
            {"en": "I use a bottle to avoid plastic.", "de": "Ich benutze eine Flasche, um Plastik zu vermeiden."},
            {"en": "We will protect the forests.", "de": "Wir werden die Wälder schützen."},
            {"en": "She recycles paper to save trees.", "de": "Sie recycelt Papier, um Bäume zu retten."},
            {"en": "The government will make new laws.", "de": "Die Regierung wird neue Gesetze machen."},
            {"en": "We drive less to reduce pollution.", "de": "Wir fahren weniger, um die Umweltverschmutzung zu reduzieren."},
            {"en": "I save energy to lower my bills.", "de": "Ich spare Energie, um meine Rechnungen zu senken."},
            {"en": "Many people will eat less meat.", "de": "Viele Menschen werden weniger Fleisch essen."},
            {"en": "We collect rubbish to clean the beach.", "de": "Wir sammeln Müll, um den Strand zu reinigen."},
            {"en": "The temperature will rise.", "de": "Die Temperatur wird steigen."},
            {"en": "I take the train to protect the environment.", "de": "Ich nehme den Zug, um die Umwelt zu schützen."},
            {"en": "We will use solar energy.", "de": "Wir werden Solarenergie nutzen."},
            {"en": "He turns off the water to save it.", "de": "Er dreht das Wasser ab, um es zu sparen."},
            {"en": "Companies will become greener.", "de": "Die Firmen werden grüner werden."},
            {"en": "We buy less to produce less waste.", "de": "Wir kaufen weniger, um weniger Müll zu produzieren."},
            {"en": "The sea level will rise.", "de": "Der Meeresspiegel wird steigen."},
            {"en": "I switch off devices to save power.", "de": "Ich schalte Geräte aus, um Strom zu sparen."},
            {"en": "We will need clean energy.", "de": "Wir werden saubere Energie brauchen."},
            {"en": "She uses public transport to save money.", "de": "Sie benutzt öffentliche Verkehrsmittel, um Geld zu sparen."},
            {"en": "We plant a garden to grow vegetables.", "de": "Wir pflanzen einen Garten, um Gemüse anzubauen."},
            {"en": "The future will be different.", "de": "Die Zukunft wird anders sein."},
            {"en": "I read about the climate to learn more.", "de": "Ich lese über das Klima, um mehr zu lernen."},
            {"en": "We will change our habits.", "de": "Wir werden unsere Gewohnheiten ändern."},
            {"en": "He saves paper to protect the forest.", "de": "Er spart Papier, um den Wald zu schützen."},
            {"en": "We work together to find solutions.", "de": "Wir arbeiten zusammen, um Lösungen zu finden."},
            {"en": "The earth will thank us.", "de": "Die Erde wird uns danken."},
            {"en": "We must start now to save the future.", "de": "Wir müssen jetzt anfangen, um die Zukunft zu retten."},
        ],
    },

    ("A2", "advertising"): {
        "note": (
            "📖 Advertising — A2\n\n"
            "SUPERLATIVE + adjective endings (selling the \"best\" of everything)\n"
            "Ads love the superlative. Before a noun it takes der/die/das + -ste (+ ending):\n"
            "  gut → der beste Preis · günstig → das günstigste Angebot · "
            "groß → die größte Auswahl\n"
            "• Wir haben die besten Produkte.  ·  Das ist das günstigste Angebot.\n"
            "Comparative before a noun also takes an ending:\n"
            "  ein besseres Produkt · ein größeres Angebot · niedrigere Preise\n"
            "Predicative superlative stays am + -sten: Unser Service ist am besten.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "We have the best products.", "de": "Wir haben die besten Produkte."},
            {"en": "This is the cheapest offer.", "de": "Das ist das günstigste Angebot."},
            {"en": "We offer the best price.", "de": "Wir bieten den besten Preis."},
            {"en": "Buy the best brand!", "de": "Kaufen Sie die beste Marke!"},
            {"en": "We have the biggest selection.", "de": "Wir haben die größte Auswahl."},
            {"en": "Our service is the best.", "de": "Unser Service ist am besten."},
            {"en": "This is a better product.", "de": "Das ist ein besseres Produkt."},
            {"en": "We have the lowest prices.", "de": "Wir haben die niedrigsten Preise."},
            {"en": "It is the most popular brand.", "de": "Es ist die beliebteste Marke."},
            {"en": "Get the newest model now!", "de": "Holen Sie sich jetzt das neueste Modell!"},
            {"en": "We give you the best quality.", "de": "Wir geben Ihnen die beste Qualität."},
            {"en": "This offer is better than the others.", "de": "Dieses Angebot ist besser als die anderen."},
            {"en": "We have the freshest fruit.", "de": "Wir haben das frischeste Obst."},
            {"en": "Choose the most modern phone!", "de": "Wählen Sie das modernste Handy!"},
            {"en": "Our prices are the lowest.", "de": "Unsere Preise sind am niedrigsten."},
            {"en": "It is the fastest computer.", "de": "Es ist der schnellste Computer."},
            {"en": "We offer a bigger discount.", "de": "Wir bieten einen größeren Rabatt."},
            {"en": "This is the best deal of the year.", "de": "Das ist das beste Angebot des Jahres."},
            {"en": "We have the most beautiful designs.", "de": "Wir haben die schönsten Designs."},
            {"en": "Buy the most comfortable shoes!", "de": "Kaufen Sie die bequemsten Schuhe!"},
            {"en": "This brand is the most famous.", "de": "Diese Marke ist die bekannteste."},
            {"en": "We sell the cheapest tickets.", "de": "Wir verkaufen die günstigsten Karten."},
            {"en": "It is a stronger material.", "de": "Es ist ein stärkeres Material."},
            {"en": "Our shop has the best offers.", "de": "Unser Geschäft hat die besten Angebote."},
            {"en": "This is the highest quality.", "de": "Das ist die höchste Qualität."},
            {"en": "We have a larger store now.", "de": "Wir haben jetzt einen größeren Laden."},
            {"en": "Try the tastiest coffee!", "de": "Probieren Sie den leckersten Kaffee!"},
            {"en": "It is the safest car.", "de": "Es ist das sicherste Auto."},
            {"en": "We offer the friendliest service.", "de": "Wir bieten den freundlichsten Service."},
            {"en": "This is the easiest solution.", "de": "Das ist die einfachste Lösung."},
            {"en": "Get more for less money!", "de": "Bekommen Sie mehr für weniger Geld!"},
            {"en": "We have the longest opening hours.", "de": "Wir haben die längsten Öffnungszeiten."},
            {"en": "It is the lightest laptop.", "de": "Es ist der leichteste Laptop."},
            {"en": "This is our most popular product.", "de": "Das ist unser beliebtestes Produkt."},
            {"en": "We give the fastest delivery.", "de": "Wir bieten die schnellste Lieferung."},
            {"en": "Choose the smarter option!", "de": "Wählen Sie die klügere Option!"},
            {"en": "It is the best moment to buy.", "de": "Es ist der beste Moment zum Kaufen."},
            {"en": "We have the warmest jackets.", "de": "Wir haben die wärmsten Jacken."},
            {"en": "This is the most important sale.", "de": "Das ist der wichtigste Verkauf."},
            {"en": "The best is just good enough for you.", "de": "Das Beste ist für Sie gerade gut genug."},
        ],
    },

    ("A2", "government"): {
        "note": (
            "📖 Government and Society — A2\n\n"
            "RELATIVE CLAUSES (introductory)\n"
            "A relative clause adds information about a noun. It starts with a relative "
            "pronoun (der / die / das — like \"the\"), and the verb goes to the END.\n"
            "GENDER/NUMBER come from the noun; CASE comes from its role in the clause.\n"
            "NOMINATIVE (subject of the clause):\n"
            "• Der Mann, der dort arbeitet, ist Beamter.\n"
            "• Das Formular, das auf dem Tisch liegt, ist wichtig.\n"
            "AKKUSATIVE (object of the clause): masc. der → den.\n"
            "• Das Formular, das ich brauche, ist hier.\n"
            "• Der Pass, den ich habe, ist neu.\n"
            "A comma always separates the relative clause.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "The man who works there is an official.", "de": "Der Mann, der dort arbeitet, ist Beamter."},
            {"en": "The form that I need is here.", "de": "Das Formular, das ich brauche, ist hier."},
            {"en": "The woman who helps me is friendly.", "de": "Die Frau, die mir hilft, ist freundlich."},
            {"en": "The office that is closed opens tomorrow.", "de": "Das Amt, das geschlossen ist, öffnet morgen."},
            {"en": "The passport that I have is new.", "de": "Der Pass, den ich habe, ist neu."},
            {"en": "The people who live here pay taxes.", "de": "Die Menschen, die hier wohnen, zahlen Steuern."},
            {"en": "The form that you signed is ready.", "de": "Das Formular, das du unterschrieben hast, ist fertig."},
            {"en": "The man who asks the question is a citizen.", "de": "Der Mann, der die Frage stellt, ist Bürger."},
            {"en": "The letter that I wrote is important.", "de": "Der Brief, den ich geschrieben habe, ist wichtig."},
            {"en": "The woman who works at the office is nice.", "de": "Die Frau, die im Amt arbeitet, ist nett."},
            {"en": "The rules that we follow are clear.", "de": "Die Regeln, die wir befolgen, sind klar."},
            {"en": "The government that we elected is new.", "de": "Die Regierung, die wir gewählt haben, ist neu."},
            {"en": "The official who helps us is patient.", "de": "Der Beamte, der uns hilft, ist geduldig."},
            {"en": "The document that I lost was important.", "de": "Das Dokument, das ich verloren habe, war wichtig."},
            {"en": "The city that I love is big.", "de": "Die Stadt, die ich liebe, ist groß."},
            {"en": "The man whom I know works here.", "de": "Der Mann, den ich kenne, arbeitet hier."},
            {"en": "The law that protects us is good.", "de": "Das Gesetz, das uns schützt, ist gut."},
            {"en": "The form that lies on the table is mine.", "de": "Das Formular, das auf dem Tisch liegt, ist meins."},
            {"en": "The people who vote decide.", "de": "Die Leute, die wählen, entscheiden."},
            {"en": "The card that I need is the ID card.", "de": "Die Karte, die ich brauche, ist der Ausweis."},
            {"en": "The woman who answers the phone is helpful.", "de": "Die Frau, die ans Telefon geht, ist hilfsbereit."},
            {"en": "The job that I want is at the office.", "de": "Die Stelle, die ich will, ist im Amt."},
            {"en": "The man who waits there is my neighbor.", "de": "Der Mann, der dort wartet, ist mein Nachbar."},
            {"en": "The passport that he shows is valid.", "de": "Der Pass, den er zeigt, ist gültig."},
            {"en": "The rule that everyone knows is simple.", "de": "Die Regel, die jeder kennt, ist einfach."},
            {"en": "The taxes that we pay are high.", "de": "Die Steuern, die wir zahlen, sind hoch."},
            {"en": "The teacher who explains it is good.", "de": "Der Lehrer, der es erklärt, ist gut."},
            {"en": "The book that I read is about politics.", "de": "Das Buch, das ich lese, handelt von Politik."},
            {"en": "The woman who leads the office is strict.", "de": "Die Frau, die das Amt leitet, ist streng."},
            {"en": "The decision that they make is important.", "de": "Die Entscheidung, die sie treffen, ist wichtig."},
            {"en": "The man who signs the form is the boss.", "de": "Der Mann, der das Formular unterschreibt, ist der Chef."},
            {"en": "The papers that I need are at home.", "de": "Die Papiere, die ich brauche, sind zu Hause."},
            {"en": "The citizen who votes has a voice.", "de": "Der Bürger, der wählt, hat eine Stimme."},
            {"en": "The form that you filled out is correct.", "de": "Das Formular, das du ausgefüllt hast, ist korrekt."},
            {"en": "The office that I visited was busy.", "de": "Das Amt, das ich besucht habe, war voll."},
            {"en": "The people that we know are kind.", "de": "Die Menschen, die wir kennen, sind nett."},
            {"en": "The number that you called is wrong.", "de": "Die Nummer, die du angerufen hast, ist falsch."},
            {"en": "The man who lives next door is quiet.", "de": "Der Mann, der nebenan wohnt, ist ruhig."},
            {"en": "The country that has good laws is fair.", "de": "Das Land, das gute Gesetze hat, ist fair."},
            {"en": "A government that listens is a good government.", "de": "Eine Regierung, die zuhört, ist eine gute Regierung."},
        ],
    },

    ("B1", "greeting"): {
        "note": (
            "📖 Greeting — B1\n\n"
            "THE NARRATIVE PAST (Präteritum)\n"
            "In writing and storytelling, German prefers the Präteritum over the Perfekt.\n"
            "WEAK verbs: stem + -te → machen → machte · fragen → fragte · arbeiten → arbeitete\n"
            "STRONG verbs change the stem vowel (learn them):\n"
            "  gehen → ging · kommen → kam · sehen → sah · sprechen → sprach · "
            "treffen → traf · geben → gab · nehmen → nahm · finden → fand · "
            "schreiben → schrieb · stehen → stand · rufen → rief\n"
            "Endings: ich –, du -st, er –, wir -en, ihr -t, sie -en (1st & 3rd sing. take NO ending).\n"
            "• Gestern traf ich einen alten Freund.  ·  Er kam zu spät und entschuldigte sich.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "Yesterday I met an old friend.", "de": "Gestern traf ich einen alten Freund."},
            {"en": "He came too late.", "de": "Er kam zu spät."},
            {"en": "She said hello and smiled.", "de": "Sie sagte Hallo und lächelte."},
            {"en": "We spoke for an hour.", "de": "Wir sprachen eine Stunde lang."},
            {"en": "I gave him my hand.", "de": "Ich gab ihm die Hand."},
            {"en": "He asked how I was.", "de": "Er fragte, wie es mir ging."},
            {"en": "They went into the café.", "de": "Sie gingen ins Café."},
            {"en": "I saw her at the station.", "de": "Ich sah sie am Bahnhof."},
            {"en": "She took a seat.", "de": "Sie nahm Platz."},
            {"en": "We found a free table.", "de": "Wir fanden einen freien Tisch."},
            {"en": "He wrote a short message.", "de": "Er schrieb eine kurze Nachricht."},
            {"en": "I waited in front of the door.", "de": "Ich wartete vor der Tür."},
            {"en": "She called my name.", "de": "Sie rief meinen Namen."},
            {"en": "We laughed a lot.", "de": "Wir lachten viel."},
            {"en": "He stood at the entrance.", "de": "Er stand am Eingang."},
            {"en": "I greeted the guests.", "de": "Ich begrüßte die Gäste."},
            {"en": "They talked about the old days.", "de": "Sie sprachen über die alten Zeiten."},
            {"en": "She brought two coffees.", "de": "Sie brachte zwei Kaffee."},
            {"en": "We sat by the window.", "de": "Wir saßen am Fenster."},
            {"en": "He thanked me for the help.", "de": "Er dankte mir für die Hilfe."},
            {"en": "I introduced my friend.", "de": "Ich stellte meinen Freund vor."},
            {"en": "The evening passed quickly.", "de": "Der Abend verging schnell."},
            {"en": "She told an interesting story.", "de": "Sie erzählte eine interessante Geschichte."},
            {"en": "We drank tea together.", "de": "Wir tranken zusammen Tee."},
            {"en": "He looked tired.", "de": "Er sah müde aus."},
            {"en": "I asked for her number.", "de": "Ich fragte nach ihrer Nummer."},
            {"en": "They left after midnight.", "de": "Sie gingen nach Mitternacht."},
            {"en": "She gave me a gift.", "de": "Sie gab mir ein Geschenk."},
            {"en": "We promised to meet again.", "de": "Wir versprachen, uns wiederzusehen."},
            {"en": "He understood my problem.", "de": "Er verstand mein Problem."},
            {"en": "I felt very happy.", "de": "Ich fühlte mich sehr glücklich."},
            {"en": "The waiter brought the bill.", "de": "Der Kellner brachte die Rechnung."},
            {"en": "We said goodbye.", "de": "Wir verabschiedeten uns."},
            {"en": "She walked home alone.", "de": "Sie ging allein nach Hause."},
            {"en": "I thought about the evening.", "de": "Ich dachte an den Abend."},
            {"en": "He read the letter slowly.", "de": "Er las den Brief langsam."},
            {"en": "We knew each other for years.", "de": "Wir kannten uns seit Jahren."},
            {"en": "She wore a red dress.", "de": "Sie trug ein rotes Kleid."},
            {"en": "The meeting began at eight.", "de": "Das Treffen begann um acht."},
            {"en": "It was a wonderful evening.", "de": "Es war ein wunderbarer Abend."},
        ],
    },

    ("B1", "holiday"): {
        "note": (
            "📖 Holiday — B1\n\n"
            "THE PAST PERFECT (Plusquamperfekt) — the \"past before the past\"\n"
            "Formed like the Perfekt, but with the PRÄTERITUM of haben/sein:\n"
            "  hatte / war  +  past participle\n"
            "• Ich hatte die Koffer gepackt.  ·  Wir waren schon angekommen.\n\n"
            "USE with nachdem (after): the nachdem-clause is one step earlier in time.\n"
            "Pattern: Nachdem + Plusquamperfekt , … Präteritum.\n"
            "• Nachdem wir gepackt hatten, fuhren wir zum Flughafen.\n"
            "• Nachdem sie angekommen war, rief sie ihre Familie an.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I had packed the suitcases.", "de": "Ich hatte die Koffer gepackt."},
            {"en": "We had already arrived.", "de": "Wir waren schon angekommen."},
            {"en": "After we had packed, we drove to the airport.", "de": "Nachdem wir gepackt hatten, fuhren wir zum Flughafen."},
            {"en": "After she had arrived, she called her family.", "de": "Nachdem sie angekommen war, rief sie ihre Familie an."},
            {"en": "He had booked the hotel.", "de": "Er hatte das Hotel gebucht."},
            {"en": "After we had eaten, we went to the beach.", "de": "Nachdem wir gegessen hatten, gingen wir an den Strand."},
            {"en": "I had never been abroad before.", "de": "Ich war vorher nie im Ausland gewesen."},
            {"en": "After the plane had landed, we took a taxi.", "de": "Nachdem das Flugzeug gelandet war, nahmen wir ein Taxi."},
            {"en": "She had lost her passport.", "de": "Sie hatte ihren Pass verloren."},
            {"en": "After I had unpacked, I relaxed.", "de": "Nachdem ich ausgepackt hatte, entspannte ich mich."},
            {"en": "We had planned the trip for months.", "de": "Wir hatten die Reise monatelang geplant."},
            {"en": "After they had checked in, they went out.", "de": "Nachdem sie eingecheckt hatten, gingen sie aus."},
            {"en": "He had forgotten his ticket.", "de": "Er hatte seine Fahrkarte vergessen."},
            {"en": "After we had rested, we explored the city.", "de": "Nachdem wir uns ausgeruht hatten, erkundeten wir die Stadt."},
            {"en": "I had saved money for the holiday.", "de": "Ich hatte für den Urlaub Geld gespart."},
            {"en": "After she had taken photos, she sent them to me.", "de": "Nachdem sie Fotos gemacht hatte, schickte sie sie mir."},
            {"en": "We had missed the first train.", "de": "Wir hatten den ersten Zug verpasst."},
            {"en": "After he had paid, we left the restaurant.", "de": "Nachdem er bezahlt hatte, verließen wir das Restaurant."},
            {"en": "The hotel had changed a lot.", "de": "Das Hotel hatte sich sehr verändert."},
            {"en": "After we had seen the museum, we drank coffee.", "de": "Nachdem wir das Museum gesehen hatten, tranken wir Kaffee."},
            {"en": "I had read about the country before.", "de": "Ich hatte vorher über das Land gelesen."},
            {"en": "After it had rained, the sun came out.", "de": "Nachdem es geregnet hatte, kam die Sonne heraus."},
            {"en": "She had learned a little Spanish.", "de": "Sie hatte ein bisschen Spanisch gelernt."},
            {"en": "After we had arrived, we were very tired.", "de": "Nachdem wir angekommen waren, waren wir sehr müde."},
            {"en": "They had reserved a table.", "de": "Sie hatten einen Tisch reserviert."},
            {"en": "After I had slept, I felt better.", "de": "Nachdem ich geschlafen hatte, fühlte ich mich besser."},
            {"en": "We had visited the city once before.", "de": "Wir hatten die Stadt schon einmal besucht."},
            {"en": "After the holiday had ended, we flew home.", "de": "Nachdem der Urlaub zu Ende gegangen war, flogen wir nach Hause."},
            {"en": "He had bought souvenirs for everyone.", "de": "Er hatte für alle Souvenirs gekauft."},
            {"en": "After she had said goodbye, she got on the bus.", "de": "Nachdem sie sich verabschiedet hatte, stieg sie in den Bus ein."},
            {"en": "I had not expected such good weather.", "de": "Ich hatte so gutes Wetter nicht erwartet."},
            {"en": "After we had walked all day, we were exhausted.", "de": "Nachdem wir den ganzen Tag gelaufen waren, waren wir erschöpft."},
            {"en": "The trip had cost a lot of money.", "de": "Die Reise hatte viel Geld gekostet."},
            {"en": "After he had returned, he showed us the pictures.", "de": "Nachdem er zurückgekommen war, zeigte er uns die Bilder."},
            {"en": "We had stayed in a nice hotel.", "de": "Wir hatten in einem schönen Hotel gewohnt."},
            {"en": "After they had landed, they called a taxi.", "de": "Nachdem sie gelandet waren, riefen sie ein Taxi."},
            {"en": "She had never seen the sea before.", "de": "Sie hatte das Meer vorher nie gesehen."},
            {"en": "After I had finished work, I went on holiday.", "de": "Nachdem ich mit der Arbeit fertig war, fuhr ich in den Urlaub."},
            {"en": "We had dreamed of this trip for years.", "de": "Wir hatten jahrelang von dieser Reise geträumt."},
            {"en": "After everything had been packed, we left.", "de": "Nachdem alles gepackt war, fuhren wir los."},
        ],
    },

    ("B1", "relationship"): {
        "note": (
            "📖 Relationship — B1\n\n"
            "VERBS WITH FIXED PREPOSITIONS (learn verb + preposition + case together)\n"
            "sich verlieben in (+Akk) · sich freuen auf/über (+Akk) · denken an (+Akk) · "
            "warten auf (+Akk) · sich kümmern um (+Akk) · sich interessieren für (+Akk) · "
            "träumen von (+Dat) · sich ärgern über (+Akk) · sich erinnern an (+Akk) · "
            "Angst haben vor (+Dat).\n"
            "• Ich denke oft an dich.  ·  Sie freut sich auf das Wochenende.\n\n"
            "DA- and WO-COMPOUNDS (for THINGS, not people)\n"
            "Instead of \"preposition + it\" use da(r)+prep; for questions use wo(r)+prep.\n"
            "• Ich freue mich darauf. (= auf das)  ·  Worüber sprecht ihr?\n"
            "With people, keep preposition + pronoun: Ich denke an ihn.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I often think of you.", "de": "Ich denke oft an dich."},
            {"en": "She is looking forward to the weekend.", "de": "Sie freut sich auf das Wochenende."},
            {"en": "He fell in love with her.", "de": "Er hat sich in sie verliebt."},
            {"en": "I am waiting for my friend.", "de": "Ich warte auf meinen Freund."},
            {"en": "She takes care of her children.", "de": "Sie kümmert sich um ihre Kinder."},
            {"en": "We are interested in music.", "de": "Wir interessieren uns für Musik."},
            {"en": "I dream of a big family.", "de": "Ich träume von einer großen Familie."},
            {"en": "He is afraid of the future.", "de": "Er hat Angst vor der Zukunft."},
            {"en": "I am looking forward to it.", "de": "Ich freue mich darauf."},
            {"en": "What are you talking about?", "de": "Worüber sprecht ihr?"},
            {"en": "She is annoyed about the noise.", "de": "Sie ärgert sich über den Lärm."},
            {"en": "I remember my childhood.", "de": "Ich erinnere mich an meine Kindheit."},
            {"en": "He thinks about her every day.", "de": "Er denkt jeden Tag an sie."},
            {"en": "We are waiting for the bus.", "de": "Wir warten auf den Bus."},
            {"en": "I am happy about your visit.", "de": "Ich freue mich über deinen Besuch."},
            {"en": "She is interested in him.", "de": "Sie interessiert sich für ihn."},
            {"en": "What are you waiting for?", "de": "Worauf wartest du?"},
            {"en": "He takes care of his parents.", "de": "Er kümmert sich um seine Eltern."},
            {"en": "I am thinking about it.", "de": "Ich denke darüber nach."},
            {"en": "She dreams of a trip around the world.", "de": "Sie träumt von einer Weltreise."},
            {"en": "We are looking forward to the holidays.", "de": "Wir freuen uns auf die Ferien."},
            {"en": "He is afraid of dogs.", "de": "Er hat Angst vor Hunden."},
            {"en": "I often talk to my sister.", "de": "Ich spreche oft mit meiner Schwester."},
            {"en": "She remembers him well.", "de": "Sie erinnert sich gut an ihn."},
            {"en": "What are you interested in?", "de": "Wofür interessierst du dich?"},
            {"en": "I am annoyed about the delay.", "de": "Ich ärgere mich über die Verspätung."},
            {"en": "He waited for an answer.", "de": "Er wartete auf eine Antwort."},
            {"en": "We are thinking of you.", "de": "Wir denken an dich."},
            {"en": "She is happy about the news.", "de": "Sie freut sich über die Nachricht."},
            {"en": "I am not afraid of it.", "de": "Ich habe keine Angst davor."},
            {"en": "He cares about his friends.", "de": "Er kümmert sich um seine Freunde."},
            {"en": "What is she dreaming of?", "de": "Wovon träumt sie?"},
            {"en": "I am looking forward to seeing you.", "de": "Ich freue mich darauf, dich zu sehen."},
            {"en": "She fell in love with the city.", "de": "Sie hat sich in die Stadt verliebt."},
            {"en": "We talk about everything.", "de": "Wir sprechen über alles."},
            {"en": "He is interested in politics.", "de": "Er interessiert sich für Politik."},
            {"en": "I remember that day.", "de": "Ich erinnere mich an diesen Tag."},
            {"en": "She is waiting for him.", "de": "Sie wartet auf ihn."},
            {"en": "I think about the past a lot.", "de": "Ich denke viel an die Vergangenheit."},
            {"en": "Love means caring for each other.", "de": "Liebe bedeutet, sich umeinander zu kümmern."},
        ],
    },

    ("B1", "technology"): {
        "note": (
            "📖 Technology — B1\n\n"
            "THE PASSIVE VOICE (Passiv) — present tense\n"
            "The passive focuses on the ACTION, not who does it.\n"
            "Form: werden (conjugated) + past participle (END).\n"
            "  Active:  Man repariert das Handy.\n"
            "  Passive: Das Handy wird repariert.\n"
            "  ich werde, du wirst, er/es wird, wir werden, sie werden + Partizip II.\n"
            "• Die Daten werden gespeichert.  ·  Das Programm wird installiert.\n"
            "To name the doer, use von (+Dat): Das Gerät wird von einem Techniker repariert.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "The phone is being repaired.", "de": "Das Handy wird repariert."},
            {"en": "The data is saved.", "de": "Die Daten werden gespeichert."},
            {"en": "The program is installed.", "de": "Das Programm wird installiert."},
            {"en": "The computer is switched on.", "de": "Der Computer wird eingeschaltet."},
            {"en": "The email is sent.", "de": "Die E-Mail wird gesendet."},
            {"en": "The file is deleted.", "de": "Die Datei wird gelöscht."},
            {"en": "The device is repaired by a technician.", "de": "Das Gerät wird von einem Techniker repariert."},
            {"en": "The software is updated.", "de": "Die Software wird aktualisiert."},
            {"en": "The password is changed.", "de": "Das Passwort wird geändert."},
            {"en": "The photos are uploaded.", "de": "Die Fotos werden hochgeladen."},
            {"en": "The message is read.", "de": "Die Nachricht wird gelesen."},
            {"en": "The machine is controlled by a computer.", "de": "Die Maschine wird von einem Computer gesteuert."},
            {"en": "The system is checked.", "de": "Das System wird überprüft."},
            {"en": "New apps are developed.", "de": "Neue Apps werden entwickelt."},
            {"en": "The screen is cleaned.", "de": "Der Bildschirm wird gereinigt."},
            {"en": "The documents are printed.", "de": "Die Dokumente werden gedruckt."},
            {"en": "The information is stored.", "de": "Die Informationen werden gespeichert."},
            {"en": "The battery is charged.", "de": "Der Akku wird geladen."},
            {"en": "The video is watched by many people.", "de": "Das Video wird von vielen Menschen angeschaut."},
            {"en": "The website is updated daily.", "de": "Die Webseite wird täglich aktualisiert."},
            {"en": "The problem is solved.", "de": "Das Problem wird gelöst."},
            {"en": "The code is written by a programmer.", "de": "Der Code wird von einem Programmierer geschrieben."},
            {"en": "The settings are saved.", "de": "Die Einstellungen werden gespeichert."},
            {"en": "The network is protected.", "de": "Das Netzwerk wird geschützt."},
            {"en": "The accounts are checked.", "de": "Die Konten werden überprüft."},
            {"en": "The text is translated.", "de": "Der Text wird übersetzt."},
            {"en": "The product is tested.", "de": "Das Produkt wird getestet."},
            {"en": "The data is sent automatically.", "de": "Die Daten werden automatisch gesendet."},
            {"en": "The computer is used every day.", "de": "Der Computer wird jeden Tag benutzt."},
            {"en": "The mistake is corrected.", "de": "Der Fehler wird korrigiert."},
            {"en": "The new model is presented today.", "de": "Das neue Modell wird heute vorgestellt."},
            {"en": "The phones are produced in Asia.", "de": "Die Handys werden in Asien produziert."},
            {"en": "The questions are answered quickly.", "de": "Die Fragen werden schnell beantwortet."},
            {"en": "The connection is established.", "de": "Die Verbindung wird hergestellt."},
            {"en": "The film is downloaded.", "de": "Der Film wird heruntergeladen."},
            {"en": "The robot is programmed by engineers.", "de": "Der Roboter wird von Ingenieuren programmiert."},
            {"en": "The card is read by the machine.", "de": "Die Karte wird von der Maschine gelesen."},
            {"en": "The light is turned off automatically.", "de": "Das Licht wird automatisch ausgeschaltet."},
            {"en": "The report is written today.", "de": "Der Bericht wird heute geschrieben."},
            {"en": "Technology is used everywhere.", "de": "Technik wird überall benutzt."},
        ],
    },

    ("B1", "sports"): {
        "note": (
            "📖 Sports — B1\n\n"
            "PASSIVE in the PAST and with MODALS\n"
            "PAST passive (Präteritum): wurde / wurden + Partizip II.\n"
            "  Das Spiel wurde abgesagt.  ·  Die Tore wurden gefeiert.\n"
            "PASSIVE with a MODAL: modal + Partizip II + werden (infinitive) at the END.\n"
            "  Das Training muss verschoben werden.  ·  Die Regeln müssen befolgt werden.\n"
            "Perfect passive (info): Das Spiel ist abgesagt worden. (worden, not geworden)\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "The game was cancelled.", "de": "Das Spiel wurde abgesagt."},
            {"en": "The goals were celebrated.", "de": "Die Tore wurden gefeiert."},
            {"en": "The training has to be postponed.", "de": "Das Training muss verschoben werden."},
            {"en": "The rules must be followed.", "de": "Die Regeln müssen befolgt werden."},
            {"en": "The match was won.", "de": "Das Spiel wurde gewonnen."},
            {"en": "The player was injured.", "de": "Der Spieler wurde verletzt."},
            {"en": "The stadium was built in 2010.", "de": "Das Stadion wurde 2010 gebaut."},
            {"en": "The team was trained well.", "de": "Die Mannschaft wurde gut trainiert."},
            {"en": "The tickets can be bought online.", "de": "Die Karten können online gekauft werden."},
            {"en": "The final was played in Berlin.", "de": "Das Finale wurde in Berlin gespielt."},
            {"en": "The trophy was given to the winner.", "de": "Der Pokal wurde dem Gewinner gegeben."},
            {"en": "The fans were disappointed.", "de": "Die Fans wurden enttäuscht."},
            {"en": "The rules must be explained.", "de": "Die Regeln müssen erklärt werden."},
            {"en": "The game was watched by millions.", "de": "Das Spiel wurde von Millionen gesehen."},
            {"en": "A new coach was hired.", "de": "Ein neuer Trainer wurde eingestellt."},
            {"en": "The match had to be stopped.", "de": "Das Spiel musste abgebrochen werden."},
            {"en": "The goal was not allowed.", "de": "Das Tor wurde nicht anerkannt."},
            {"en": "The players were praised.", "de": "Die Spieler wurden gelobt."},
            {"en": "The field must be prepared.", "de": "Der Platz muss vorbereitet werden."},
            {"en": "The tournament was organized well.", "de": "Das Turnier wurde gut organisiert."},
            {"en": "The result was announced.", "de": "Das Ergebnis wurde bekannt gegeben."},
            {"en": "The team can be improved.", "de": "Die Mannschaft kann verbessert werden."},
            {"en": "The medals were handed out.", "de": "Die Medaillen wurden verteilt."},
            {"en": "The injury was treated quickly.", "de": "Die Verletzung wurde schnell behandelt."},
            {"en": "The game was broadcast live.", "de": "Das Spiel wurde live übertragen."},
            {"en": "The decision must be respected.", "de": "Die Entscheidung muss respektiert werden."},
            {"en": "The stadium was filled.", "de": "Das Stadion wurde gefüllt."},
            {"en": "The training was cancelled because of rain.", "de": "Das Training wurde wegen Regen abgesagt."},
            {"en": "The new rules will be introduced.", "de": "Die neuen Regeln werden eingeführt."},
            {"en": "The champion was celebrated.", "de": "Der Meister wurde gefeiert."},
            {"en": "The ball must be passed.", "de": "Der Ball muss abgespielt werden."},
            {"en": "The match was decided in the last minute.", "de": "Das Spiel wurde in der letzten Minute entschieden."},
            {"en": "The athletes were tested.", "de": "Die Sportler wurden getestet."},
            {"en": "The schedule has to be changed.", "de": "Der Spielplan muss geändert werden."},
            {"en": "The captain was chosen by the team.", "de": "Der Kapitän wurde von der Mannschaft gewählt."},
            {"en": "The record was broken.", "de": "Der Rekord wurde gebrochen."},
            {"en": "The goal was scored in the first half.", "de": "Das Tor wurde in der ersten Halbzeit geschossen."},
            {"en": "The players must be motivated.", "de": "Die Spieler müssen motiviert werden."},
            {"en": "The season was ended early.", "de": "Die Saison wurde früh beendet."},
            {"en": "Sport must be respected and enjoyed.", "de": "Sport muss respektiert und genossen werden."},
        ],
    },

    ("B1", "food"): {
        "note": (
            "📖 Food — B1\n\n"
            "POLITE REQUESTS & WISHES — Konjunktiv II\n"
            "Konjunktiv II makes requests softer (like English \"would / could\").\n"
            "Most verbs: würde + infinitive →  Ich würde gern einen Kaffee bestellen.\n"
            "Common verbs have their OWN forms (use these, not würde):\n"
            "  haben → hätte · sein → wäre · können → könnte · mögen → möchte.\n"
            "• Ich hätte gern die Speisekarte.\n"
            "• Könnten Sie mir Wasser bringen?\n"
            "• Ich möchte bestellen.  ·  Wäre es möglich, …?\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I would like the menu.", "de": "Ich hätte gern die Speisekarte."},
            {"en": "Could you bring me water?", "de": "Könnten Sie mir Wasser bringen?"},
            {"en": "I would like to order.", "de": "Ich möchte bestellen."},
            {"en": "I would like a coffee.", "de": "Ich hätte gern einen Kaffee."},
            {"en": "Could I have the bill, please?", "de": "Könnte ich bitte die Rechnung haben?"},
            {"en": "Would you like a dessert?", "de": "Möchten Sie ein Dessert?"},
            {"en": "I would order the fish.", "de": "Ich würde den Fisch bestellen."},
            {"en": "Could you recommend something?", "de": "Könnten Sie etwas empfehlen?"},
            {"en": "I would like a table for two.", "de": "Ich hätte gern einen Tisch für zwei."},
            {"en": "Would it be possible to pay by card?", "de": "Wäre es möglich, mit Karte zu zahlen?"},
            {"en": "I would prefer a salad.", "de": "Ich hätte lieber einen Salat."},
            {"en": "Could we sit by the window?", "de": "Könnten wir am Fenster sitzen?"},
            {"en": "I would like to see the wine list.", "de": "Ich würde gern die Weinkarte sehen."},
            {"en": "Would you bring us some bread?", "de": "Würden Sie uns etwas Brot bringen?"},
            {"en": "I would like it without sugar.", "de": "Ich hätte es gern ohne Zucker."},
            {"en": "Could you make it spicy?", "de": "Könnten Sie es scharf machen?"},
            {"en": "I would like to book a table.", "de": "Ich möchte einen Tisch reservieren."},
            {"en": "Would you have a vegetarian dish?", "de": "Hätten Sie ein vegetarisches Gericht?"},
            {"en": "I would order a pizza.", "de": "Ich würde eine Pizza bestellen."},
            {"en": "Could I get a glass of water?", "de": "Könnte ich ein Glas Wasser bekommen?"},
            {"en": "I would like to try the soup.", "de": "Ich würde gern die Suppe probieren."},
            {"en": "Would you like to order now?", "de": "Möchten Sie jetzt bestellen?"},
            {"en": "I would prefer to sit outside.", "de": "Ich würde lieber draußen sitzen."},
            {"en": "Could you bring the children a smaller portion?", "de": "Könnten Sie den Kindern eine kleinere Portion bringen?"},
            {"en": "I would like the same as yesterday.", "de": "Ich hätte gern das Gleiche wie gestern."},
            {"en": "Would it be possible to change the order?", "de": "Wäre es möglich, die Bestellung zu ändern?"},
            {"en": "I would not eat that.", "de": "Das würde ich nicht essen."},
            {"en": "Could you tell me what is in it?", "de": "Könnten Sie mir sagen, was darin ist?"},
            {"en": "I would like to pay separately.", "de": "Ich möchte getrennt bezahlen."},
            {"en": "Would you recommend the dessert?", "de": "Würden Sie das Dessert empfehlen?"},
            {"en": "I would like a little more.", "de": "Ich hätte gern noch ein bisschen mehr."},
            {"en": "Could we have the menu in English?", "de": "Könnten wir die Karte auf Englisch haben?"},
            {"en": "I would order a soup as a starter.", "de": "Ich würde eine Suppe als Vorspeise bestellen."},
            {"en": "Would you have a moment?", "de": "Hätten Sie einen Moment?"},
            {"en": "I would like to thank the chef.", "de": "Ich möchte dem Koch danken."},
            {"en": "Could you bring the salt, please?", "de": "Könnten Sie bitte das Salz bringen?"},
            {"en": "I would prefer tea instead of coffee.", "de": "Ich hätte lieber Tee statt Kaffee."},
            {"en": "Would that be okay for you?", "de": "Wäre das für Sie in Ordnung?"},
            {"en": "I would like to reserve for eight o'clock.", "de": "Ich möchte für acht Uhr reservieren."},
            {"en": "It would be lovely to eat here again.", "de": "Es wäre schön, hier wieder zu essen."},
        ],
    },

    ("B1", "education"): {
        "note": (
            "📖 Education — B1\n\n"
            "HYPOTHETICALS & WISHES — Konjunktiv II\n"
            "Use Konjunktiv II for unreal situations (\"if I were…\", \"I wish…\").\n"
            "  wäre (sein) · hätte (haben) · könnte (können) · würde + infinitive.\n"
            "UNREAL conditional with wenn (both clauses in Konjunktiv II):\n"
            "• Wenn ich mehr Zeit hätte, würde ich Spanisch lernen.\n"
            "• Wenn ich reich wäre, würde ich studieren.\n"
            "WISHES:\n"
            "• Wenn ich nur mehr Zeit hätte!\n"
            "• Ich wünschte, ich könnte besser Deutsch sprechen.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "If I had more time, I would learn Spanish.", "de": "Wenn ich mehr Zeit hätte, würde ich Spanisch lernen."},
            {"en": "If I were rich, I would study.", "de": "Wenn ich reich wäre, würde ich studieren."},
            {"en": "I wish I had more time!", "de": "Wenn ich nur mehr Zeit hätte!"},
            {"en": "I wish I could speak German better.", "de": "Ich wünschte, ich könnte besser Deutsch sprechen."},
            {"en": "If I were you, I would learn more.", "de": "Wenn ich du wäre, würde ich mehr lernen."},
            {"en": "If she studied harder, she would pass.", "de": "Wenn sie mehr lernen würde, würde sie bestehen."},
            {"en": "I would help you if I could.", "de": "Ich würde dir helfen, wenn ich könnte."},
            {"en": "If I had a teacher, it would be easier.", "de": "Wenn ich einen Lehrer hätte, wäre es leichter."},
            {"en": "I wish the exam were easier.", "de": "Ich wünschte, die Prüfung wäre leichter."},
            {"en": "If we had a break, we could relax.", "de": "Wenn wir eine Pause hätten, könnten wir uns entspannen."},
            {"en": "If I knew the answer, I would tell you.", "de": "Wenn ich die Antwort wüsste, würde ich es dir sagen."},
            {"en": "It would be great to study abroad.", "de": "Es wäre toll, im Ausland zu studieren."},
            {"en": "If he had listened, he would understand now.", "de": "Wenn er zugehört hätte, würde er es jetzt verstehen."},
            {"en": "I wish I were better at math.", "de": "Ich wünschte, ich wäre besser in Mathe."},
            {"en": "If I had money, I would buy more books.", "de": "Wenn ich Geld hätte, würde ich mehr Bücher kaufen."},
            {"en": "If you practiced more, you would improve.", "de": "Wenn du mehr üben würdest, würdest du besser werden."},
            {"en": "I would take the course if it were cheaper.", "de": "Ich würde den Kurs machen, wenn er billiger wäre."},
            {"en": "If I were a teacher, I would be patient.", "de": "Wenn ich Lehrer wäre, wäre ich geduldig."},
            {"en": "I wish I could remember everything.", "de": "Ich wünschte, ich könnte mir alles merken."},
            {"en": "If we had more teachers, the classes would be smaller.", "de": "Wenn wir mehr Lehrer hätten, wären die Klassen kleiner."},
            {"en": "It would help if you explained it again.", "de": "Es würde helfen, wenn du es noch einmal erklären würdest."},
            {"en": "If I were younger, I would study medicine.", "de": "Wenn ich jünger wäre, würde ich Medizin studieren."},
            {"en": "I wish the lessons were longer.", "de": "Ich wünschte, die Stunden wären länger."},
            {"en": "If she had time, she would help me.", "de": "Wenn sie Zeit hätte, würde sie mir helfen."},
            {"en": "I would learn faster with a tutor.", "de": "Mit einem Tutor würde ich schneller lernen."},
            {"en": "If the school were closer, I would walk.", "de": "Wenn die Schule näher wäre, würde ich zu Fuß gehen."},
            {"en": "I wish I had studied harder.", "de": "Ich wünschte, ich hätte mehr gelernt."},
            {"en": "If I could choose, I would learn three languages.", "de": "Wenn ich wählen könnte, würde ich drei Sprachen lernen."},
            {"en": "It would be nice to have a smaller class.", "de": "Es wäre schön, eine kleinere Klasse zu haben."},
            {"en": "If you asked the teacher, he would help.", "de": "Wenn du den Lehrer fragen würdest, würde er helfen."},
            {"en": "I would be happier if I understood more.", "de": "Ich wäre glücklicher, wenn ich mehr verstehen würde."},
            {"en": "If I had known that, I would have studied it.", "de": "Wenn ich das gewusst hätte, hätte ich es gelernt."},
            {"en": "I wish I were more confident.", "de": "Ich wünschte, ich wäre selbstbewusster."},
            {"en": "If we worked together, it would be easier.", "de": "Wenn wir zusammenarbeiten würden, wäre es leichter."},
            {"en": "I would read more if I had time.", "de": "Ich würde mehr lesen, wenn ich Zeit hätte."},
            {"en": "If the book were cheaper, I would buy it.", "de": "Wenn das Buch billiger wäre, würde ich es kaufen."},
            {"en": "I wish I could travel and learn.", "de": "Ich wünschte, ich könnte reisen und lernen."},
            {"en": "If I were in your place, I would not give up.", "de": "An deiner Stelle würde ich nicht aufgeben."},
            {"en": "It would be better if we started now.", "de": "Es wäre besser, wenn wir jetzt anfangen würden."},
            {"en": "If everyone helped, learning would be easier.", "de": "Wenn alle helfen würden, wäre das Lernen leichter."},
        ],
    },

    ("B1", "work"): {
        "note": (
            "📖 Work — B1\n\n"
            "CONCESSION & CONSEQUENCE\n"
            "obwohl (although) — subordinate conjunction, verb goes to the END:\n"
            "• Obwohl er müde war, arbeitete er weiter.\n"
            "• Ich mag den Job, obwohl er anstrengend ist.\n"
            "trotzdem (nevertheless) — adverb, verb stays in position 2 (subject after):\n"
            "• Der Job ist hart. Trotzdem mache ich ihn gern.\n"
            "deshalb / deswegen (therefore) — adverb, verb in position 2:\n"
            "• Ich war krank, deshalb blieb ich zu Hause.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "Although he was tired, he kept working.", "de": "Obwohl er müde war, arbeitete er weiter."},
            {"en": "I like the job, although it is exhausting.", "de": "Ich mag den Job, obwohl er anstrengend ist."},
            {"en": "The job is hard. Nevertheless, I enjoy it.", "de": "Der Job ist hart. Trotzdem mache ich ihn gern."},
            {"en": "I was sick, therefore I stayed home.", "de": "Ich war krank, deshalb blieb ich zu Hause."},
            {"en": "Although she earns little, she is happy.", "de": "Obwohl sie wenig verdient, ist sie glücklich."},
            {"en": "He works a lot, therefore he is tired.", "de": "Er arbeitet viel, deshalb ist er müde."},
            {"en": "Although it was late, we finished the project.", "de": "Obwohl es spät war, beendeten wir das Projekt."},
            {"en": "The meeting was long. Nevertheless, it was useful.", "de": "Das Meeting war lang. Trotzdem war es nützlich."},
            {"en": "I had no time, therefore I could not come.", "de": "Ich hatte keine Zeit, deshalb konnte ich nicht kommen."},
            {"en": "Although he is the boss, he is very friendly.", "de": "Obwohl er der Chef ist, ist er sehr freundlich."},
            {"en": "She was ill. Nevertheless, she went to work.", "de": "Sie war krank. Trotzdem ging sie zur Arbeit."},
            {"en": "Although I tried hard, I did not get the job.", "de": "Obwohl ich mich sehr bemühte, bekam ich den Job nicht."},
            {"en": "The work is boring, therefore I want to change jobs.", "de": "Die Arbeit ist langweilig, deshalb will ich den Job wechseln."},
            {"en": "Although the salary is low, the job is interesting.", "de": "Obwohl das Gehalt niedrig ist, ist der Job interessant."},
            {"en": "He missed the train, therefore he was late.", "de": "Er verpasste den Zug, deshalb kam er zu spät."},
            {"en": "Although we were busy, we helped him.", "de": "Obwohl wir beschäftigt waren, halfen wir ihm."},
            {"en": "The deadline was tight. Nevertheless, we managed it.", "de": "Die Frist war knapp. Trotzdem schafften wir es."},
            {"en": "I like my colleagues, although the work is stressful.", "de": "Ich mag meine Kollegen, obwohl die Arbeit stressig ist."},
            {"en": "She studied hard, therefore she got the position.", "de": "Sie lernte fleißig, deshalb bekam sie die Stelle."},
            {"en": "Although he had little experience, he was hired.", "de": "Obwohl er wenig Erfahrung hatte, wurde er eingestellt."},
            {"en": "The office is far, therefore I take the train.", "de": "Das Büro ist weit, deshalb nehme ich den Zug."},
            {"en": "Although the meeting was important, he did not come.", "de": "Obwohl das Meeting wichtig war, kam er nicht."},
            {"en": "It was raining. Nevertheless, we walked to work.", "de": "Es regnete. Trotzdem gingen wir zu Fuß zur Arbeit."},
            {"en": "I was tired, therefore I drank a coffee.", "de": "Ich war müde, deshalb trank ich einen Kaffee."},
            {"en": "Although she is young, she is very experienced.", "de": "Obwohl sie jung ist, ist sie sehr erfahren."},
            {"en": "The project failed, therefore we tried again.", "de": "Das Projekt scheiterte, deshalb versuchten wir es noch einmal."},
            {"en": "Although I work a lot, I have little money.", "de": "Obwohl ich viel arbeite, habe ich wenig Geld."},
            {"en": "He was nervous. Nevertheless, he gave a good talk.", "de": "Er war nervös. Trotzdem hielt er einen guten Vortrag."},
            {"en": "Although the customer complained, we stayed calm.", "de": "Obwohl der Kunde sich beschwerte, blieben wir ruhig."},
            {"en": "The bus was late, therefore I missed the meeting.", "de": "Der Bus war spät, deshalb verpasste ich das Meeting."},
            {"en": "Although it is hard work, I would do it again.", "de": "Obwohl es harte Arbeit ist, würde ich es wieder tun."},
            {"en": "She had a cold. Nevertheless, she finished the report.", "de": "Sie war erkältet. Trotzdem beendete sie den Bericht."},
            {"en": "I respect my boss, although we often disagree.", "de": "Ich respektiere meinen Chef, obwohl wir oft anderer Meinung sind."},
            {"en": "The work was difficult, therefore we asked for help.", "de": "Die Arbeit war schwierig, deshalb baten wir um Hilfe."},
            {"en": "Although he was offered more money, he stayed.", "de": "Obwohl ihm mehr Geld angeboten wurde, blieb er."},
            {"en": "The company is small. Nevertheless, it is successful.", "de": "Die Firma ist klein. Trotzdem ist sie erfolgreich."},
            {"en": "I had an interview, therefore I wore a suit.", "de": "Ich hatte ein Vorstellungsgespräch, deshalb trug ich einen Anzug."},
            {"en": "Although the task was new, she did it well.", "de": "Obwohl die Aufgabe neu war, machte sie es gut."},
            {"en": "He works hard, therefore he deserves a break.", "de": "Er arbeitet hart, deshalb verdient er eine Pause."},
            {"en": "Although work is important, health comes first.", "de": "Obwohl die Arbeit wichtig ist, kommt die Gesundheit zuerst."},
        ],
    },

    ("B1", "health"): {
        "note": (
            "📖 Health — B1\n\n"
            "GIVING ADVICE — Konjunktiv II\n"
            "For gentle advice German uses sollte (should) and Konjunktiv II forms.\n"
            "  sollen → sollte: Du solltest mehr schlafen.\n"
            "  An deiner Stelle würde ich … → If I were you, I would …\n"
            "  Es wäre besser, wenn … → It would be better if …\n"
            "  Du könntest … → You could …\n"
            "• An deiner Stelle würde ich zum Arzt gehen.\n"
            "• Du solltest weniger Kaffee trinken.\n"
            "• Es wäre gut, wenn du dich ausruhen würdest.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "You should sleep more.", "de": "Du solltest mehr schlafen."},
            {"en": "If I were you, I would go to the doctor.", "de": "An deiner Stelle würde ich zum Arzt gehen."},
            {"en": "You should drink less coffee.", "de": "Du solltest weniger Kaffee trinken."},
            {"en": "It would be good if you rested.", "de": "Es wäre gut, wenn du dich ausruhen würdest."},
            {"en": "You could take a break.", "de": "Du könntest eine Pause machen."},
            {"en": "You should eat more vegetables.", "de": "Du solltest mehr Gemüse essen."},
            {"en": "If I were you, I would stay in bed.", "de": "An deiner Stelle würde ich im Bett bleiben."},
            {"en": "You should not smoke.", "de": "Du solltest nicht rauchen."},
            {"en": "It would be better to walk more.", "de": "Es wäre besser, mehr zu laufen."},
            {"en": "You could drink more water.", "de": "Du könntest mehr Wasser trinken."},
            {"en": "You should see a doctor.", "de": "Du solltest einen Arzt aufsuchen."},
            {"en": "If I were you, I would relax.", "de": "An deiner Stelle würde ich mich entspannen."},
            {"en": "You should take this medicine.", "de": "Du solltest dieses Medikament nehmen."},
            {"en": "It would help if you slept more.", "de": "Es würde helfen, wenn du mehr schlafen würdest."},
            {"en": "You could try yoga.", "de": "Du könntest Yoga ausprobieren."},
            {"en": "You should not work so much.", "de": "Du solltest nicht so viel arbeiten."},
            {"en": "If I were you, I would eat healthier.", "de": "An deiner Stelle würde ich gesünder essen."},
            {"en": "You should rest for a few days.", "de": "Du solltest dich ein paar Tage ausruhen."},
            {"en": "It would be wise to exercise.", "de": "Es wäre klug, Sport zu treiben."},
            {"en": "You could go for a walk.", "de": "Du könntest spazieren gehen."},
            {"en": "You should avoid stress.", "de": "Du solltest Stress vermeiden."},
            {"en": "If I were you, I would call the doctor.", "de": "An deiner Stelle würde ich den Arzt anrufen."},
            {"en": "You should drink some tea.", "de": "Du solltest einen Tee trinken."},
            {"en": "It would be better if you went home.", "de": "Es wäre besser, wenn du nach Hause gehen würdest."},
            {"en": "You could take a day off.", "de": "Du könntest einen Tag freinehmen."},
            {"en": "You should warm up before sport.", "de": "Du solltest dich vor dem Sport aufwärmen."},
            {"en": "If I were you, I would sleep early.", "de": "An deiner Stelle würde ich früh schlafen."},
            {"en": "You should eat less sugar.", "de": "Du solltest weniger Zucker essen."},
            {"en": "It would help to drink more.", "de": "Es würde helfen, mehr zu trinken."},
            {"en": "You could ask a doctor for advice.", "de": "Du könntest einen Arzt um Rat fragen."},
            {"en": "You should not lift that.", "de": "Du solltest das nicht heben."},
            {"en": "If I were you, I would rest today.", "de": "An deiner Stelle würde ich mich heute ausruhen."},
            {"en": "You should take care of yourself.", "de": "Du solltest auf dich aufpassen."},
            {"en": "It would be good to eat regularly.", "de": "Es wäre gut, regelmäßig zu essen."},
            {"en": "You could try to relax more.", "de": "Du könntest versuchen, dich mehr zu entspannen."},
            {"en": "You should breathe slowly.", "de": "Du solltest langsam atmen."},
            {"en": "If I were you, I would not worry.", "de": "An deiner Stelle würde ich mir keine Sorgen machen."},
            {"en": "You should listen to your body.", "de": "Du solltest auf deinen Körper hören."},
            {"en": "It would be better to start slowly.", "de": "Es wäre besser, langsam anzufangen."},
            {"en": "If you took care of yourself, you would feel better.", "de": "Wenn du auf dich aufpassen würdest, würdest du dich besser fühlen."},
        ],
    },

    ("B1", "books_films"): {
        "note": (
            "📖 Books and Films — B1\n\n"
            "RELATIVE CLAUSES with a PREPOSITION or the DATIVE\n"
            "The relative pronoun takes the case its role in the clause requires.\n"
            "DATIVE relative pronouns: dem (m/n), der (f), denen (pl).\n"
            "• Der Autor, dem ich geschrieben habe, hat geantwortet.\n"
            "With a PREPOSITION, the preposition comes FIRST, then the pronoun:\n"
            "• Das Buch, über das wir gesprochen haben, ist toll.\n"
            "• Der Film, in dem sie spielt, gewann einen Preis.\n"
            "• Die Freunde, mit denen ich ins Kino gehe, sind nett.\n"
            "The verb still goes to the END.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "The book that we talked about is great.", "de": "Das Buch, über das wir gesprochen haben, ist toll."},
            {"en": "The film in which she plays won a prize.", "de": "Der Film, in dem sie spielt, gewann einen Preis."},
            {"en": "The author to whom I wrote answered.", "de": "Der Autor, dem ich geschrieben habe, hat geantwortet."},
            {"en": "The friends with whom I go to the cinema are nice.", "de": "Die Freunde, mit denen ich ins Kino gehe, sind nett."},
            {"en": "The story that I am thinking of is sad.", "de": "Die Geschichte, an die ich denke, ist traurig."},
            {"en": "The actor whom we applauded smiled.", "de": "Der Schauspieler, dem wir applaudierten, lächelte."},
            {"en": "The book that I am reading is exciting.", "de": "Das Buch, das ich lese, ist spannend."},
            {"en": "The series that everyone talks about is new.", "de": "Die Serie, über die alle reden, ist neu."},
            {"en": "The film that I am waiting for starts soon.", "de": "Der Film, auf den ich warte, beginnt bald."},
            {"en": "The writer that I admire is German.", "de": "Der Schriftsteller, den ich bewundere, ist Deutscher."},
            {"en": "The cinema that we go to is modern.", "de": "Das Kino, in das wir gehen, ist modern."},
            {"en": "The book that I learned from is useful.", "de": "Das Buch, aus dem ich gelernt habe, ist nützlich."},
            {"en": "The film that he told me about is funny.", "de": "Der Film, von dem er mir erzählt hat, ist lustig."},
            {"en": "The actress with whom I took a photo was friendly.", "de": "Die Schauspielerin, mit der ich ein Foto gemacht habe, war freundlich."},
            {"en": "The story that the film is based on is true.", "de": "Die Geschichte, auf der der Film basiert, ist wahr."},
            {"en": "The people whom I recommended the book to liked it.", "de": "Die Leute, denen ich das Buch empfohlen habe, mochten es."},
            {"en": "The novel that I am interested in is long.", "de": "Der Roman, für den ich mich interessiere, ist lang."},
            {"en": "The film about which we argued is famous.", "de": "Der Film, über den wir gestritten haben, ist berühmt."},
            {"en": "The book that lies on the table is mine.", "de": "Das Buch, das auf dem Tisch liegt, ist meins."},
            {"en": "The director whom everyone knows made it.", "de": "Der Regisseur, den jeder kennt, hat ihn gemacht."},
            {"en": "The friend to whom I lent the book moved away.", "de": "Der Freund, dem ich das Buch geliehen habe, ist weggezogen."},
            {"en": "The series that I am addicted to has many seasons.", "de": "Die Serie, von der ich begeistert bin, hat viele Staffeln."},
            {"en": "The story in which the hero dies is tragic.", "de": "Die Geschichte, in der der Held stirbt, ist tragisch."},
            {"en": "The author whom I met was very kind.", "de": "Der Autor, den ich getroffen habe, war sehr nett."},
            {"en": "The book that I am looking for is sold out.", "de": "Das Buch, das ich suche, ist ausverkauft."},
            {"en": "The film that we laughed at was a comedy.", "de": "Der Film, über den wir gelacht haben, war eine Komödie."},
            {"en": "The actor whom she is a fan of is famous.", "de": "Der Schauspieler, von dem sie ein Fan ist, ist berühmt."},
            {"en": "The library that I work in is quiet.", "de": "Die Bibliothek, in der ich arbeite, ist ruhig."},
            {"en": "The film for which he won an award is short.", "de": "Der Film, für den er einen Preis gewann, ist kurz."},
            {"en": "The characters whom I like best are funny.", "de": "Die Figuren, die ich am liebsten mag, sind lustig."},
            {"en": "The book from which I read aloud is old.", "de": "Das Buch, aus dem ich vorgelesen habe, ist alt."},
            {"en": "The story that he believes in is a fairy tale.", "de": "Die Geschichte, an die er glaubt, ist ein Märchen."},
            {"en": "The film that we are watching is in German.", "de": "Der Film, den wir gerade sehen, ist auf Deutsch."},
            {"en": "The friends to whom I told the plot were surprised.", "de": "Die Freunde, denen ich die Handlung erzählt habe, waren überrascht."},
            {"en": "The novel that the series is based on is better.", "de": "Der Roman, auf dem die Serie basiert, ist besser."},
            {"en": "The author with whom I spoke gave me advice.", "de": "Der Autor, mit dem ich gesprochen habe, gab mir einen Rat."},
            {"en": "The book that I think about often is poetry.", "de": "Das Buch, an das ich oft denke, ist Lyrik."},
            {"en": "The film that I fell asleep during was boring.", "de": "Der Film, bei dem ich eingeschlafen bin, war langweilig."},
            {"en": "The story that we all know is a classic.", "de": "Die Geschichte, die wir alle kennen, ist ein Klassiker."},
            {"en": "A good book is a friend that never leaves you.", "de": "Ein gutes Buch ist ein Freund, der dich nie verlässt."},
        ],
    },

    ("B1", "accommodation"): {
        "note": (
            "📖 Accommodation — B1\n\n"
            "THE GENITIVE CASE (Genitiv) — possession (\"of\")\n"
            "Articles: des/eines (m/n, + -(e)s on the noun), der/einer (f and plural).\n"
            "  das Haus meines Vaters · die Tür der Wohnung · das Dach des Hauses · "
            "die Zimmer der Kinder.\n"
            "Masculine & neuter nouns add -(e)s: des Hauses, des Mannes.\n"
            "• Das Zimmer meiner Schwester ist groß.  ·  Die Farbe der Wände gefällt mir.\n\n"
            "GENITIVE relative pronouns: dessen (m/n), deren (f/pl) = \"whose\":\n"
            "• Der Mann, dessen Haus brennt, ruft die Feuerwehr.\n"
            "• Die Familie, deren Wohnung wir mieten, ist nett.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "My father's house is big.", "de": "Das Haus meines Vaters ist groß."},
            {"en": "The door of the flat is open.", "de": "Die Tür der Wohnung ist offen."},
            {"en": "The roof of the house is new.", "de": "Das Dach des Hauses ist neu."},
            {"en": "My sister's room is big.", "de": "Das Zimmer meiner Schwester ist groß."},
            {"en": "I like the colour of the walls.", "de": "Die Farbe der Wände gefällt mir."},
            {"en": "The children's rooms are small.", "de": "Die Zimmer der Kinder sind klein."},
            {"en": "The man whose house is burning calls the fire brigade.", "de": "Der Mann, dessen Haus brennt, ruft die Feuerwehr."},
            {"en": "The family whose flat we rent is nice.", "de": "Die Familie, deren Wohnung wir mieten, ist nett."},
            {"en": "The size of the kitchen is perfect.", "de": "Die Größe der Küche ist perfekt."},
            {"en": "The price of the flat is too high.", "de": "Der Preis der Wohnung ist zu hoch."},
            {"en": "The windows of the house are big.", "de": "Die Fenster des Hauses sind groß."},
            {"en": "My neighbor's garden is beautiful.", "de": "Der Garten meines Nachbarn ist schön."},
            {"en": "The walls of the room are white.", "de": "Die Wände des Zimmers sind weiß."},
            {"en": "The owner of the building is friendly.", "de": "Der Besitzer des Gebäudes ist freundlich."},
            {"en": "The woman whose house we visited is rich.", "de": "Die Frau, deren Haus wir besucht haben, ist reich."},
            {"en": "The address of the flat is on the letter.", "de": "Die Adresse der Wohnung steht auf dem Brief."},
            {"en": "The rent of the apartment is fair.", "de": "Die Miete der Wohnung ist fair."},
            {"en": "The keys of the house are lost.", "de": "Die Schlüssel des Hauses sind verloren."},
            {"en": "My parents' house is in the country.", "de": "Das Haus meiner Eltern ist auf dem Land."},
            {"en": "The view of the city is wonderful.", "de": "Der Blick auf die Stadt ist wunderbar."},
            {"en": "The man whose dog barks lives next door.", "de": "Der Mann, dessen Hund bellt, wohnt nebenan."},
            {"en": "The floor of the kitchen is dirty.", "de": "Der Boden der Küche ist schmutzig."},
            {"en": "The roof of the building needs repair.", "de": "Das Dach des Gebäudes muss repariert werden."},
            {"en": "The colour of the door is red.", "de": "Die Farbe der Tür ist rot."},
            {"en": "The neighbors whose children play here are nice.", "de": "Die Nachbarn, deren Kinder hier spielen, sind nett."},
            {"en": "The kitchen of the new flat is modern.", "de": "Die Küche der neuen Wohnung ist modern."},
            {"en": "The garden of the house is large.", "de": "Der Garten des Hauses ist groß."},
            {"en": "The number of the apartment is twelve.", "de": "Die Nummer der Wohnung ist zwölf."},
            {"en": "The light of the lamp is warm.", "de": "Das Licht der Lampe ist warm."},
            {"en": "The man whose car stands here is my landlord.", "de": "Der Mann, dessen Auto hier steht, ist mein Vermieter."},
            {"en": "The smell of the kitchen is wonderful.", "de": "Der Geruch der Küche ist wunderbar."},
            {"en": "The walls of my room are thin.", "de": "Die Wände meines Zimmers sind dünn."},
            {"en": "The balcony of the flat faces south.", "de": "Der Balkon der Wohnung liegt im Süden."},
            {"en": "The woman whose flat is for sale is moving.", "de": "Die Frau, deren Wohnung zum Verkauf steht, zieht um."},
            {"en": "The condition of the house is good.", "de": "Der Zustand des Hauses ist gut."},
            {"en": "The corner of the room is dark.", "de": "Die Ecke des Zimmers ist dunkel."},
            {"en": "The door of my neighbor is always open.", "de": "Die Tür meines Nachbarn ist immer offen."},
            {"en": "The roof of the church is high.", "de": "Das Dach der Kirche ist hoch."},
            {"en": "The owner whose flat we like is on holiday.", "de": "Der Besitzer, dessen Wohnung uns gefällt, ist im Urlaub."},
            {"en": "The heart of a home is its kitchen.", "de": "Das Herz eines Hauses ist seine Küche."},
        ],
    },

    ("B1", "clothes_fashion"): {
        "note": (
            "📖 Clothes & Fashion — B1\n\n"
            "ADJECTIVE ENDINGS without an article (and after quantifiers)\n"
            "With NO article, the adjective takes the ending the article would have had: "
            "-er (m), -e (f), -es (n), -e (pl nom/akk).\n"
            "• Ich trage warme Kleidung. (f)  ·  Er kauft teuren Schmuck. (m, Akk)\n"
            "• Das ist modernes Design. (n)  ·  Sie verkaufen schöne Schuhe. (pl)\n"
            "After etwas / nichts / viel → neuter adjective-noun with -es:\n"
            "• etwas Schönes · nichts Neues · viel Interessantes\n"
            "After viele / einige / wenige / andere the adjective takes -e/-en:\n"
            "• viele schöne Kleider · mit einigen guten Ideen\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I wear warm clothing.", "de": "Ich trage warme Kleidung."},
            {"en": "He buys expensive jewelry.", "de": "Er kauft teuren Schmuck."},
            {"en": "That is modern design.", "de": "Das ist modernes Design."},
            {"en": "They sell beautiful shoes.", "de": "Sie verkaufen schöne Schuhe."},
            {"en": "I am looking for something nice.", "de": "Ich suche etwas Schönes."},
            {"en": "There is nothing new.", "de": "Es gibt nichts Neues."},
            {"en": "She wears elegant clothes.", "de": "Sie trägt elegante Kleidung."},
            {"en": "We saw many beautiful dresses.", "de": "Wir sahen viele schöne Kleider."},
            {"en": "He likes dark colours.", "de": "Er mag dunkle Farben."},
            {"en": "I bought new shoes.", "de": "Ich habe neue Schuhe gekauft."},
            {"en": "That is good quality.", "de": "Das ist gute Qualität."},
            {"en": "She has expensive taste.", "de": "Sie hat teuren Geschmack."},
            {"en": "I prefer comfortable clothes.", "de": "Ich bevorzuge bequeme Kleidung."},
            {"en": "There is something interesting in the shop.", "de": "Im Geschäft gibt es etwas Interessantes."},
            {"en": "He wears bright colours.", "de": "Er trägt bunte Farben."},
            {"en": "We need warm jackets.", "de": "Wir brauchen warme Jacken."},
            {"en": "She designs modern fashion.", "de": "Sie entwirft moderne Mode."},
            {"en": "I saw nothing special.", "de": "Ich habe nichts Besonderes gesehen."},
            {"en": "They make beautiful jewelry.", "de": "Sie machen schönen Schmuck."},
            {"en": "I like soft fabrics.", "de": "Ich mag weiche Stoffe."},
            {"en": "With some good ideas we made a collection.", "de": "Mit einigen guten Ideen machten wir eine Kollektion."},
            {"en": "He buys cheap clothes.", "de": "Er kauft billige Kleidung."},
            {"en": "That is real leather.", "de": "Das ist echtes Leder."},
            {"en": "She wears bright red.", "de": "Sie trägt leuchtendes Rot."},
            {"en": "We sell fashionable shoes.", "de": "Wir verkaufen modische Schuhe."},
            {"en": "There is much interesting here.", "de": "Hier gibt es viel Interessantes."},
            {"en": "I want something warm.", "de": "Ich möchte etwas Warmes."},
            {"en": "He has good taste.", "de": "Er hat guten Geschmack."},
            {"en": "They offer high quality.", "de": "Sie bieten hohe Qualität."},
            {"en": "I like classic styles.", "de": "Ich mag klassische Stile."},
            {"en": "She bought several new bags.", "de": "Sie kaufte mehrere neue Taschen."},
            {"en": "That is pure silk.", "de": "Das ist reine Seide."},
            {"en": "We design comfortable clothing.", "de": "Wir entwerfen bequeme Kleidung."},
            {"en": "I found nothing cheap.", "de": "Ich habe nichts Billiges gefunden."},
            {"en": "He wears stylish glasses.", "de": "Er trägt stilvolle Brillen."},
            {"en": "They have few good options.", "de": "Sie haben wenige gute Optionen."},
            {"en": "I love warm colours.", "de": "Ich liebe warme Farben."},
            {"en": "That is excellent work.", "de": "Das ist ausgezeichnete Arbeit."},
            {"en": "She prefers simple elegance.", "de": "Sie bevorzugt schlichte Eleganz."},
            {"en": "Good style needs no expensive labels.", "de": "Guter Stil braucht keine teuren Labels."},
        ],
    },

    ("B1", "personality"): {
        "note": (
            "📖 Personality — B1\n\n"
            "ADJECTIVES USED AS NOUNS (nominalized adjectives)\n"
            "Turn an adjective into a noun: capitalize it, but keep adjective endings.\n"
            "  bekannt → ein Bekannter / die Bekannte (acquaintance)\n"
            "  deutsch → der Deutsche / ein Deutscher · verwandt → der/die Verwandte\n"
            "  fremd → ein Fremder (a stranger) · erwachsen → der/ein Erwachsener\n"
            "• Ein Bekannter von mir ist sehr großzügig.  ·  Die Deutschen sind oft pünktlich.\n\n"
            "N-DECLENSION (weak masculine nouns) add -(e)n in every case except nom. singular:\n"
            "  der Junge → den/dem/des Jungen · der Mensch → den Menschen · "
            "der Kollege, der Nachbar, der Kunde, der Student, der Herr.\n"
            "• Ich kenne den Jungen.  ·  Das ist das Auto des Kollegen.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "An acquaintance of mine is very generous.", "de": "Ein Bekannter von mir ist sehr großzügig."},
            {"en": "The Germans are often punctual.", "de": "Die Deutschen sind oft pünktlich."},
            {"en": "I know the boy.", "de": "Ich kenne den Jungen."},
            {"en": "He is a stranger.", "de": "Er ist ein Fremder."},
            {"en": "That is the colleague's car.", "de": "Das ist das Auto des Kollegen."},
            {"en": "A relative is visiting us.", "de": "Ein Verwandter besucht uns."},
            {"en": "The young man is very polite.", "de": "Der Jugendliche ist sehr höflich."},
            {"en": "I helped a stranger.", "de": "Ich habe einem Fremden geholfen."},
            {"en": "The employee is friendly.", "de": "Der Angestellte ist freundlich."},
            {"en": "She is a relative of mine.", "de": "Sie ist eine Verwandte von mir."},
            {"en": "I talked to the neighbor.", "de": "Ich habe mit dem Nachbarn gesprochen."},
            {"en": "The boy is shy.", "de": "Der Junge ist schüchtern."},
            {"en": "He is an acquaintance from work.", "de": "Er ist ein Bekannter von der Arbeit."},
            {"en": "We helped the man.", "de": "Wir haben dem Menschen geholfen."},
            {"en": "The German is very precise.", "de": "Der Deutsche ist sehr genau."},
            {"en": "I know the student well.", "de": "Ich kenne den Studenten gut."},
            {"en": "A young person needs support.", "de": "Ein Jugendlicher braucht Unterstützung."},
            {"en": "The customer is always right.", "de": "Der Kunde hat immer recht."},
            {"en": "The sick man rested.", "de": "Der Kranke ruhte sich aus."},
            {"en": "I trust my colleague.", "de": "Ich vertraue dem Kollegen."},
            {"en": "She greeted the stranger kindly.", "de": "Sie begrüßte den Fremden freundlich."},
            {"en": "The unemployed man is looking for work.", "de": "Der Arbeitslose sucht Arbeit."},
            {"en": "Many relatives came to the party.", "de": "Viele Verwandte kamen zur Party."},
            {"en": "I gave the boy a gift.", "de": "Ich gab dem Jungen ein Geschenk."},
            {"en": "The new colleague is competent.", "de": "Der neue Kollege ist kompetent."},
            {"en": "He is a typical German.", "de": "Er ist ein typischer Deutscher."},
            {"en": "The grown-ups talked for hours.", "de": "Die Erwachsenen redeten stundenlang."},
            {"en": "I saw the customer leave.", "de": "Ich sah den Kunden gehen."},
            {"en": "An adult should be responsible.", "de": "Ein Erwachsener sollte verantwortlich sein."},
            {"en": "The traveler asked for directions.", "de": "Der Reisende fragte nach dem Weg."},
            {"en": "We invited the neighbors.", "de": "Wir haben die Nachbarn eingeladen."},
            {"en": "The intellectual gave a speech.", "de": "Der Intellektuelle hielt eine Rede."},
            {"en": "I know that gentleman.", "de": "Ich kenne diesen Herrn."},
            {"en": "The employee works hard.", "de": "Der Angestellte arbeitet hart."},
            {"en": "A good acquaintance helped me.", "de": "Ein guter Bekannter hat mir geholfen."},
            {"en": "The relatives live abroad.", "de": "Die Verwandten wohnen im Ausland."},
            {"en": "He behaves like an adult.", "de": "Er benimmt sich wie ein Erwachsener."},
            {"en": "I spoke with the student.", "de": "Ich habe mit dem Studenten gesprochen."},
            {"en": "The newcomer felt welcome.", "de": "Der Neue fühlte sich willkommen."},
            {"en": "Every person deserves respect.", "de": "Jeder Mensch verdient Respekt."},
        ],
    },

    ("B1", "business"): {
        "note": (
            "📖 Business and Money — B1\n\n"
            "PREPOSITIONS that take the GENITIVE\n"
            "wegen (because of) · während (during) · trotz (despite) · (an)statt (instead of) · "
            "innerhalb (within) · außerhalb (outside of) · aufgrund (due to).\n"
            "Followed by the Genitiv: des/eines (m/n + -s), der/einer (f/pl).\n"
            "• Wegen des Wetters bleiben wir zu Hause.\n"
            "• Während der Arbeit darf man nicht telefonieren.\n"
            "• Trotz des Regens gingen wir spazieren.\n"
            "• Innerhalb einer Woche kam die Antwort.\n"
            "(In casual speech wegen + Dativ is also heard, but the Genitiv is standard.)\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "Because of the weather we stay home.", "de": "Wegen des Wetters bleiben wir zu Hause."},
            {"en": "During work you may not phone.", "de": "Während der Arbeit darf man nicht telefonieren."},
            {"en": "Despite the rain we went for a walk.", "de": "Trotz des Regens gingen wir spazieren."},
            {"en": "The answer came within a week.", "de": "Innerhalb einer Woche kam die Antwort."},
            {"en": "Because of the price I did not buy it.", "de": "Wegen des Preises habe ich es nicht gekauft."},
            {"en": "During the meeting he was quiet.", "de": "Während des Meetings war er ruhig."},
            {"en": "Despite the problems the project succeeded.", "de": "Trotz der Probleme war das Projekt erfolgreich."},
            {"en": "Instead of a bonus we got a free day.", "de": "Anstatt eines Bonus bekamen wir einen freien Tag."},
            {"en": "The shop is open outside business hours.", "de": "Das Geschäft ist außerhalb der Geschäftszeiten offen."},
            {"en": "Because of the crisis prices rose.", "de": "Wegen der Krise stiegen die Preise."},
            {"en": "During the holidays the office is closed.", "de": "Während der Ferien ist das Büro geschlossen."},
            {"en": "Despite his age he still works.", "de": "Trotz seines Alters arbeitet er noch."},
            {"en": "We must decide within a month.", "de": "Innerhalb eines Monats müssen wir entscheiden."},
            {"en": "Because of the delay we missed the deal.", "de": "Wegen der Verspätung verpassten wir das Geschäft."},
            {"en": "During the negotiation everyone was nervous.", "de": "Während der Verhandlung waren alle nervös."},
            {"en": "Despite the high costs they continued.", "de": "Trotz der hohen Kosten machten sie weiter."},
            {"en": "Instead of the meeting we sent an email.", "de": "Anstatt des Meetings schickten wir eine E-Mail."},
            {"en": "The payment must come within ten days.", "de": "Innerhalb von zehn Tagen muss die Zahlung kommen."},
            {"en": "Because of an error the invoice was wrong.", "de": "Wegen eines Fehlers war die Rechnung falsch."},
            {"en": "During the presentation the screen broke.", "de": "Während der Präsentation ging der Bildschirm kaputt."},
            {"en": "Despite the competition the company grew.", "de": "Trotz der Konkurrenz wuchs die Firma."},
            {"en": "Outside the city rents are lower.", "de": "Außerhalb der Stadt ist die Miete niedriger."},
            {"en": "Because of the strike the trains stopped.", "de": "Wegen des Streiks fuhren keine Züge."},
            {"en": "During the week I have no time.", "de": "Während der Woche habe ich keine Zeit."},
            {"en": "Despite the risk we invested.", "de": "Trotz des Risikos investierten wir."},
            {"en": "Within the team we trust each other.", "de": "Innerhalb des Teams vertrauen wir uns."},
            {"en": "Because of the demand we hired more people.", "de": "Wegen der Nachfrage stellten wir mehr Leute ein."},
            {"en": "During the crisis many shops closed.", "de": "Während der Krise schlossen viele Geschäfte."},
            {"en": "Despite the warning he signed the contract.", "de": "Trotz der Warnung unterschrieb er den Vertrag."},
            {"en": "Instead of money she offered her time.", "de": "Anstatt des Geldes bot sie ihre Zeit an."},
            {"en": "Because of the holidays delivery takes longer.", "de": "Wegen der Feiertage dauert die Lieferung länger."},
            {"en": "During the day the bank is busy.", "de": "Während des Tages ist die Bank voll."},
            {"en": "Despite the loss the company survived.", "de": "Trotz des Verlusts überlebte die Firma."},
            {"en": "The decision was made within the company.", "de": "Die Entscheidung wurde innerhalb der Firma getroffen."},
            {"en": "Because of the new law taxes changed.", "de": "Wegen des neuen Gesetzes änderten sich die Steuern."},
            {"en": "During the interview I was confident.", "de": "Während des Gesprächs war ich selbstbewusst."},
            {"en": "Despite the difficulties we kept going.", "de": "Trotz der Schwierigkeiten machten wir weiter."},
            {"en": "Outside working hours nobody answers.", "de": "Außerhalb der Arbeitszeit antwortet niemand."},
            {"en": "Because of the success they expanded.", "de": "Wegen des Erfolgs expandierten sie."},
            {"en": "Despite all the work, business was good.", "de": "Trotz der ganzen Arbeit lief das Geschäft gut."},
        ],
    },

    ("B1", "physical_appearance"): {
        "note": (
            "📖 Physical Appearance — B1\n\n"
            "PARTICIPLES AS ADJECTIVES (Partizip I & II)\n"
            "Place a participle before a noun like an adjective (with normal endings).\n"
            "PARTIZIP I (active, \"-ing\"): infinitive + d → lachend, weinend, schlafend.\n"
            "  ein lachendes Kind · die strahlende Frau\n"
            "PARTIZIP II (passive/finished, \"-ed\"): the normal past participle.\n"
            "  die geöffnete Tür · ein gut gekleideter Mann · gefärbte Haare\n"
            "• Der lächelnde Mann winkte mir.  ·  Sie trägt eine gestreifte Bluse.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "The smiling man waved at me.", "de": "Der lächelnde Mann winkte mir."},
            {"en": "She is a laughing child.", "de": "Sie ist ein lachendes Kind."},
            {"en": "He wears a striped shirt.", "de": "Er trägt ein gestreiftes Hemd."},
            {"en": "The well-dressed man entered.", "de": "Der gut gekleidete Mann kam herein."},
            {"en": "She has dyed hair.", "de": "Sie hat gefärbte Haare."},
            {"en": "The crying baby needs its mother.", "de": "Das weinende Baby braucht seine Mutter."},
            {"en": "He has a charming smile.", "de": "Er hat ein bezauberndes Lächeln."},
            {"en": "The sleeping cat looks cute.", "de": "Die schlafende Katze sieht süß aus."},
            {"en": "She wore a torn jacket.", "de": "Sie trug eine zerrissene Jacke."},
            {"en": "The shining sun made her happy.", "de": "Die scheinende Sonne machte sie glücklich."},
            {"en": "He is a well-known actor.", "de": "Er ist ein bekannter Schauspieler."},
            {"en": "The painted nails look elegant.", "de": "Die lackierten Nägel sehen elegant aus."},
            {"en": "A smiling face is welcoming.", "de": "Ein lächelndes Gesicht wirkt einladend."},
            {"en": "She has curled hair.", "de": "Sie hat gelockte Haare."},
            {"en": "The running man was in a hurry.", "de": "Der laufende Mann hatte es eilig."},
            {"en": "He wears polished shoes.", "de": "Er trägt polierte Schuhe."},
            {"en": "The freshly washed hair shines.", "de": "Das frisch gewaschene Haar glänzt."},
            {"en": "The standing woman waited patiently.", "de": "Die stehende Frau wartete geduldig."},
            {"en": "She has a tired face.", "de": "Sie hat ein müdes Gesicht."},
            {"en": "The combed hair looks neat.", "de": "Die gekämmten Haare sehen ordentlich aus."},
            {"en": "A growing child needs sleep.", "de": "Ein wachsendes Kind braucht Schlaf."},
            {"en": "He has a trimmed beard.", "de": "Er hat einen gestutzten Bart."},
            {"en": "The dancing couple looked happy.", "de": "Das tanzende Paar sah glücklich aus."},
            {"en": "She wears an ironed blouse.", "de": "Sie trägt eine gebügelte Bluse."},
            {"en": "The smiling girl took a photo.", "de": "Das lächelnde Mädchen machte ein Foto."},
            {"en": "He has broad, trained shoulders.", "de": "Er hat breite, trainierte Schultern."},
            {"en": "The relaxed man smiled.", "de": "Der entspannte Mann lächelte."},
            {"en": "She has well-groomed hands.", "de": "Sie hat gepflegte Hände."},
            {"en": "The waiting guests were patient.", "de": "Die wartenden Gäste waren geduldig."},
            {"en": "He wears a tailored suit.", "de": "Er trägt einen maßgeschneiderten Anzug."},
            {"en": "The sparkling eyes were beautiful.", "de": "Die funkelnden Augen waren schön."},
            {"en": "She has tied-back hair.", "de": "Sie hat zusammengebundene Haare."},
            {"en": "The well-dressed woman entered.", "de": "Die gut gekleidete Frau kam herein."},
            {"en": "He has a worried look.", "de": "Er hat einen besorgten Blick."},
            {"en": "The aging man stayed active.", "de": "Der alternde Mann blieb aktiv."},
            {"en": "She wore a freshly cleaned dress.", "de": "Sie trug ein frisch gereinigtes Kleid."},
            {"en": "The beaming bride was radiant.", "de": "Die strahlende Braut sah wunderschön aus."},
            {"en": "He has a freshly shaved face.", "de": "Er hat ein frisch rasiertes Gesicht."},
            {"en": "The trembling hands showed fear.", "de": "Die zitternden Hände zeigten Angst."},
            {"en": "A friendly, smiling person is attractive.", "de": "Ein freundlicher, lächelnder Mensch ist attraktiv."},
        ],
    },

    ("B1", "town_city"): {
        "note": (
            "📖 Town and City — B1\n\n"
            "TEMPORAL SUBORDINATE CLAUSES (verb to the END)\n"
            "These conjunctions place an action in time; the verb goes to the end of the clause.\n"
            "  bevor (before) · nachdem (after) · während (while) · seitdem/seit (since) · "
            "sobald (as soon as) · bis (until).\n"
            "• Bevor ich in die Stadt fahre, frühstücke ich.\n"
            "• Während ich im Bus saß, las ich ein Buch.\n"
            "• Seitdem ich hier wohne, nehme ich die U-Bahn.\n"
            "• Sobald der Bus kommt, steigen wir ein.\n"
            "(With nachdem use Plusquamperfekt + Präteritum — see Holiday B1.)\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "Before I go into town, I have breakfast.", "de": "Bevor ich in die Stadt fahre, frühstücke ich."},
            {"en": "While I was sitting on the bus, I read a book.", "de": "Während ich im Bus saß, las ich ein Buch."},
            {"en": "Since I live here, I take the subway.", "de": "Seitdem ich hier wohne, nehme ich die U-Bahn."},
            {"en": "As soon as the bus comes, we get on.", "de": "Sobald der Bus kommt, steigen wir ein."},
            {"en": "Before we left, we locked the door.", "de": "Bevor wir gingen, schlossen wir die Tür ab."},
            {"en": "While she was shopping, he waited outside.", "de": "Während sie einkaufte, wartete er draußen."},
            {"en": "After we had arrived, we found the hotel.", "de": "Nachdem wir angekommen waren, fanden wir das Hotel."},
            {"en": "Since the new line opened, the journey is faster.", "de": "Seitdem die neue Linie eröffnet ist, ist die Fahrt schneller."},
            {"en": "As soon as I arrive, I will call you.", "de": "Sobald ich ankomme, rufe ich dich an."},
            {"en": "Before you cross the street, look left.", "de": "Bevor du die Straße überquerst, schau nach links."},
            {"en": "While we walked through the city, it started to rain.", "de": "Während wir durch die Stadt liefen, begann es zu regnen."},
            {"en": "Since I moved here, I know more people.", "de": "Seitdem ich hierher gezogen bin, kenne ich mehr Leute."},
            {"en": "As soon as the shops open, I go shopping.", "de": "Sobald die Geschäfte öffnen, gehe ich einkaufen."},
            {"en": "Before the train leaves, we buy tickets.", "de": "Bevor der Zug abfährt, kaufen wir Karten."},
            {"en": "While he was driving, she navigated.", "de": "Während er fuhr, navigierte sie."},
            {"en": "After he had parked, we went into the museum.", "de": "Nachdem er geparkt hatte, gingen wir ins Museum."},
            {"en": "Since they built the bridge, the traffic is better.", "de": "Seitdem sie die Brücke gebaut haben, ist der Verkehr besser."},
            {"en": "As soon as we got off, we found the café.", "de": "Sobald wir ausstiegen, fanden wir das Café."},
            {"en": "Before I take the bus, I check the time.", "de": "Bevor ich den Bus nehme, schaue ich auf die Zeit."},
            {"en": "While the city slept, the streets were empty.", "de": "Während die Stadt schlief, waren die Straßen leer."},
            {"en": "Since the museum is free, more people visit it.", "de": "Seitdem das Museum kostenlos ist, besuchen es mehr Menschen."},
            {"en": "As soon as it gets dark, the lights turn on.", "de": "Sobald es dunkel wird, gehen die Lichter an."},
            {"en": "Before we entered, we waited in line.", "de": "Bevor wir hineingingen, warteten wir in der Schlange."},
            {"en": "While I was waiting, I read the map.", "de": "Während ich wartete, las ich die Karte."},
            {"en": "Since I started cycling, I am fitter.", "de": "Seitdem ich Rad fahre, bin ich fitter."},
            {"en": "As soon as the light turns green, we cross.", "de": "Sobald die Ampel grün wird, gehen wir über die Straße."},
            {"en": "Before the market closes, I buy vegetables.", "de": "Bevor der Markt schließt, kaufe ich Gemüse."},
            {"en": "While the tourists took photos, the guide explained.", "de": "Während die Touristen Fotos machten, erklärte der Führer."},
            {"en": "After we had seen the cathedral, we drank coffee.", "de": "Nachdem wir den Dom gesehen hatten, tranken wir Kaffee."},
            {"en": "Since the road was closed, we took another way.", "de": "Seitdem die Straße gesperrt war, nahmen wir einen anderen Weg."},
            {"en": "As soon as I find a parking spot, I will text you.", "de": "Sobald ich einen Parkplatz finde, schreibe ich dir."},
            {"en": "Before the bus arrived, it started to snow.", "de": "Bevor der Bus ankam, begann es zu schneien."},
            {"en": "While we explored the old town, we got lost.", "de": "Während wir die Altstadt erkundeten, verirrten wir uns."},
            {"en": "Since the station was renovated, it looks modern.", "de": "Seitdem der Bahnhof renoviert wurde, sieht er modern aus."},
            {"en": "As soon as we arrive, we will check in.", "de": "Sobald wir ankommen, checken wir ein."},
            {"en": "Before you leave, turn off the lights.", "de": "Bevor du gehst, schalte das Licht aus."},
            {"en": "While she was reading the sign, the bus left.", "de": "Während sie das Schild las, fuhr der Bus ab."},
            {"en": "Since I know the city, I never get lost.", "de": "Seitdem ich die Stadt kenne, verirre ich mich nie."},
            {"en": "As soon as the rain stopped, we went outside.", "de": "Sobald der Regen aufhörte, gingen wir nach draußen."},
            {"en": "Before the journey ends, enjoy the view.", "de": "Bevor die Reise endet, genieße die Aussicht."},
        ],
    },

    ("B1", "music"): {
        "note": (
            "📖 Music — B1\n\n"
            "INFINITIVE CLAUSES with zu\n"
            "Many verbs and expressions are followed by zu + infinitive (at the END).\n"
            "  Ich versuche, Gitarre zu spielen.  ·  Es macht Spaß, zu singen.\n"
            "With separable verbs, zu goes inside: anzufangen, mitzusingen.\n"
            "SPECIAL connectors (same subject in both parts):\n"
            "  um … zu (in order to): Ich übe, um besser zu werden.\n"
            "  ohne … zu (without …-ing): Er sang, ohne zu üben.\n"
            "  (an)statt … zu (instead of …-ing): Sie spielte Klavier, anstatt zu lernen.\n"
            "Triggers: versuchen, vergessen, anfangen, aufhören, Lust haben, Spaß machen, hoffen.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I try to play the guitar.", "de": "Ich versuche, Gitarre zu spielen."},
            {"en": "It is fun to sing.", "de": "Es macht Spaß, zu singen."},
            {"en": "He sang without practicing.", "de": "Er sang, ohne zu üben."},
            {"en": "She played piano instead of studying.", "de": "Sie spielte Klavier, anstatt zu lernen."},
            {"en": "I practice in order to get better.", "de": "Ich übe, um besser zu werden."},
            {"en": "I forgot to bring my guitar.", "de": "Ich habe vergessen, meine Gitarre mitzubringen."},
            {"en": "He started to learn the drums.", "de": "Er fing an, Schlagzeug zu lernen."},
            {"en": "We stopped singing.", "de": "Wir hörten auf zu singen."},
            {"en": "I feel like dancing.", "de": "Ich habe Lust zu tanzen."},
            {"en": "She hopes to play in a band.", "de": "Sie hofft, in einer Band zu spielen."},
            {"en": "It is important to practice every day.", "de": "Es ist wichtig, jeden Tag zu üben."},
            {"en": "He left without saying goodbye.", "de": "Er ging, ohne sich zu verabschieden."},
            {"en": "I try to sing in tune.", "de": "Ich versuche, richtig zu singen."},
            {"en": "Instead of resting, she rehearsed.", "de": "Anstatt sich auszuruhen, probte sie."},
            {"en": "We came to listen to the concert.", "de": "Wir kamen, um das Konzert zu hören."},
            {"en": "He plays without reading the notes.", "de": "Er spielt, ohne die Noten zu lesen."},
            {"en": "It is not easy to learn an instrument.", "de": "Es ist nicht leicht, ein Instrument zu lernen."},
            {"en": "I promised to come to the show.", "de": "Ich habe versprochen, zur Show zu kommen."},
            {"en": "She decided to study music.", "de": "Sie hat beschlossen, Musik zu studieren."},
            {"en": "We are happy to be here.", "de": "Wir freuen uns, hier zu sein."},
            {"en": "He practices in order to win.", "de": "Er übt, um zu gewinnen."},
            {"en": "I started to write a song.", "de": "Ich fing an, ein Lied zu schreiben."},
            {"en": "Instead of watching TV, he played guitar.", "de": "Anstatt fernzusehen, spielte er Gitarre."},
            {"en": "It is great to make music together.", "de": "Es ist toll, zusammen Musik zu machen."},
            {"en": "She tries to sing every day.", "de": "Sie versucht, jeden Tag zu singen."},
            {"en": "He went on stage without being nervous.", "de": "Er ging auf die Bühne, ohne nervös zu sein."},
            {"en": "I have time to practice tonight.", "de": "Ich habe heute Abend Zeit zu üben."},
            {"en": "We plan to record a song.", "de": "Wir planen, ein Lied aufzunehmen."},
            {"en": "It is fun to learn new songs.", "de": "Es macht Spaß, neue Lieder zu lernen."},
            {"en": "She forgot to turn off the music.", "de": "Sie vergaß, die Musik auszuschalten."},
            {"en": "He hopes to become a musician.", "de": "Er hofft, Musiker zu werden."},
            {"en": "Instead of complaining, she practiced more.", "de": "Anstatt sich zu beschweren, übte sie mehr."},
            {"en": "I love to listen to live music.", "de": "Ich liebe es, Live-Musik zu hören."},
            {"en": "We tried to find tickets.", "de": "Wir versuchten, Karten zu finden."},
            {"en": "He learned to play without a teacher.", "de": "Er lernte zu spielen, ohne einen Lehrer zu haben."},
            {"en": "It is hard to stop once you start.", "de": "Es ist schwer aufzuhören, wenn man einmal anfängt."},
            {"en": "She offered to teach me.", "de": "Sie bot an, mir Unterricht zu geben."},
            {"en": "We are looking forward to performing.", "de": "Wir freuen uns darauf, aufzutreten."},
            {"en": "He continued to play despite the noise.", "de": "Er spielte weiter, ohne auf den Lärm zu achten."},
            {"en": "Music gives us a reason to celebrate.", "de": "Musik gibt uns einen Grund zu feiern."},
        ],
    },

    ("B1", "weather"): {
        "note": (
            "📖 Weather — B1\n\n"
            "UNREAL CONDITIONALS — Konjunktiv II (present & past)\n"
            "PRESENT unreal: wenn + Konjunktiv II , … Konjunktiv II.\n"
            "• Wenn es nicht regnen würde, würden wir spazieren gehen.\n"
            "• Wenn ich Zeit hätte, würde ich an den Strand fahren.\n"
            "PAST unreal (a missed past possibility): wenn + hätte/wäre + Partizip II …, "
            "… hätte/wäre + Partizip II.\n"
            "• Wenn es gestern nicht geregnet hätte, wären wir gegangen.\n"
            "• Wenn ich das gewusst hätte, hätte ich einen Schirm mitgenommen.\n"
            "Use hätte for haben-verbs, wäre for sein-verbs.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "If it were not raining, we would go for a walk.", "de": "Wenn es nicht regnen würde, würden wir spazieren gehen."},
            {"en": "If I had time, I would go to the beach.", "de": "Wenn ich Zeit hätte, würde ich an den Strand fahren."},
            {"en": "If it had not rained yesterday, we would have gone.", "de": "Wenn es gestern nicht geregnet hätte, wären wir gegangen."},
            {"en": "If I had known that, I would have taken an umbrella.", "de": "Wenn ich das gewusst hätte, hätte ich einen Schirm mitgenommen."},
            {"en": "If the sun were shining, I would be happy.", "de": "Wenn die Sonne scheinen würde, wäre ich glücklich."},
            {"en": "If it were warmer, we would swim.", "de": "Wenn es wärmer wäre, würden wir schwimmen."},
            {"en": "If it snowed, the children would be happy.", "de": "Wenn es schneien würde, wären die Kinder glücklich."},
            {"en": "If I had a coat, I would not be cold.", "de": "Wenn ich einen Mantel hätte, wäre mir nicht kalt."},
            {"en": "If it had been sunny, we would have had a picnic.", "de": "Wenn es sonnig gewesen wäre, hätten wir ein Picknick gemacht."},
            {"en": "If the weather were better, we would travel.", "de": "Wenn das Wetter besser wäre, würden wir reisen."},
            {"en": "If it were not so hot, I could sleep.", "de": "Wenn es nicht so heiß wäre, könnte ich schlafen."},
            {"en": "If I had checked the forecast, I would have stayed home.", "de": "Wenn ich den Wetterbericht gelesen hätte, wäre ich zu Hause geblieben."},
            {"en": "If there were no wind, sailing would be impossible.", "de": "Wenn es keinen Wind gäbe, wäre Segeln unmöglich."},
            {"en": "If it rained less, the streets would be drier.", "de": "Wenn es weniger regnen würde, wären die Straßen trockener."},
            {"en": "If I were you, I would take a jacket.", "de": "An deiner Stelle würde ich eine Jacke mitnehmen."},
            {"en": "If it had not been so cold, we would have stayed longer.", "de": "Wenn es nicht so kalt gewesen wäre, wären wir länger geblieben."},
            {"en": "If the sky were clear, we could see the stars.", "de": "Wenn der Himmel klar wäre, könnten wir die Sterne sehen."},
            {"en": "If it were spring, the flowers would bloom.", "de": "Wenn es Frühling wäre, würden die Blumen blühen."},
            {"en": "If I had brought an umbrella, I would be dry now.", "de": "Wenn ich einen Schirm mitgebracht hätte, wäre ich jetzt trocken."},
            {"en": "If it were not foggy, the flight would leave.", "de": "Wenn es nicht neblig wäre, würde der Flug starten."},
            {"en": "If the storm had not come, we would have sailed.", "de": "Wenn der Sturm nicht gekommen wäre, wären wir gesegelt."},
            {"en": "If I had more time, I would enjoy the sun.", "de": "Wenn ich mehr Zeit hätte, würde ich die Sonne genießen."},
            {"en": "If it were colder, it would snow.", "de": "Wenn es kälter wäre, würde es schneien."},
            {"en": "If we had left earlier, we would have avoided the rain.", "de": "Wenn wir früher gegangen wären, hätten wir den Regen vermieden."},
            {"en": "If the weather allowed, we would go hiking.", "de": "Wenn das Wetter es erlauben würde, würden wir wandern gehen."},
            {"en": "If I were on holiday, I would lie in the sun.", "de": "Wenn ich im Urlaub wäre, würde ich in der Sonne liegen."},
            {"en": "If it had snowed, we would have gone skiing.", "de": "Wenn es geschneit hätte, wären wir Ski gefahren."},
            {"en": "If the temperature rose, the ice would melt.", "de": "Wenn die Temperatur steigen würde, würde das Eis schmelzen."},
            {"en": "If I had a garden, I would enjoy the spring.", "de": "Wenn ich einen Garten hätte, würde ich den Frühling genießen."},
            {"en": "If it were not so windy, we could cycle.", "de": "Wenn es nicht so windig wäre, könnten wir Rad fahren."},
            {"en": "If the rain had stopped, we would have continued.", "de": "Wenn der Regen aufgehört hätte, hätten wir weitergemacht."},
            {"en": "If summer lasted longer, I would be glad.", "de": "Wenn der Sommer länger dauern würde, wäre ich froh."},
            {"en": "If I had known it would rain, I would have stayed inside.", "de": "Wenn ich gewusst hätte, dass es regnet, wäre ich drinnen geblieben."},
            {"en": "If it were warmer, the lake would not freeze.", "de": "Wenn es wärmer wäre, würde der See nicht zufrieren."},
            {"en": "If we had a boat, we would go on the water.", "de": "Wenn wir ein Boot hätten, würden wir aufs Wasser fahren."},
            {"en": "If the weather were nicer, more people would come.", "de": "Wenn das Wetter schöner wäre, würden mehr Leute kommen."},
            {"en": "If it had been dry, the path would have been easier.", "de": "Wenn es trocken gewesen wäre, wäre der Weg leichter gewesen."},
            {"en": "If there were more sun, the fruit would ripen.", "de": "Wenn es mehr Sonne gäbe, würde das Obst reifen."},
            {"en": "If I could change the weather, it would always be spring.", "de": "Wenn ich das Wetter ändern könnte, wäre immer Frühling."},
            {"en": "If everyone watched the forecast, fewer people would be surprised.", "de": "Wenn alle den Wetterbericht schauen würden, wären weniger Leute überrascht."},
        ],
    },

    ("B1", "shopping"): {
        "note": (
            "📖 Shopping — B1\n\n"
            "TWO-PART CONNECTORS (correlative conjunctions)\n"
            "These come in pairs and link two ideas:\n"
            "  entweder … oder (either … or) · weder … noch (neither … nor) · "
            "sowohl … als auch (both … and) · nicht nur … sondern auch (not only … but also) · "
            "je … desto/umso (the … the).\n"
            "• Ich kaufe entweder die Jacke oder den Mantel.\n"
            "• Das Geschäft hat weder Brot noch Milch.\n"
            "• Sie verkaufen sowohl Kleidung als auch Schuhe.\n"
            "• Je teurer das Produkt, desto besser die Qualität. (je-clause: verb to END)\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I buy either the jacket or the coat.", "de": "Ich kaufe entweder die Jacke oder den Mantel."},
            {"en": "The shop has neither bread nor milk.", "de": "Das Geschäft hat weder Brot noch Milch."},
            {"en": "They sell both clothes and shoes.", "de": "Sie verkaufen sowohl Kleidung als auch Schuhe."},
            {"en": "The more expensive the product, the better the quality.", "de": "Je teurer das Produkt, desto besser die Qualität."},
            {"en": "I want not only a shirt but also a tie.", "de": "Ich möchte nicht nur ein Hemd, sondern auch eine Krawatte."},
            {"en": "We can either pay now or later.", "de": "Wir können entweder jetzt oder später zahlen."},
            {"en": "She buys neither meat nor fish.", "de": "Sie kauft weder Fleisch noch Fisch."},
            {"en": "The shop is both cheap and good.", "de": "Das Geschäft ist sowohl billig als auch gut."},
            {"en": "The bigger the shop, the more choice.", "de": "Je größer das Geschäft, desto mehr Auswahl."},
            {"en": "He bought not only food but also drinks.", "de": "Er kaufte nicht nur Essen, sondern auch Getränke."},
            {"en": "You can pay either by card or in cash.", "de": "Du kannst entweder mit Karte oder bar zahlen."},
            {"en": "I have neither time nor money.", "de": "Ich habe weder Zeit noch Geld."},
            {"en": "They offer both quality and good prices.", "de": "Sie bieten sowohl Qualität als auch gute Preise."},
            {"en": "The more I shop, the less I save.", "de": "Je mehr ich einkaufe, desto weniger spare ich."},
            {"en": "We need not only milk but also eggs.", "de": "Wir brauchen nicht nur Milch, sondern auch Eier."},
            {"en": "Either we go now or we stay home.", "de": "Entweder gehen wir jetzt, oder wir bleiben zu Hause."},
            {"en": "The bag is neither big nor practical.", "de": "Die Tasche ist weder groß noch praktisch."},
            {"en": "The store sells both food and clothes.", "de": "Der Laden verkauft sowohl Lebensmittel als auch Kleidung."},
            {"en": "The longer you wait, the higher the price.", "de": "Je länger du wartest, desto höher der Preis."},
            {"en": "She is not only friendly but also helpful.", "de": "Sie ist nicht nur freundlich, sondern auch hilfsbereit."},
            {"en": "I will buy either the red or the blue one.", "de": "Ich kaufe entweder das rote oder das blaue."},
            {"en": "He has neither a receipt nor a bag.", "de": "Er hat weder einen Kassenbon noch eine Tüte."},
            {"en": "The market offers both fruit and vegetables.", "de": "Der Markt bietet sowohl Obst als auch Gemüse."},
            {"en": "The fresher the food, the better it tastes.", "de": "Je frischer das Essen, desto besser schmeckt es."},
            {"en": "We buy not only for ourselves but also for friends.", "de": "Wir kaufen nicht nur für uns, sondern auch für Freunde."},
            {"en": "You can either order online or come to the shop.", "de": "Du kannst entweder online bestellen oder in den Laden kommen."},
            {"en": "The shop accepts neither cash nor cards.", "de": "Das Geschäft nimmt weder Bargeld noch Karten."},
            {"en": "The dress is both elegant and comfortable.", "de": "Das Kleid ist sowohl elegant als auch bequem."},
            {"en": "The more you buy, the cheaper it gets.", "de": "Je mehr du kaufst, desto billiger wird es."},
            {"en": "I bought not only shoes but also a belt.", "de": "Ich kaufte nicht nur Schuhe, sondern auch einen Gürtel."},
            {"en": "Either the size or the colour is wrong.", "de": "Entweder die Größe oder die Farbe ist falsch."},
            {"en": "The shop has neither parking nor an elevator.", "de": "Das Geschäft hat weder Parkplätze noch einen Aufzug."},
            {"en": "They sell both online and in stores.", "de": "Sie verkaufen sowohl online als auch in Geschäften."},
            {"en": "The earlier you come, the more you find.", "de": "Je früher du kommst, desto mehr findest du."},
            {"en": "The product is not only cheap but also good.", "de": "Das Produkt ist nicht nur billig, sondern auch gut."},
            {"en": "We can either keep it or return it.", "de": "Wir können es entweder behalten oder zurückgeben."},
            {"en": "She likes neither this nor that.", "de": "Sie mag weder dieses noch jenes."},
            {"en": "The shop is both modern and clean.", "de": "Das Geschäft ist sowohl modern als auch sauber."},
            {"en": "The bigger the discount, the more people buy.", "de": "Je größer der Rabatt, desto mehr Leute kaufen."},
            {"en": "Good shopping is not only about price but also about quality.", "de": "Beim Einkaufen geht es nicht nur um den Preis, sondern auch um die Qualität."},
        ],
    },

    ("B1", "environment"): {
        "note": (
            "📖 Environment — B1\n\n"
            "PURPOSE: damit vs um … zu (+ Passiv review)\n"
            "um … zu + infinitive — when BOTH clauses have the SAME subject:\n"
            "• Wir trennen den Müll, um die Umwelt zu schützen. (we … we)\n"
            "damit + clause (verb to END) — when the subjects are DIFFERENT (or with passive):\n"
            "• Wir trennen den Müll, damit die Umwelt geschützt wird.\n"
            "• Ich erkläre es, damit alle es verstehen.\n"
            "Passive review: werden + Partizip II (present) / wurde + Partizip II (past).\n"
            "• Energie wird gespart.  ·  Der Müll wurde recycelt.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "We separate the rubbish to protect the environment.", "de": "Wir trennen den Müll, um die Umwelt zu schützen."},
            {"en": "We separate the rubbish so that the environment is protected.", "de": "Wir trennen den Müll, damit die Umwelt geschützt wird."},
            {"en": "I explain it so that everyone understands.", "de": "Ich erkläre es, damit alle es verstehen."},
            {"en": "Energy is saved.", "de": "Energie wird gespart."},
            {"en": "The rubbish was recycled.", "de": "Der Müll wurde recycelt."},
            {"en": "We use less water to protect nature.", "de": "Wir verbrauchen weniger Wasser, um die Natur zu schützen."},
            {"en": "We plant trees so that the air stays clean.", "de": "Wir pflanzen Bäume, damit die Luft sauber bleibt."},
            {"en": "The forest must be protected.", "de": "Der Wald muss geschützt werden."},
            {"en": "I switch off the light to save energy.", "de": "Ich schalte das Licht aus, um Energie zu sparen."},
            {"en": "We sort the waste so that it can be recycled.", "de": "Wir sortieren den Abfall, damit er recycelt werden kann."},
            {"en": "Plastic is avoided.", "de": "Plastik wird vermieden."},
            {"en": "The river was cleaned.", "de": "Der Fluss wurde gereinigt."},
            {"en": "We act now so that our children have a future.", "de": "Wir handeln jetzt, damit unsere Kinder eine Zukunft haben."},
            {"en": "I take the bus to reduce pollution.", "de": "Ich nehme den Bus, um die Umweltverschmutzung zu reduzieren."},
            {"en": "The streets are cleaned every morning.", "de": "Die Straßen werden jeden Morgen gereinigt."},
            {"en": "We save water so that there is enough for everyone.", "de": "Wir sparen Wasser, damit es für alle reicht."},
            {"en": "Solar energy is used more and more.", "de": "Solarenergie wird immer mehr genutzt."},
            {"en": "We recycle paper to save trees.", "de": "Wir recyceln Papier, um Bäume zu retten."},
            {"en": "The law was changed so that companies pollute less.", "de": "Das Gesetz wurde geändert, damit die Firmen weniger verschmutzen."},
            {"en": "The waste is collected on Mondays.", "de": "Der Müll wird montags gesammelt."},
            {"en": "We turn off devices so that less energy is wasted.", "de": "Wir schalten Geräte aus, damit weniger Energie verschwendet wird."},
            {"en": "The beach was cleaned by volunteers.", "de": "Der Strand wurde von Freiwilligen gereinigt."},
            {"en": "We buy local products to support the region.", "de": "Wir kaufen lokale Produkte, um die Region zu unterstützen."},
            {"en": "The air is tested regularly.", "de": "Die Luft wird regelmäßig getestet."},
            {"en": "We explain the problem so that people understand it.", "de": "Wir erklären das Problem, damit die Leute es verstehen."},
            {"en": "Many trees were planted last year.", "de": "Letztes Jahr wurden viele Bäume gepflanzt."},
            {"en": "I cycle to work to stay healthy.", "de": "Ich fahre mit dem Rad zur Arbeit, um gesund zu bleiben."},
            {"en": "The rules were made so that nature is protected.", "de": "Die Regeln wurden gemacht, damit die Natur geschützt wird."},
            {"en": "Clean energy is produced here.", "de": "Hier wird saubere Energie produziert."},
            {"en": "We reduce plastic so that the oceans stay clean.", "de": "Wir reduzieren Plastik, damit die Meere sauber bleiben."},
            {"en": "The garden was watered in the evening.", "de": "Der Garten wurde am Abend gegossen."},
            {"en": "We save paper to protect the forest.", "de": "Wir sparen Papier, um den Wald zu schützen."},
            {"en": "The bottles are collected and reused.", "de": "Die Flaschen werden gesammelt und wiederverwendet."},
            {"en": "We inform people so that they recycle correctly.", "de": "Wir informieren die Leute, damit sie richtig recyceln."},
            {"en": "The pollution was reduced.", "de": "Die Verschmutzung wurde reduziert."},
            {"en": "We use public transport to save fuel.", "de": "Wir benutzen öffentliche Verkehrsmittel, um Treibstoff zu sparen."},
            {"en": "The animals are protected by law.", "de": "Die Tiere werden durch das Gesetz geschützt."},
            {"en": "We plant flowers so that the bees find food.", "de": "Wir pflanzen Blumen, damit die Bienen Futter finden."},
            {"en": "The energy is produced from wind and sun.", "de": "Die Energie wird aus Wind und Sonne erzeugt."},
            {"en": "We all must act so that the planet is saved.", "de": "Wir müssen alle handeln, damit der Planet gerettet wird."},
        ],
    },

    ("B1", "advertising"): {
        "note": (
            "📖 Advertising — B1\n\n"
            "CONNECTORS of CONSEQUENCE (therefore / so that)\n"
            "ADVERBS (verb in position 2, subject after): deshalb, deswegen, darum, daher, folglich.\n"
            "• Das Angebot ist gut, deshalb kaufen viele Leute.\n"
            "SUBORDINATING: sodass / so dass (so that, as a result) — verb to the END:\n"
            "• Der Preis ist niedrig, sodass jeder es sich leisten kann.\n"
            "Also: so + adjective + dass (so … that):\n"
            "• Das Produkt ist so beliebt, dass es schnell ausverkauft ist.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "The offer is good, therefore many people buy.", "de": "Das Angebot ist gut, deshalb kaufen viele Leute."},
            {"en": "The price is low, so that everyone can afford it.", "de": "Der Preis ist niedrig, sodass jeder es sich leisten kann."},
            {"en": "The product is so popular that it is quickly sold out.", "de": "Das Produkt ist so beliebt, dass es schnell ausverkauft ist."},
            {"en": "The brand is famous, therefore it sells well.", "de": "Die Marke ist berühmt, deshalb verkauft sie sich gut."},
            {"en": "The quality is high, therefore the price is too.", "de": "Die Qualität ist hoch, deswegen ist der Preis es auch."},
            {"en": "We lowered the price, so that more people buy.", "de": "Wir haben den Preis gesenkt, sodass mehr Leute kaufen."},
            {"en": "The ad was clever, therefore everyone remembers it.", "de": "Die Werbung war clever, deshalb erinnert sich jeder daran."},
            {"en": "The shop is popular, therefore it is always full.", "de": "Der Laden ist beliebt, daher ist er immer voll."},
            {"en": "The discount is big, so that customers come quickly.", "de": "Der Rabatt ist groß, sodass die Kunden schnell kommen."},
            {"en": "The product is so cheap that everyone wants it.", "de": "Das Produkt ist so billig, dass es jeder haben will."},
            {"en": "The campaign was successful, therefore sales rose.", "de": "Die Kampagne war erfolgreich, deshalb stiegen die Verkäufe."},
            {"en": "We use bright colours, so that the ad stands out.", "de": "Wir benutzen helle Farben, sodass die Werbung auffällt."},
            {"en": "The slogan is catchy, therefore people repeat it.", "de": "Der Slogan ist einprägsam, deshalb wiederholen ihn die Leute."},
            {"en": "The service is excellent, therefore customers return.", "de": "Der Service ist ausgezeichnet, daher kommen die Kunden wieder."},
            {"en": "The offer ends soon, therefore you should hurry.", "de": "Das Angebot endet bald, deshalb solltest du dich beeilen."},
            {"en": "The product is so good that it sells itself.", "de": "Das Produkt ist so gut, dass es sich von selbst verkauft."},
            {"en": "We advertise online, so that more people see it.", "de": "Wir werben online, sodass mehr Leute es sehen."},
            {"en": "The brand is trusted, therefore people recommend it.", "de": "Der Marke wird vertraut, deshalb empfehlen sie die Leute."},
            {"en": "The price dropped, therefore demand increased.", "de": "Der Preis fiel, deswegen stieg die Nachfrage."},
            {"en": "The packaging is attractive, so that it catches the eye.", "de": "Die Verpackung ist attraktiv, sodass sie ins Auge fällt."},
            {"en": "The ad was funny, therefore it became popular.", "de": "Die Werbung war lustig, deshalb wurde sie beliebt."},
            {"en": "The product is new, therefore everyone is curious.", "de": "Das Produkt ist neu, daher sind alle neugierig."},
            {"en": "The shop offers free delivery, so that people order more.", "de": "Der Laden bietet kostenlose Lieferung, sodass die Leute mehr bestellen."},
            {"en": "The deal is so attractive that it spreads quickly.", "de": "Das Angebot ist so attraktiv, dass es sich schnell verbreitet."},
            {"en": "We changed the design, therefore sales improved.", "de": "Wir haben das Design geändert, deshalb verbesserten sich die Verkäufe."},
            {"en": "The brand is everywhere, therefore everyone knows it.", "de": "Die Marke ist überall, deshalb kennt sie jeder."},
            {"en": "The reviews are good, therefore customers trust the shop.", "de": "Die Bewertungen sind gut, daher vertrauen die Kunden dem Laden."},
            {"en": "The offer is limited, so that buyers act fast.", "de": "Das Angebot ist begrenzt, sodass die Käufer schnell handeln."},
            {"en": "The price is fair, therefore people come back.", "de": "Der Preis ist fair, deshalb kommen die Leute wieder."},
            {"en": "The product is so useful that everyone needs it.", "de": "Das Produkt ist so nützlich, dass es jeder braucht."},
            {"en": "We posted the ad on social media, therefore it went viral.", "de": "Wir haben die Werbung in den sozialen Medien gepostet, deshalb ging sie viral."},
            {"en": "The store looks modern, so that customers feel welcome.", "de": "Das Geschäft sieht modern aus, sodass sich die Kunden wohlfühlen."},
            {"en": "The product won an award, therefore it became famous.", "de": "Das Produkt gewann einen Preis, deshalb wurde es berühmt."},
            {"en": "The sale starts tomorrow, therefore people are waiting.", "de": "Der Verkauf beginnt morgen, daher warten die Leute."},
            {"en": "The quality improved, therefore the brand grew.", "de": "Die Qualität verbesserte sich, deshalb wuchs die Marke."},
            {"en": "The ad is everywhere, so that nobody can miss it.", "de": "Die Werbung ist überall, sodass sie niemand übersehen kann."},
            {"en": "The product is rare, therefore it is expensive.", "de": "Das Produkt ist selten, deshalb ist es teuer."},
            {"en": "The shop gives discounts, so that customers stay loyal.", "de": "Der Laden gibt Rabatte, sodass die Kunden treu bleiben."},
            {"en": "The campaign was clever, therefore it worked.", "de": "Die Kampagne war clever, deshalb funktionierte sie."},
            {"en": "Good advertising is honest, therefore people trust it.", "de": "Gute Werbung ist ehrlich, deshalb vertrauen ihr die Leute."},
        ],
    },

    ("B1", "government"): {
        "note": (
            "📖 Government and Society — B1\n\n"
            "REPORTED SPEECH — Konjunktiv I (indirekte Rede)\n"
            "News and official reports use Konjunktiv I to repeat what someone said neutrally.\n"
            "Common 3rd-person forms: sein → sei · haben → habe · können → könne · "
            "werden → werde · regular verbs → -e (er sage, er komme).\n"
            "• Direct: Ich bin krank. → Er sagt, er sei krank.\n"
            "• Direct: Wir haben keine Zeit. → Sie sagen, sie hätten keine Zeit.\n"
            "(When Konjunktiv I looks like the present, switch to Konjunktiv II: hätten, not haben.)\n"
            "Introduced by: Er sagt/behauptet/erklärt, dass … (or without dass, verb in pos. 2).\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "He says he is ill.", "de": "Er sagt, er sei krank."},
            {"en": "She says she has no time.", "de": "Sie sagt, sie habe keine Zeit."},
            {"en": "They say they cannot come.", "de": "Sie sagen, sie könnten nicht kommen."},
            {"en": "The minister says the law is new.", "de": "Der Minister sagt, das Gesetz sei neu."},
            {"en": "He claims he knows nothing.", "de": "Er behauptet, er wisse nichts."},
            {"en": "She says she will come tomorrow.", "de": "Sie sagt, sie werde morgen kommen."},
            {"en": "The president says the country is safe.", "de": "Der Präsident sagt, das Land sei sicher."},
            {"en": "They say they have no money.", "de": "Sie sagen, sie hätten kein Geld."},
            {"en": "He explains that the office is closed.", "de": "Er erklärt, das Amt sei geschlossen."},
            {"en": "She says she lives in Berlin.", "de": "Sie sagt, sie wohne in Berlin."},
            {"en": "The report says the economy is growing.", "de": "Der Bericht sagt, die Wirtschaft wachse."},
            {"en": "He says he needs the documents.", "de": "Er sagt, er brauche die Dokumente."},
            {"en": "They claim they are innocent.", "de": "Sie behaupten, sie seien unschuldig."},
            {"en": "She says she can help.", "de": "Sie sagt, sie könne helfen."},
            {"en": "The official says the form is ready.", "de": "Der Beamte sagt, das Formular sei fertig."},
            {"en": "He says the taxes are too high.", "de": "Er sagt, die Steuern seien zu hoch."},
            {"en": "She explains that she has signed it.", "de": "Sie erklärt, sie habe es unterschrieben."},
            {"en": "They say they will vote.", "de": "Sie sagen, sie würden wählen."},
            {"en": "The chancellor says she is optimistic.", "de": "Die Kanzlerin sagt, sie sei optimistisch."},
            {"en": "He claims he has paid.", "de": "Er behauptet, er habe bezahlt."},
            {"en": "She says the meeting starts at ten.", "de": "Sie sagt, das Treffen beginne um zehn."},
            {"en": "They say the situation is difficult.", "de": "Sie sagen, die Lage sei schwierig."},
            {"en": "He says he wants to register.", "de": "Er sagt, er wolle sich anmelden."},
            {"en": "The newspaper reports that prices are rising.", "de": "Die Zeitung berichtet, die Preise stiegen."},
            {"en": "She says she does not understand the rule.", "de": "Sie sagt, sie verstehe die Regel nicht."},
            {"en": "He says he has lost his passport.", "de": "Er sagt, er habe seinen Pass verloren."},
            {"en": "They claim they were not informed.", "de": "Sie behaupten, sie seien nicht informiert worden."},
            {"en": "She says she must work tomorrow.", "de": "Sie sagt, sie müsse morgen arbeiten."},
            {"en": "The official says the decision is final.", "de": "Der Beamte sagt, die Entscheidung sei endgültig."},
            {"en": "He says he is a citizen of this country.", "de": "Er sagt, er sei Bürger dieses Landes."},
            {"en": "She explains that the law has changed.", "de": "Sie erklärt, das Gesetz habe sich geändert."},
            {"en": "They say they will help us.", "de": "Sie sagen, sie würden uns helfen."},
            {"en": "He says he cannot find the office.", "de": "Er sagt, er könne das Amt nicht finden."},
            {"en": "The report says unemployment is falling.", "de": "Der Bericht sagt, die Arbeitslosigkeit sinke."},
            {"en": "She says she has an appointment.", "de": "Sie sagt, sie habe einen Termin."},
            {"en": "He claims the rules are unfair.", "de": "Er behauptet, die Regeln seien ungerecht."},
            {"en": "She says she will send the form.", "de": "Sie sagt, sie werde das Formular schicken."},
            {"en": "They say they trust the government.", "de": "Sie sagen, sie vertrauten der Regierung."},
            {"en": "He says everything is in order.", "de": "Er sagt, alles sei in Ordnung."},
            {"en": "A good leader says what he means and means what he says.", "de": "Ein guter Politiker sagt, was er meine, und meint, was er sage."},
        ],
    },

    ("B2", "greeting"): {
        "note": (
            "📖 Greeting — B2\n\n"
            "FUNCTION-VERB CONSTRUCTIONS (Funktionsverbgefüge)\n"
            "Formal German often replaces a simple verb with noun + a light verb. "
            "The meaning sits in the noun; the verb carries the grammar.\n"
            "  eine Frage stellen (ask) · eine Entscheidung treffen (decide) · "
            "Abschied nehmen (say goodbye) · Hilfe leisten (help) · "
            "in Betracht ziehen (consider) · in Kontakt treten (get in touch) · "
            "zur Verfügung stehen (be available) · in Kraft treten (come into force) · "
            "Bezug nehmen auf (refer to) · Wert legen auf (attach importance to).\n"
            "• Darf ich Ihnen eine Frage stellen?  ·  Wir nehmen Bezug auf Ihr Schreiben.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "May I ask you a question?", "de": "Darf ich Ihnen eine Frage stellen?"},
            {"en": "We refer to your letter.", "de": "Wir nehmen Bezug auf Ihr Schreiben."},
            {"en": "She gave a clear answer.", "de": "Sie gab eine klare Antwort."},
            {"en": "We made a decision.", "de": "Wir haben eine Entscheidung getroffen."},
            {"en": "He took his leave politely.", "de": "Er nahm höflich Abschied."},
            {"en": "They offered help.", "de": "Sie leisteten Hilfe."},
            {"en": "I would like to get in contact with you.", "de": "Ich möchte mit Ihnen in Kontakt treten."},
            {"en": "We will take your wish into consideration.", "de": "Wir werden Ihren Wunsch in Betracht ziehen."},
            {"en": "I am at your disposal.", "de": "Ich stehe Ihnen zur Verfügung."},
            {"en": "The new law comes into force tomorrow.", "de": "Das neue Gesetz tritt morgen in Kraft."},
            {"en": "Please take a seat.", "de": "Nehmen Sie bitte Platz."},
            {"en": "He made an important suggestion.", "de": "Er machte einen wichtigen Vorschlag."},
            {"en": "We came to an agreement.", "de": "Wir kamen zu einer Einigung."},
            {"en": "She paid attention to the details.", "de": "Sie schenkte den Details Aufmerksamkeit."},
            {"en": "I would like to express my thanks.", "de": "Ich möchte meinen Dank aussprechen."},
            {"en": "We have taken note of your concern.", "de": "Wir haben Ihr Anliegen zur Kenntnis genommen."},
            {"en": "He took responsibility for the mistake.", "de": "Er übernahm die Verantwortung für den Fehler."},
            {"en": "They reached an agreement quickly.", "de": "Sie erzielten schnell eine Einigung."},
            {"en": "We would like to make you an offer.", "de": "Wir möchten Ihnen ein Angebot machen."},
            {"en": "Please get in touch with us.", "de": "Bitte nehmen Sie Kontakt mit uns auf."},
            {"en": "I take your criticism seriously.", "de": "Ich nehme Ihre Kritik ernst."},
            {"en": "The company is making an effort.", "de": "Das Unternehmen unternimmt Anstrengungen."},
            {"en": "We will keep you informed.", "de": "Wir halten Sie auf dem Laufenden."},
            {"en": "He drew attention to the problem.", "de": "Er machte auf das Problem aufmerksam."},
            {"en": "Allow me to introduce myself.", "de": "Erlauben Sie mir, mich vorzustellen."},
            {"en": "We attach great importance to quality.", "de": "Wir legen großen Wert auf Qualität."},
            {"en": "They took the matter into their own hands.", "de": "Sie nahmen die Sache selbst in die Hand."},
            {"en": "I would like to make a request.", "de": "Ich möchte eine Bitte äußern."},
            {"en": "We are taking measures.", "de": "Wir ergreifen Maßnahmen."},
            {"en": "He came to a conclusion.", "de": "Er kam zu einem Schluss."},
            {"en": "She expressed her opinion.", "de": "Sie brachte ihre Meinung zum Ausdruck."},
            {"en": "We will give the matter our attention.", "de": "Wir werden der Sache unsere Aufmerksamkeit widmen."},
            {"en": "Please accept my apologies.", "de": "Bitte nehmen Sie meine Entschuldigung an."},
            {"en": "The decision was put into practice.", "de": "Die Entscheidung wurde in die Tat umgesetzt."},
            {"en": "We are in close contact.", "de": "Wir stehen in engem Kontakt."},
            {"en": "He raised an objection.", "de": "Er erhob Einspruch."},
            {"en": "I have come to a decision.", "de": "Ich bin zu einer Entscheidung gekommen."},
            {"en": "They placed an order.", "de": "Sie gaben eine Bestellung auf."},
            {"en": "We take your needs into account.", "de": "Wir berücksichtigen Ihre Bedürfnisse."},
            {"en": "A good conversation builds a bridge between people.", "de": "Ein gutes Gespräch schlägt eine Brücke zwischen Menschen."},
        ],
    },

    ("B2", "holiday"): {
        "note": (
            "📖 Holiday — B2\n\n"
            "EXTENDED PARTICIPLE ATTRIBUTES (erweiterte Partizipialattribute)\n"
            "A whole phrase can sit between the article and the noun, built around a participle. "
            "Typical of written German; speech prefers a relative clause.\n"
            "  der im Sommer gebuchte Urlaub (= der Urlaub, der im Sommer gebucht wurde)\n"
            "Partizip II (passive/done): die gestern angekommenen Gäste.\n"
            "Partizip I (active/ongoing): die am Strand spielenden Kinder.\n"
            "Partizip I + zu (necessity): die noch zu buchende Reise (still to be booked).\n"
            "The participle takes the normal adjective ending for its case.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "The holiday booked in summer was great.", "de": "Der im Sommer gebuchte Urlaub war toll."},
            {"en": "The guests who arrived yesterday are tired.", "de": "Die gestern angekommenen Gäste sind müde."},
            {"en": "The children playing on the beach are happy.", "de": "Die am Strand spielenden Kinder sind glücklich."},
            {"en": "The trip that still has to be booked is expensive.", "de": "Die noch zu buchende Reise ist teuer."},
            {"en": "The hotel recommended by friends was perfect.", "de": "Das von Freunden empfohlene Hotel war perfekt."},
            {"en": "The flight delayed by the storm landed late.", "de": "Der vom Sturm verspätete Flug landete spät."},
            {"en": "The case I packed yesterday is heavy.", "de": "Der gestern gepackte Koffer ist schwer."},
            {"en": "The map printed last week is outdated.", "de": "Die letzte Woche gedruckte Karte ist veraltet."},
            {"en": "The tourists waiting at the airport were nervous.", "de": "Die am Flughafen wartenden Touristen waren nervös."},
            {"en": "The room booked online was small.", "de": "Das online gebuchte Zimmer war klein."},
            {"en": "The beach surrounded by palm trees is beautiful.", "de": "Der von Palmen umgebene Strand ist schön."},
            {"en": "The photos taken on holiday are wonderful.", "de": "Die im Urlaub gemachten Fotos sind wunderbar."},
            {"en": "The bus leaving in ten minutes is full.", "de": "Der in zehn Minuten abfahrende Bus ist voll."},
            {"en": "The luggage left on the train was lost.", "de": "Das im Zug zurückgelassene Gepäck ging verloren."},
            {"en": "The city visited by millions is famous.", "de": "Die von Millionen besuchte Stadt ist berühmt."},
            {"en": "The mountain covered in snow looked majestic.", "de": "Der mit Schnee bedeckte Berg sah majestätisch aus."},
            {"en": "The restaurant praised in the guide was full.", "de": "Das im Reiseführer gelobte Restaurant war voll."},
            {"en": "The island discovered long ago is now a resort.", "de": "Die vor langer Zeit entdeckte Insel ist heute ein Ferienort."},
            {"en": "The path leading to the sea is steep.", "de": "Der zum Meer führende Weg ist steil."},
            {"en": "The ticket bought in advance was cheaper.", "de": "Die im Voraus gekaufte Karte war billiger."},
            {"en": "The travelers arriving late missed dinner.", "de": "Die spät ankommenden Reisenden verpassten das Abendessen."},
            {"en": "The village hidden in the mountains is quiet.", "de": "Das in den Bergen versteckte Dorf ist ruhig."},
            {"en": "The lake reflecting the sky was calm.", "de": "Der den Himmel spiegelnde See war ruhig."},
            {"en": "The plan made months ago worked well.", "de": "Der vor Monaten gemachte Plan funktionierte gut."},
            {"en": "The guide explaining the history was excellent.", "de": "Der die Geschichte erklärende Führer war ausgezeichnet."},
            {"en": "The hotel built last year is modern.", "de": "Das letztes Jahr gebaute Hotel ist modern."},
            {"en": "The route still to be planned is long.", "de": "Die noch zu planende Route ist lang."},
            {"en": "The car rented at the airport broke down.", "de": "Das am Flughafen gemietete Auto hatte eine Panne."},
            {"en": "The festival held every summer attracts crowds.", "de": "Das jeden Sommer stattfindende Festival zieht Menschenmengen an."},
            {"en": "The food served at the hotel was delicious.", "de": "Das im Hotel servierte Essen war lecker."},
            {"en": "The bridge built in the old town is famous.", "de": "Die in der Altstadt gebaute Brücke ist berühmt."},
            {"en": "The picture hanging in the lobby is valuable.", "de": "Das in der Lobby hängende Bild ist wertvoll."},
            {"en": "The travelers exhausted by the journey slept.", "de": "Die von der Reise erschöpften Reisenden schliefen."},
            {"en": "The beach cleaned every morning is spotless.", "de": "Der jeden Morgen gereinigte Strand ist makellos."},
            {"en": "The story told by the guide was fascinating.", "de": "Die vom Führer erzählte Geschichte war faszinierend."},
            {"en": "The tickets still to be paid are reserved.", "de": "Die noch zu bezahlenden Karten sind reserviert."},
            {"en": "The garden surrounding the hotel is huge.", "de": "Der das Hotel umgebende Garten ist riesig."},
            {"en": "The plane arriving from Rome is delayed.", "de": "Das aus Rom ankommende Flugzeug hat Verspätung."},
            {"en": "The memories made on this trip will last.", "de": "Die auf dieser Reise gemachten Erinnerungen bleiben."},
            {"en": "A journey carefully planned is half enjoyed.", "de": "Eine sorgfältig geplante Reise ist halb genossen."},
        ],
    },

    ("B2", "relationship"): {
        "note": (
            "📖 Relationship — B2\n\n"
            "UNREAL COMPARISONS — als ob / als wenn + Konjunktiv\n"
            "To say something seems a certain way (but isn't), use tun/aussehen, als ob …\n"
            "The verb in the als-ob-clause goes to the END, in Konjunktiv II.\n"
            "• Er tut, als ob er mich nicht kennen würde.\n"
            "• Sie sieht aus, als ob sie geweint hätte.\n"
            "SHORT form with just als (verb comes RIGHT AFTER als):\n"
            "• Er tut, als kennte er mich nicht.\n"
            "• Sie sieht aus, als hätte sie geweint.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "He acts as if he didn't know me.", "de": "Er tut, als ob er mich nicht kennen würde."},
            {"en": "She looks as if she had cried.", "de": "Sie sieht aus, als ob sie geweint hätte."},
            {"en": "He acts as if he were rich.", "de": "Er tut, als ob er reich wäre."},
            {"en": "She behaves as if nothing had happened.", "de": "Sie tut, als ob nichts passiert wäre."},
            {"en": "He talks as if he knew everything.", "de": "Er redet, als ob er alles wüsste."},
            {"en": "It seems as if they were in love.", "de": "Es scheint, als ob sie verliebt wären."},
            {"en": "You look as if you were tired.", "de": "Du siehst aus, als ob du müde wärst."},
            {"en": "He smiles as if he were happy.", "de": "Er lächelt, als ob er glücklich wäre."},
            {"en": "She acts as if she didn't care.", "de": "Sie tut, als ob es ihr egal wäre."},
            {"en": "He looks as if he hadn't slept.", "de": "Er sieht aus, als hätte er nicht geschlafen."},
            {"en": "They behave as if they were a couple.", "de": "Sie benehmen sich, als ob sie ein Paar wären."},
            {"en": "He speaks as if he had been there.", "de": "Er spricht, als ob er dort gewesen wäre."},
            {"en": "She acts as if she understood me.", "de": "Sie tut, als ob sie mich verstehen würde."},
            {"en": "It feels as if we had known each other for years.", "de": "Es fühlt sich an, als ob wir uns seit Jahren kennen würden."},
            {"en": "He looks as if he had seen a ghost.", "de": "Er sieht aus, als hätte er einen Geist gesehen."},
            {"en": "She acts as if she were my friend.", "de": "Sie tut, als wäre sie meine Freundin."},
            {"en": "He behaves as if he owned the place.", "de": "Er benimmt sich, als ob ihm der Laden gehören würde."},
            {"en": "You speak as if you knew her well.", "de": "Du redest, als ob du sie gut kennen würdest."},
            {"en": "He acts as if he had forgotten me.", "de": "Er tut, als ob er mich vergessen hätte."},
            {"en": "She looks as if she were about to cry.", "de": "Sie sieht aus, als ob sie gleich weinen würde."},
            {"en": "It sounds as if you were angry.", "de": "Es klingt, als ob du wütend wärst."},
            {"en": "He pretends as if he were listening.", "de": "Er tut so, als ob er zuhören würde."},
            {"en": "She acts as if she had won.", "de": "Sie tut, als hätte sie gewonnen."},
            {"en": "They look as if they had argued.", "de": "Sie sehen aus, als ob sie sich gestritten hätten."},
            {"en": "He behaves as if he were the boss.", "de": "Er benimmt sich, als wäre er der Chef."},
            {"en": "She talks as if she had read the book.", "de": "Sie redet, als ob sie das Buch gelesen hätte."},
            {"en": "It seems as if he didn't want to come.", "de": "Es scheint, als ob er nicht kommen wollte."},
            {"en": "You act as if you didn't believe me.", "de": "Du tust, als ob du mir nicht glauben würdest."},
            {"en": "He smiles as if everything were fine.", "de": "Er lächelt, als ob alles in Ordnung wäre."},
            {"en": "She looks as if she were waiting for someone.", "de": "Sie sieht aus, als ob sie auf jemanden warten würde."},
            {"en": "He acts as if we had never met.", "de": "Er tut, als ob wir uns nie getroffen hätten."},
            {"en": "It feels as if time had stopped.", "de": "Es fühlt sich an, als ob die Zeit stehen geblieben wäre."},
            {"en": "She behaves as if she were younger.", "de": "Sie benimmt sich, als ob sie jünger wäre."},
            {"en": "He speaks as if he had all the answers.", "de": "Er spricht, als hätte er alle Antworten."},
            {"en": "You look as if you had good news.", "de": "Du siehst aus, als ob du gute Nachrichten hättest."},
            {"en": "He acts as if he didn't hear me.", "de": "Er tut, als ob er mich nicht hören würde."},
            {"en": "She looks as if she were in love.", "de": "Sie sieht aus, als ob sie verliebt wäre."},
            {"en": "It seems as if they had made up.", "de": "Es scheint, als ob sie sich versöhnt hätten."},
            {"en": "He behaves as if he had done nothing wrong.", "de": "Er benimmt sich, als hätte er nichts falsch gemacht."},
            {"en": "Sometimes love feels as if it had always been there.", "de": "Manchmal fühlt sich Liebe an, als wäre sie immer da gewesen."},
        ],
    },

    ("B2", "technology"): {
        "note": (
            "📖 Technology — B2\n\n"
            "PASSIVE ALTERNATIVES (Passiversatzformen)\n"
            "German often expresses passive meaning WITHOUT werden:\n"
            "1) man + active verb: Man repariert das Gerät.\n"
            "2) sich lassen + infinitive (= can be done): Das Problem lässt sich lösen.\n"
            "3) sein + zu + infinitive (= must/can be done): Die Aufgabe ist zu erledigen.\n"
            "4) adjective on -bar / -lich (= -able): reparierbar, machbar, lösbar.\n"
            "• Diese App lässt sich leicht bedienen.  ·  Das Update ist sofort zu installieren.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "The problem can be solved.", "de": "Das Problem lässt sich lösen."},
            {"en": "The task must be done.", "de": "Die Aufgabe ist zu erledigen."},
            {"en": "The device is repairable.", "de": "Das Gerät ist reparierbar."},
            {"en": "This app is easy to use.", "de": "Diese App lässt sich leicht bedienen."},
            {"en": "The update must be installed immediately.", "de": "Das Update ist sofort zu installieren."},
            {"en": "The file can be opened.", "de": "Die Datei lässt sich öffnen."},
            {"en": "The data must be saved.", "de": "Die Daten sind zu speichern."},
            {"en": "The error is fixable.", "de": "Der Fehler ist behebbar."},
            {"en": "You can repair the phone.", "de": "Man kann das Handy reparieren."},
            {"en": "The password cannot be changed.", "de": "Das Passwort lässt sich nicht ändern."},
            {"en": "The instructions are easy to understand.", "de": "Die Anleitung ist leicht zu verstehen."},
            {"en": "The software is downloadable.", "de": "Die Software ist herunterladbar."},
            {"en": "The machine can be controlled remotely.", "de": "Die Maschine lässt sich aus der Ferne steuern."},
            {"en": "The settings must be checked.", "de": "Die Einstellungen sind zu überprüfen."},
            {"en": "The screen is replaceable.", "de": "Der Bildschirm ist austauschbar."},
            {"en": "The text can be translated easily.", "de": "Der Text lässt sich leicht übersetzen."},
            {"en": "The form must be filled out.", "de": "Das Formular ist auszufüllen."},
            {"en": "The result is predictable.", "de": "Das Ergebnis ist vorhersehbar."},
            {"en": "You cannot recover the lost data.", "de": "Man kann die verlorenen Daten nicht wiederherstellen."},
            {"en": "The system can be updated automatically.", "de": "Das System lässt sich automatisch aktualisieren."},
            {"en": "The rules are to be followed.", "de": "Die Regeln sind zu befolgen."},
            {"en": "The product is recyclable.", "de": "Das Produkt ist recycelbar."},
            {"en": "The mistake can hardly be avoided.", "de": "Der Fehler lässt sich kaum vermeiden."},
            {"en": "The document must be signed.", "de": "Das Dokument ist zu unterschreiben."},
            {"en": "The plan is feasible.", "de": "Der Plan ist machbar."},
            {"en": "The battery can be charged quickly.", "de": "Der Akku lässt sich schnell laden."},
            {"en": "The question is not easy to answer.", "de": "Die Frage ist nicht leicht zu beantworten."},
            {"en": "The app is freely available.", "de": "Die App ist frei verfügbar."},
            {"en": "The connection cannot be established.", "de": "Die Verbindung lässt sich nicht herstellen."},
            {"en": "The deadline must be met.", "de": "Die Frist ist einzuhalten."},
            {"en": "The problem is unsolvable.", "de": "Das Problem ist unlösbar."},
            {"en": "The program can be installed in minutes.", "de": "Das Programm lässt sich in Minuten installieren."},
            {"en": "The contract is to be read carefully.", "de": "Der Vertrag ist sorgfältig zu lesen."},
            {"en": "The damage is repairable.", "de": "Der Schaden ist reparierbar."},
            {"en": "The photos can be shared easily.", "de": "Die Fotos lassen sich leicht teilen."},
            {"en": "The risk must be considered.", "de": "Das Risiko ist zu berücksichtigen."},
            {"en": "The result is measurable.", "de": "Das Ergebnis ist messbar."},
            {"en": "The data can be analyzed quickly.", "de": "Die Daten lassen sich schnell analysieren."},
            {"en": "The instructions are to be observed.", "de": "Die Hinweise sind zu beachten."},
            {"en": "A good system is one that anyone can use.", "de": "Ein gutes System ist eines, das sich von jedem bedienen lässt."},
        ],
    },

    ("B2", "sports"): {
        "note": (
            "📖 Sports — B2\n\n"
            "STATE PASSIVE (Zustandspassiv) vs PROCESS PASSIVE (Vorgangspassiv)\n"
            "PROCESS passive (werden) = the action happening:\n"
            "  Das Spiel wird beendet. → The game is being ended.\n"
            "STATE passive (sein) = the RESULT/state after the action:\n"
            "  Das Spiel ist beendet. → The game is (already) over.\n"
            "Form: sein + Partizip II (a finished condition).\n"
            "• Das Stadion ist gebaut. (stands, finished)  vs  Das Stadion wird gebaut. (in progress)\n"
            "Past state passive: war + Partizip II → Das Spiel war beendet.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "The game is over.", "de": "Das Spiel ist beendet."},
            {"en": "The game is being ended.", "de": "Das Spiel wird beendet."},
            {"en": "The stadium is built.", "de": "Das Stadion ist gebaut."},
            {"en": "The stadium is being built.", "de": "Das Stadion wird gebaut."},
            {"en": "The door is closed.", "de": "Die Tür ist geschlossen."},
            {"en": "The match was already finished.", "de": "Das Spiel war schon beendet."},
            {"en": "The field is prepared.", "de": "Der Platz ist vorbereitet."},
            {"en": "The tickets are sold out.", "de": "Die Karten sind ausverkauft."},
            {"en": "The match is decided.", "de": "Das Spiel ist entschieden."},
            {"en": "The players are exhausted.", "de": "Die Spieler sind erschöpft."},
            {"en": "The training is finished.", "de": "Das Training ist beendet."},
            {"en": "The team is well prepared.", "de": "Die Mannschaft ist gut vorbereitet."},
            {"en": "The result is announced.", "de": "Das Ergebnis ist bekannt gegeben."},
            {"en": "The season is over.", "de": "Die Saison ist beendet."},
            {"en": "The injury is healed.", "de": "Die Verletzung ist verheilt."},
            {"en": "The new rules are introduced.", "de": "Die neuen Regeln sind eingeführt."},
            {"en": "The match is being broadcast.", "de": "Das Spiel wird übertragen."},
            {"en": "The trophy is engraved.", "de": "Der Pokal ist graviert."},
            {"en": "The schedule is fixed.", "de": "Der Spielplan ist festgelegt."},
            {"en": "The contract is signed.", "de": "Der Vertrag ist unterschrieben."},
            {"en": "The gym is closed today.", "de": "Das Fitnessstudio ist heute geschlossen."},
            {"en": "The goal is being celebrated.", "de": "Das Tor wird gefeiert."},
            {"en": "The athletes are tested.", "de": "Die Sportler sind getestet."},
            {"en": "The ball is inflated.", "de": "Der Ball ist aufgepumpt."},
            {"en": "The match is cancelled.", "de": "Das Spiel ist abgesagt."},
            {"en": "The match is being cancelled.", "de": "Das Spiel wird abgesagt."},
            {"en": "The records are broken.", "de": "Die Rekorde sind gebrochen."},
            {"en": "The team is motivated.", "de": "Die Mannschaft ist motiviert."},
            {"en": "The medals are handed out.", "de": "Die Medaillen sind verteilt."},
            {"en": "The pitch is freshly mowed.", "de": "Der Rasen ist frisch gemäht."},
            {"en": "The goalkeeper is injured.", "de": "Der Torwart ist verletzt."},
            {"en": "The tournament is organized.", "de": "Das Turnier ist organisiert."},
            {"en": "The lights are switched off.", "de": "Die Lichter sind ausgeschaltet."},
            {"en": "The seats are reserved.", "de": "Die Plätze sind reserviert."},
            {"en": "The decision was already made.", "de": "Die Entscheidung war schon getroffen."},
            {"en": "The training plan is set.", "de": "Der Trainingsplan ist festgelegt."},
            {"en": "The doors are opened.", "de": "Die Türen sind geöffnet."},
            {"en": "The game was lost.", "de": "Das Spiel war verloren."},
            {"en": "The champion is determined.", "de": "Der Meister ist ermittelt."},
            {"en": "When the whistle is blown, the game is over.", "de": "Wenn abgepfiffen wird, ist das Spiel beendet."},
        ],
    },

    ("B2", "food"): {
        "note": (
            "📖 Food — B2\n\n"
            "KONJUNKTIV II — refined wishes & comparisons\n"
            "IRREAL WISH (regret/longing) with doch / bloß / nur:\n"
            "• Hätte ich doch das Dessert probiert! → If only I had tried the dessert!\n"
            "• Wäre ich bloß früher gekommen!\n"
            "IRREAL COMPARISON (als ob) about taste/quality:\n"
            "• Es schmeckt, als ob Salz fehlen würde.\n"
            "POLITE distance & speculation (past Konjunktiv II = hätte/wäre + Partizip II):\n"
            "• An deiner Stelle hätte ich etwas anderes bestellt.\n"
            "• Das hätte besser sein können.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "If only I had tried the dessert!", "de": "Hätte ich doch das Dessert probiert!"},
            {"en": "If only I had come earlier!", "de": "Wäre ich bloß früher gekommen!"},
            {"en": "It tastes as if salt were missing.", "de": "Es schmeckt, als ob Salz fehlen würde."},
            {"en": "In your place I would have ordered something else.", "de": "An deiner Stelle hätte ich etwas anderes bestellt."},
            {"en": "That could have been better.", "de": "Das hätte besser sein können."},
            {"en": "If only the restaurant were still open!", "de": "Wäre das Restaurant doch noch geöffnet!"},
            {"en": "I wish I hadn't eaten so much.", "de": "Ich wünschte, ich hätte nicht so viel gegessen."},
            {"en": "The soup tastes as if it had been warmed up.", "de": "Die Suppe schmeckt, als ob sie aufgewärmt worden wäre."},
            {"en": "We could have booked a table.", "de": "Wir hätten einen Tisch reservieren können."},
            {"en": "If only I had ordered the fish!", "de": "Hätte ich nur den Fisch bestellt!"},
            {"en": "You should have tried the cake.", "de": "Du hättest den Kuchen probieren sollen."},
            {"en": "It looks as if it had been freshly baked.", "de": "Es sieht aus, als ob es frisch gebacken worden wäre."},
            {"en": "I would have preferred to cook at home.", "de": "Ich hätte lieber zu Hause gekocht."},
            {"en": "If only we had reserved earlier!", "de": "Hätten wir doch früher reserviert!"},
            {"en": "The meat tastes as if it were undercooked.", "de": "Das Fleisch schmeckt, als ob es nicht durch wäre."},
            {"en": "He could have paid the bill.", "de": "Er hätte die Rechnung bezahlen können."},
            {"en": "I wish the portions were bigger.", "de": "Ich wünschte, die Portionen wären größer."},
            {"en": "You shouldn't have ordered so much.", "de": "Du hättest nicht so viel bestellen sollen."},
            {"en": "If only the coffee weren't so bitter!", "de": "Wäre der Kaffee doch nicht so bitter!"},
            {"en": "We would have stayed longer if the food had been better.", "de": "Wir wären länger geblieben, wenn das Essen besser gewesen wäre."},
            {"en": "It smells as if something were burning.", "de": "Es riecht, als ob etwas anbrennen würde."},
            {"en": "I would have recommended the soup.", "de": "Ich hätte die Suppe empfohlen."},
            {"en": "If only I had saved room for dessert!", "de": "Hätte ich doch Platz für den Nachtisch gelassen!"},
            {"en": "The wine tastes as if it had gone bad.", "de": "Der Wein schmeckt, als ob er schlecht geworden wäre."},
            {"en": "She could have chosen a vegetarian dish.", "de": "Sie hätte ein vegetarisches Gericht wählen können."},
            {"en": "I wish I had made a reservation.", "de": "Ich wünschte, ich hätte reserviert."},
            {"en": "You should have tasted it first.", "de": "Du hättest es zuerst probieren sollen."},
            {"en": "If only the service had been faster!", "de": "Wäre der Service doch schneller gewesen!"},
            {"en": "The cake looks as if it had collapsed.", "de": "Der Kuchen sieht aus, als ob er zusammengefallen wäre."},
            {"en": "We could have shared a dessert.", "de": "Wir hätten uns einen Nachtisch teilen können."},
            {"en": "I would have enjoyed it more without the noise.", "de": "Ohne den Lärm hätte ich es mehr genossen."},
            {"en": "If only I had brought more cash!", "de": "Hätte ich doch mehr Bargeld dabei gehabt!"},
            {"en": "The dish tastes as if it had no seasoning.", "de": "Das Gericht schmeckt, als ob es keine Würze hätte."},
            {"en": "He should have asked about the ingredients.", "de": "Er hätte nach den Zutaten fragen sollen."},
            {"en": "I wish the kitchen were still open.", "de": "Ich wünschte, die Küche wäre noch offen."},
            {"en": "We would have ordered more if we had been hungrier.", "de": "Wir hätten mehr bestellt, wenn wir hungriger gewesen wären."},
            {"en": "It tastes as if too much sugar had been added.", "de": "Es schmeckt, als ob zu viel Zucker hinzugefügt worden wäre."},
            {"en": "You could have warned me about the spice.", "de": "Du hättest mich vor der Schärfe warnen können."},
            {"en": "If only we had discovered this place sooner!", "de": "Hätten wir diesen Ort doch früher entdeckt!"},
            {"en": "A good meal shared with friends could not be better.", "de": "Ein gutes Essen mit Freunden könnte nicht besser sein."},
        ],
    },

    ("B2", "education"): {
        "note": (
            "📖 Education — B2\n\n"
            "NOMINAL STYLE (Nominalisierung)\n"
            "Formal/academic German turns verbs and clauses into NOUNS with prepositions.\n"
            "  VERBAL: Während ich lese, mache ich Notizen.\n"
            "  NOMINAL: Beim Lesen mache ich Notizen.\n"
            "  VERBAL: Nachdem er die Prüfung bestanden hatte, feierte er.\n"
            "  NOMINAL: Nach dem Bestehen der Prüfung feierte er.\n"
            "Conversions: weil → wegen (+Gen) · wenn → bei (+Dat) · nachdem → nach · "
            "bevor → vor · um zu → zur · während → während (+Gen).\n"
            "Verbs become -ung / -en nouns: lesen → das Lesen, prüfen → die Prüfung.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "While reading I take notes.", "de": "Beim Lesen mache ich Notizen."},
            {"en": "After passing the exam he celebrated.", "de": "Nach dem Bestehen der Prüfung feierte er."},
            {"en": "Because of the bad weather the trip was cancelled.", "de": "Wegen des schlechten Wetters wurde die Reise abgesagt."},
            {"en": "Before the exam I was nervous.", "de": "Vor der Prüfung war ich nervös."},
            {"en": "When learning vocabulary, repetition helps.", "de": "Beim Lernen von Vokabeln hilft Wiederholung."},
            {"en": "After arriving I called home.", "de": "Nach der Ankunft rief ich zu Hause an."},
            {"en": "For a better understanding we use examples.", "de": "Zum besseren Verständnis benutzen wir Beispiele."},
            {"en": "During the lesson talking is not allowed.", "de": "Während des Unterrichts ist Reden nicht erlaubt."},
            {"en": "Because of his illness he missed school.", "de": "Wegen seiner Krankheit verpasste er die Schule."},
            {"en": "When writing I make mistakes.", "de": "Beim Schreiben mache ich Fehler."},
            {"en": "After the explanation everything was clear.", "de": "Nach der Erklärung war alles klar."},
            {"en": "Before the test we revised.", "de": "Vor dem Test wiederholten wir."},
            {"en": "For learning a language you need patience.", "de": "Zum Lernen einer Sprache braucht man Geduld."},
            {"en": "During the break we relaxed.", "de": "Während der Pause entspannten wir uns."},
            {"en": "Because of the noise I could not concentrate.", "de": "Wegen des Lärms konnte ich mich nicht konzentrieren."},
            {"en": "When solving problems logic is important.", "de": "Beim Lösen von Problemen ist Logik wichtig."},
            {"en": "After registering you get a confirmation.", "de": "Nach der Anmeldung erhält man eine Bestätigung."},
            {"en": "Before going to university she traveled.", "de": "Vor dem Studium reiste sie."},
            {"en": "For the improvement of his grades he studied more.", "de": "Zur Verbesserung seiner Noten lernte er mehr."},
            {"en": "During the presentation the audience listened.", "de": "Während der Präsentation hörte das Publikum zu."},
            {"en": "Because of a lack of time we stopped.", "de": "Wegen Zeitmangels hörten wir auf."},
            {"en": "When repeating the words you remember them.", "de": "Beim Wiederholen der Wörter behält man sie."},
            {"en": "After finishing the course I got a certificate.", "de": "Nach dem Abschluss des Kurses bekam ich ein Zertifikat."},
            {"en": "Before the deadline everyone was stressed.", "de": "Vor dem Abgabetermin waren alle gestresst."},
            {"en": "For the preparation of the exam she made a plan.", "de": "Zur Vorbereitung der Prüfung machte sie einen Plan."},
            {"en": "During the discussion opinions differed.", "de": "Während der Diskussion gingen die Meinungen auseinander."},
            {"en": "Because of the explanation I understood.", "de": "Aufgrund der Erklärung verstand ich."},
            {"en": "When practicing daily you improve.", "de": "Beim täglichen Üben wird man besser."},
            {"en": "After reading the book I wrote a review.", "de": "Nach dem Lesen des Buches schrieb ich eine Rezension."},
            {"en": "Before making a decision he thought carefully.", "de": "Vor der Entscheidung dachte er sorgfältig nach."},
            {"en": "For the analysis of the data we used software.", "de": "Zur Analyse der Daten benutzten wir Software."},
            {"en": "During the experiment we took notes.", "de": "Während des Experiments machten wir Notizen."},
            {"en": "Because of the complexity the topic was difficult.", "de": "Wegen der Komplexität war das Thema schwierig."},
            {"en": "When correcting mistakes you learn most.", "de": "Beim Korrigieren von Fehlern lernt man am meisten."},
            {"en": "After the meeting the plan was clear.", "de": "Nach der Besprechung war der Plan klar."},
            {"en": "For the development of skills practice is essential.", "de": "Zur Entwicklung von Fähigkeiten ist Übung wichtig."},
            {"en": "During the lecture I took many notes.", "de": "Während der Vorlesung machte ich viele Notizen."},
            {"en": "Because of his effort he succeeded.", "de": "Aufgrund seiner Anstrengung hatte er Erfolg."},
            {"en": "Before the publication the text was checked.", "de": "Vor der Veröffentlichung wurde der Text geprüft."},
            {"en": "Through constant learning we grow.", "de": "Durch ständiges Lernen wachsen wir."},
        ],
    },

    ("B2", "work"): {
        "note": (
            "📖 Work — B2\n\n"
            "ADVANCED CONDITIONAL CONNECTORS\n"
            "falls / sofern (if / provided that) — subordinate, verb to the END:\n"
            "• Falls Sie Fragen haben, rufen Sie an.\n"
            "• Sofern alles klappt, beginnen wir morgen.\n"
            "vorausgesetzt(, dass) (provided that) · angenommen(, dass) (assuming that):\n"
            "• Vorausgesetzt, dass das Budget reicht, stellen wir ein.\n"
            "es sei denn (unless) — main-clause order after it:\n"
            "• Ich komme morgen, es sei denn, ich werde krank.\n"
            "sonst / andernfalls (otherwise): Wir müssen sparen, sonst geht die Firma pleite.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "If you have questions, call us.", "de": "Falls Sie Fragen haben, rufen Sie an."},
            {"en": "Provided everything works, we start tomorrow.", "de": "Sofern alles klappt, beginnen wir morgen."},
            {"en": "Provided that the budget is enough, we will hire.", "de": "Vorausgesetzt, dass das Budget reicht, stellen wir ein."},
            {"en": "I will come tomorrow, unless I get sick.", "de": "Ich komme morgen, es sei denn, ich werde krank."},
            {"en": "We must save money, otherwise the company goes bankrupt.", "de": "Wir müssen sparen, sonst geht die Firma pleite."},
            {"en": "If the client agrees, we sign the contract.", "de": "Falls der Kunde zustimmt, unterschreiben wir den Vertrag."},
            {"en": "Assuming the meeting takes place, I will prepare.", "de": "Angenommen, dass das Meeting stattfindet, bereite ich mich vor."},
            {"en": "Provided the team is ready, we can present.", "de": "Sofern das Team bereit ist, können wir präsentieren."},
            {"en": "I will finish today, unless something comes up.", "de": "Ich werde heute fertig, es sei denn, es kommt etwas dazwischen."},
            {"en": "If you need help, let me know.", "de": "Falls du Hilfe brauchst, sag Bescheid."},
            {"en": "Provided that we get the funding, the project starts.", "de": "Vorausgesetzt, dass wir die Förderung bekommen, startet das Projekt."},
            {"en": "We will deliver on time, unless there is a delay.", "de": "Wir liefern pünktlich, es sei denn, es gibt eine Verzögerung."},
            {"en": "Assuming the prices stay stable, we will profit.", "de": "Angenommen, die Preise bleiben stabil, machen wir Gewinn."},
            {"en": "If the boss approves, we can begin.", "de": "Sofern der Chef zustimmt, können wir anfangen."},
            {"en": "We have to act now, otherwise we lose the deal.", "de": "Wir müssen jetzt handeln, sonst verlieren wir das Geschäft."},
            {"en": "If the data is correct, the report is ready.", "de": "Falls die Daten korrekt sind, ist der Bericht fertig."},
            {"en": "Provided that you sign today, delivery is free.", "de": "Vorausgesetzt, dass Sie heute unterschreiben, ist die Lieferung kostenlos."},
            {"en": "I will attend, unless I am needed elsewhere.", "de": "Ich nehme teil, es sei denn, ich werde woanders gebraucht."},
            {"en": "Assuming everything goes well, we expand next year.", "de": "Angenommen, alles läuft gut, expandieren wir nächstes Jahr."},
            {"en": "If you submit the form, we will process it.", "de": "Sofern Sie das Formular einreichen, bearbeiten wir es."},
            {"en": "We need more staff, otherwise we cannot finish.", "de": "Wir brauchen mehr Personal, sonst schaffen wir es nicht."},
            {"en": "If the offer is good, we accept it.", "de": "Falls das Angebot gut ist, nehmen wir es an."},
            {"en": "Provided that the deadline is met, the bonus is paid.", "de": "Vorausgesetzt, dass die Frist eingehalten wird, wird der Bonus gezahlt."},
            {"en": "I will help you, unless I run out of time.", "de": "Ich helfe dir, es sei denn, mir geht die Zeit aus."},
            {"en": "Assuming the contract is valid, we proceed.", "de": "Angenommen, der Vertrag ist gültig, machen wir weiter."},
            {"en": "If the machine breaks, production stops.", "de": "Sofern die Maschine kaputtgeht, stoppt die Produktion."},
            {"en": "We must hurry, otherwise we miss the train.", "de": "Wir müssen uns beeilen, sonst verpassen wir den Zug."},
            {"en": "If you are interested, contact us.", "de": "Falls Sie interessiert sind, kontaktieren Sie uns."},
            {"en": "Provided that sales rise, we open a new branch.", "de": "Vorausgesetzt, dass der Umsatz steigt, eröffnen wir eine neue Filiale."},
            {"en": "The plan works, unless something unexpected happens.", "de": "Der Plan funktioniert, es sei denn, etwas Unerwartetes passiert."},
            {"en": "Assuming we agree, the project can start.", "de": "Angenommen, wir sind uns einig, kann das Projekt beginnen."},
            {"en": "If the report is finished, send it to me.", "de": "Sofern der Bericht fertig ist, schick ihn mir."},
            {"en": "We have to decide, otherwise the chance is gone.", "de": "Wir müssen uns entscheiden, sonst ist die Chance weg."},
            {"en": "If the customer pays, we ship the goods.", "de": "Falls der Kunde zahlt, versenden wir die Ware."},
            {"en": "Provided that you are on time, you can join.", "de": "Vorausgesetzt, dass du pünktlich bist, kannst du mitmachen."},
            {"en": "I will sign, unless the terms change.", "de": "Ich unterschreibe, es sei denn, die Bedingungen ändern sich."},
            {"en": "Assuming the test is positive, we launch.", "de": "Angenommen, der Test ist positiv, bringen wir es auf den Markt."},
            {"en": "If you follow the rules, nothing happens.", "de": "Sofern du dich an die Regeln hältst, passiert nichts."},
            {"en": "We invest now, otherwise we fall behind.", "de": "Wir investieren jetzt, sonst fallen wir zurück."},
            {"en": "Success comes, provided that you never give up.", "de": "Erfolg kommt, vorausgesetzt, dass man niemals aufgibt."},
        ],
    },

    ("B2", "health"): {
        "note": (
            "📖 Health — B2\n\n"
            "SUBJECTIVE MODAL VERBS (certainty, guess, or hearsay)\n"
            "Modals can express the SPEAKER's assessment, not real ability/obligation.\n"
            "Certainty (high → low):\n"
            "  müssen = must be: Er muss krank sein.\n"
            "  dürfte = is probably: Sie dürfte zu Hause sein.\n"
            "  könnte / kann = could/might: Das könnte eine Erkältung sein.\n"
            "  mag = may well: Er mag recht haben.\n"
            "HEARSAY:\n"
            "  sollen = is said to: Das Medikament soll gut helfen.\n"
            "  wollen = claims to: Er will gesund sein.\n"
            "Past: modal + Partizip II + haben/sein → Er muss krank gewesen sein.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "He must be ill.", "de": "Er muss krank sein."},
            {"en": "She is probably at home.", "de": "Sie dürfte zu Hause sein."},
            {"en": "That could be a cold.", "de": "Das könnte eine Erkältung sein."},
            {"en": "The medicine is said to help well.", "de": "Das Medikament soll gut helfen."},
            {"en": "He claims to be healthy.", "de": "Er will gesund sein."},
            {"en": "He must have been ill.", "de": "Er muss krank gewesen sein."},
            {"en": "She might have a fever.", "de": "Sie könnte Fieber haben."},
            {"en": "He may well be right.", "de": "Er mag recht haben."},
            {"en": "The doctor should be very good.", "de": "Der Arzt soll sehr gut sein."},
            {"en": "You must be tired.", "de": "Du musst müde sein."},
            {"en": "It could be the flu.", "de": "Es könnte die Grippe sein."},
            {"en": "She is probably already better.", "de": "Ihr dürfte es schon besser gehen."},
            {"en": "He claims to have slept well.", "de": "Er will gut geschlafen haben."},
            {"en": "The treatment is said to be expensive.", "de": "Die Behandlung soll teuer sein."},
            {"en": "That must hurt a lot.", "de": "Das muss sehr wehtun."},
            {"en": "He might still be at the doctor.", "de": "Er könnte noch beim Arzt sein."},
            {"en": "She must have caught a cold.", "de": "Sie muss sich erkältet haben."},
            {"en": "The new therapy is said to work.", "de": "Die neue Therapie soll wirken."},
            {"en": "You should rest, you must be exhausted.", "de": "Du solltest dich ausruhen, du musst erschöpft sein."},
            {"en": "He claims to have never been sick.", "de": "Er will nie krank gewesen sein."},
            {"en": "That could be dangerous.", "de": "Das könnte gefährlich sein."},
            {"en": "She is probably sleeping now.", "de": "Sie dürfte jetzt schlafen."},
            {"en": "The pills are said to have side effects.", "de": "Die Tabletten sollen Nebenwirkungen haben."},
            {"en": "He must have forgotten the appointment.", "de": "Er muss den Termin vergessen haben."},
            {"en": "It might just be stress.", "de": "Es könnte nur Stress sein."},
            {"en": "She may be right about the diagnosis.", "de": "Sie mag mit der Diagnose recht haben."},
            {"en": "The clinic is said to be the best.", "de": "Die Klinik soll die beste sein."},
            {"en": "You must have been very worried.", "de": "Du musst sehr besorgt gewesen sein."},
            {"en": "He claims to feel fine.", "de": "Er will sich gut fühlen."},
            {"en": "That could explain the pain.", "de": "Das könnte die Schmerzen erklären."},
            {"en": "She is probably waiting for the results.", "de": "Sie dürfte auf die Ergebnisse warten."},
            {"en": "The medicine is said to be harmless.", "de": "Das Medikament soll harmlos sein."},
            {"en": "He must have taken the wrong pill.", "de": "Er muss die falsche Tablette genommen haben."},
            {"en": "It might get worse.", "de": "Es könnte schlimmer werden."},
            {"en": "She may well need an operation.", "de": "Sie mag eine Operation brauchen."},
            {"en": "The doctor is said to have helped many people.", "de": "Der Arzt soll vielen Menschen geholfen haben."},
            {"en": "You must have a strong immune system.", "de": "Du musst ein starkes Immunsystem haben."},
            {"en": "He claims to have recovered completely.", "de": "Er will sich vollständig erholt haben."},
            {"en": "That could be the reason for the headache.", "de": "Das könnte der Grund für die Kopfschmerzen sein."},
            {"en": "Whatever the cause may be, rest will help.", "de": "Was auch immer die Ursache sein mag, Ruhe wird helfen."},
        ],
    },

    ("B2", "books_films"): {
        "note": (
            "📖 Books and Films — B2\n\n"
            "EXTENDED ATTRIBUTES describing works (advanced)\n"
            "Combine modifiers and participle phrases before the noun — a hallmark of "
            "literary/critical German.\n"
            "  der von Kafka geschriebene Roman → the novel written by Kafka\n"
            "  ein von der Kritik gefeierter Film → a film celebrated by the critics\n"
            "  die in den 60er Jahren gedrehte Serie → the series shot in the 60s\n"
            "Structure: article + [phrase + participle] + noun (replaces a relative clause).\n"
            "Partizip I (active) and II (passive) both work:\n"
            "  der die Wahrheit suchende Held · das viel diskutierte Ende.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "The novel written by Kafka is famous.", "de": "Der von Kafka geschriebene Roman ist berühmt."},
            {"en": "A film celebrated by the critics won the prize.", "de": "Ein von der Kritik gefeierter Film gewann den Preis."},
            {"en": "The series shot in the 60s is a classic.", "de": "Die in den 60er Jahren gedrehte Serie ist ein Klassiker."},
            {"en": "The much-discussed ending surprised everyone.", "de": "Das viel diskutierte Ende überraschte alle."},
            {"en": "The truth-seeking hero fascinated me.", "de": "Der die Wahrheit suchende Held faszinierte mich."},
            {"en": "The book translated into many languages sold well.", "de": "Das in viele Sprachen übersetzte Buch verkaufte sich gut."},
            {"en": "The director praised by everyone made a new film.", "de": "Der von allen gelobte Regisseur drehte einen neuen Film."},
            {"en": "The story told from a child's perspective is moving.", "de": "Die aus der Sicht eines Kindes erzählte Geschichte ist bewegend."},
            {"en": "The recently published novel became a bestseller.", "de": "Der kürzlich veröffentlichte Roman wurde ein Bestseller."},
            {"en": "The film banned for years is now available.", "de": "Der jahrelang verbotene Film ist jetzt verfügbar."},
            {"en": "A character based on a real person appears in the book.", "de": "Eine auf einer realen Person basierende Figur kommt im Buch vor."},
            {"en": "The scene cut from the film was shown later.", "de": "Die aus dem Film geschnittene Szene wurde später gezeigt."},
            {"en": "The award-winning author gave an interview.", "de": "Der preisgekrönte Autor gab ein Interview."},
            {"en": "The poem written during the war is powerful.", "de": "Das während des Krieges geschriebene Gedicht ist kraftvoll."},
            {"en": "The widely read magazine published the review.", "de": "Die viel gelesene Zeitschrift veröffentlichte die Rezension."},
            {"en": "The film inspired by a true story moved me.", "de": "Der von einer wahren Geschichte inspirierte Film bewegte mich."},
            {"en": "The long-awaited sequel disappointed the fans.", "de": "Die lang erwartete Fortsetzung enttäuschte die Fans."},
            {"en": "The book recommended by my teacher is difficult.", "de": "Das von meinem Lehrer empfohlene Buch ist schwierig."},
            {"en": "The actor admired by millions retired.", "de": "Der von Millionen bewunderte Schauspieler zog sich zurück."},
            {"en": "The film released last year won an Oscar.", "de": "Der letztes Jahr erschienene Film gewann einen Oscar."},
            {"en": "The constantly changing plot confused me.", "de": "Die sich ständig ändernde Handlung verwirrte mich."},
            {"en": "The novel set in Berlin describes the war.", "de": "Der in Berlin spielende Roman beschreibt den Krieg."},
            {"en": "The scene filmed at night is impressive.", "de": "Die nachts gefilmte Szene ist beeindruckend."},
            {"en": "The harshly criticized film flopped.", "de": "Der scharf kritisierte Film floppte."},
            {"en": "The story narrated by an old man is sad.", "de": "Die von einem alten Mann erzählte Geschichte ist traurig."},
            {"en": "The carefully written script convinced the producers.", "de": "Das sorgfältig geschriebene Drehbuch überzeugte die Produzenten."},
            {"en": "The book lying on my desk is unfinished.", "de": "Das auf meinem Schreibtisch liegende Buch ist unvollendet."},
            {"en": "The character developing throughout the story is complex.", "de": "Die sich durch die Geschichte entwickelnde Figur ist komplex."},
            {"en": "The often quoted line became famous.", "de": "Der oft zitierte Satz wurde berühmt."},
            {"en": "The newly filmed version is in colour.", "de": "Die neu verfilmte Version ist in Farbe."},
            {"en": "The book forgotten for decades was rediscovered.", "de": "Das jahrzehntelang vergessene Buch wurde wiederentdeckt."},
            {"en": "The hero searching for his father travels far.", "de": "Der seinen Vater suchende Held reist weit."},
            {"en": "The deeply moving film made me cry.", "de": "Der zutiefst bewegende Film brachte mich zum Weinen."},
            {"en": "The novel published after his death became famous.", "de": "Der nach seinem Tod veröffentlichte Roman wurde berühmt."},
            {"en": "The scene improvised by the actors is the best.", "de": "Die von den Schauspielern improvisierte Szene ist die beste."},
            {"en": "The frequently adapted play is still popular.", "de": "Das häufig adaptierte Stück ist immer noch beliebt."},
            {"en": "The story unfolding slowly builds tension.", "de": "Die sich langsam entfaltende Geschichte baut Spannung auf."},
            {"en": "The widely acclaimed documentary opened my eyes.", "de": "Die viel gelobte Dokumentation öffnete mir die Augen."},
            {"en": "The film shown at the festival was experimental.", "de": "Der auf dem Festival gezeigte Film war experimentell."},
            {"en": "A story well told stays with us forever.", "de": "Eine gut erzählte Geschichte bleibt für immer bei uns."},
        ],
    },

    ("B2", "accommodation"): {
        "note": (
            "📖 Accommodation — B2\n\n"
            "GENITIVE MASTERY + formal Genitive prepositions\n"
            "Beyond wegen/während/trotz, formal German uses:\n"
            "  anhand (+Gen) — on the basis of · mittels (+Gen) — by means of ·\n"
            "  hinsichtlich (+Gen) — regarding · bezüglich (+Gen) — concerning ·\n"
            "  infolge (+Gen) — as a result of · zwecks (+Gen) — for the purpose of ·\n"
            "  angesichts (+Gen) — in view of · seitens (+Gen) — on the part of.\n"
            "• Anhand des Plans fanden wir die Wohnung.\n"
            "• Infolge des Schadens mussten wir umziehen.\n"
            "Genitive endings: des/eines + -(e)s (m/n), der/einer (f/pl).\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "On the basis of the plan we found the flat.", "de": "Anhand des Plans fanden wir die Wohnung."},
            {"en": "As a result of the damage we had to move.", "de": "Infolge des Schadens mussten wir umziehen."},
            {"en": "Regarding the rent there is a question.", "de": "Hinsichtlich der Miete gibt es eine Frage."},
            {"en": "By means of a key we opened the door.", "de": "Mittels eines Schlüssels öffneten wir die Tür."},
            {"en": "In view of the high costs we declined.", "de": "Angesichts der hohen Kosten lehnten wir ab."},
            {"en": "Concerning the contract we have doubts.", "de": "Bezüglich des Vertrags haben wir Zweifel."},
            {"en": "For the purpose of renovation the house is closed.", "de": "Zwecks Renovierung ist das Haus geschlossen."},
            {"en": "As a result of the fire the building was destroyed.", "de": "Infolge des Brandes wurde das Gebäude zerstört."},
            {"en": "On the part of the landlord there were no objections.", "de": "Seitens des Vermieters gab es keine Einwände."},
            {"en": "On the basis of the documents we signed.", "de": "Anhand der Unterlagen unterschrieben wir."},
            {"en": "Regarding the repairs we contacted the owner.", "de": "Hinsichtlich der Reparaturen kontaktierten wir den Besitzer."},
            {"en": "By means of a loan we bought the house.", "de": "Mittels eines Kredits kauften wir das Haus."},
            {"en": "In view of the situation we stayed calm.", "de": "Angesichts der Lage blieben wir ruhig."},
            {"en": "As a result of the move everything changed.", "de": "Infolge des Umzugs änderte sich alles."},
            {"en": "The roof of the old house needs repair.", "de": "Das Dach des alten Hauses muss repariert werden."},
            {"en": "The colour of the new walls is bright.", "de": "Die Farbe der neuen Wände ist hell."},
            {"en": "Concerning the deposit we asked the agent.", "de": "Bezüglich der Kaution fragten wir den Makler."},
            {"en": "For the purpose of cleaning the flat is empty.", "de": "Zwecks Reinigung ist die Wohnung leer."},
            {"en": "The size of the rooms impressed us.", "de": "Die Größe der Zimmer beeindruckte uns."},
            {"en": "On the part of the tenants there were complaints.", "de": "Seitens der Mieter gab es Beschwerden."},
            {"en": "On the basis of the photos we chose the apartment.", "de": "Anhand der Fotos wählten wir die Wohnung."},
            {"en": "The condition of the building is poor.", "de": "Der Zustand des Gebäudes ist schlecht."},
            {"en": "In view of the noise we moved out.", "de": "Angesichts des Lärms zogen wir aus."},
            {"en": "By means of an app we found the flat.", "de": "Mittels einer App fanden wir die Wohnung."},
            {"en": "As a result of the renovation the rent rose.", "de": "Infolge der Renovierung stieg die Miete."},
            {"en": "The location of the house is excellent.", "de": "Die Lage des Hauses ist ausgezeichnet."},
            {"en": "Regarding the heating there is a problem.", "de": "Hinsichtlich der Heizung gibt es ein Problem."},
            {"en": "The value of the property increased.", "de": "Der Wert der Immobilie stieg."},
            {"en": "Concerning the neighbors we have no complaints.", "de": "Bezüglich der Nachbarn haben wir keine Beschwerden."},
            {"en": "For the purpose of inspection we visited the house.", "de": "Zwecks Besichtigung besuchten wir das Haus."},
            {"en": "On the basis of the report the damage was clear.", "de": "Anhand des Berichts war der Schaden klar."},
            {"en": "In view of the price the flat is a bargain.", "de": "Angesichts des Preises ist die Wohnung ein Schnäppchen."},
            {"en": "The windows of the apartment face the park.", "de": "Die Fenster der Wohnung gehen zum Park."},
            {"en": "As a result of the storm the roof leaked.", "de": "Infolge des Sturms war das Dach undicht."},
            {"en": "The history of the building is interesting.", "de": "Die Geschichte des Gebäudes ist interessant."},
            {"en": "By means of a contract the terms were fixed.", "de": "Mittels eines Vertrags wurden die Bedingungen festgelegt."},
            {"en": "On the part of the owner help was offered.", "de": "Seitens des Besitzers wurde Hilfe angeboten."},
            {"en": "Regarding the garden we have plans.", "de": "Hinsichtlich des Gartens haben wir Pläne."},
            {"en": "The atmosphere of the house is cozy.", "de": "Die Atmosphäre des Hauses ist gemütlich."},
            {"en": "The beauty of a home lies in its details.", "de": "Die Schönheit eines Zuhauses liegt in seinen Details."},
        ],
    },

    ("B2", "clothes_fashion"): {
        "note": (
            "📖 Clothes & Fashion — B2\n\n"
            "ADJECTIVE DECLENSION — full mastery (the ending depends on the determiner)\n"
            "After alle/beide/manche/diese → like the definite article (mostly -en in plural):\n"
            "  alle teuren Kleider · beide neuen Mäntel · manche modischen Schuhe.\n"
            "After viele/wenige/einige/andere/mehrere → the adjective shows the case:\n"
            "  viele schöne Kleider · mit mehreren teuren Stücken (Dat pl → -en).\n"
            "After etwas/nichts/viel/wenig → neuter -es: etwas Modisches, nichts Passendes.\n"
            "Genitive & Dative end mostly in -en: wegen des teuren Mantels · mit dem roten Kleid.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "All the expensive dresses are sold.", "de": "Alle teuren Kleider sind verkauft."},
            {"en": "Both new coats fit well.", "de": "Beide neuen Mäntel passen gut."},
            {"en": "Some fashionable shoes are cheap.", "de": "Manche modischen Schuhe sind billig."},
            {"en": "Many beautiful dresses hang here.", "de": "Viele schöne Kleider hängen hier."},
            {"en": "I am looking for something fashionable.", "de": "Ich suche etwas Modisches."},
            {"en": "There is nothing suitable.", "de": "Es gibt nichts Passendes."},
            {"en": "With several expensive pieces she built a collection.", "de": "Mit mehreren teuren Stücken baute sie eine Kollektion auf."},
            {"en": "Because of the expensive coat I waited.", "de": "Wegen des teuren Mantels wartete ich."},
            {"en": "She wears the red dress.", "de": "Sie trägt das rote Kleid."},
            {"en": "The jacket is made of pure silk.", "de": "Die Jacke ist aus reiner Seide."},
            {"en": "All the new collections are elegant.", "de": "Alle neuen Kollektionen sind elegant."},
            {"en": "Few good designers remain.", "de": "Wenige gute Designer bleiben."},
            {"en": "I bought some warm sweaters.", "de": "Ich kaufte einige warme Pullover."},
            {"en": "Both black shoes are scratched.", "de": "Beide schwarzen Schuhe sind zerkratzt."},
            {"en": "With the blue scarf she looked elegant.", "de": "Mit dem blauen Schal sah sie elegant aus."},
            {"en": "Some old hats are valuable.", "de": "Manche alten Hüte sind wertvoll."},
            {"en": "I prefer something simple.", "de": "Ich bevorzuge etwas Schlichtes."},
            {"en": "Many young people follow fashion.", "de": "Viele junge Leute folgen der Mode."},
            {"en": "Despite the high prices she bought it.", "de": "Trotz der hohen Preise kaufte sie es."},
            {"en": "Other expensive brands are similar.", "de": "Andere teure Marken sind ähnlich."},
            {"en": "With several colourful dresses she traveled.", "de": "Mit mehreren bunten Kleidern reiste sie."},
            {"en": "All the comfortable shoes were gone.", "de": "Alle bequemen Schuhe waren weg."},
            {"en": "I found nothing cheaper.", "de": "Ich fand nichts Billigeres."},
            {"en": "The colour of the new jacket is bright.", "de": "Die Farbe der neuen Jacke ist hell."},
            {"en": "Both elegant coats suit you.", "de": "Beide eleganten Mäntel stehen dir."},
            {"en": "Some modern designs are minimalist.", "de": "Manche modernen Designs sind minimalistisch."},
            {"en": "With the warm gloves my hands stayed warm.", "de": "Mit den warmen Handschuhen blieben meine Hände warm."},
            {"en": "Many expensive labels are overrated.", "de": "Viele teure Marken sind überbewertet."},
            {"en": "Because of the soft fabric it is comfortable.", "de": "Wegen des weichen Stoffes ist es bequem."},
            {"en": "She wears something colourful today.", "de": "Sie trägt heute etwas Buntes."},
            {"en": "All the famous designers came.", "de": "Alle berühmten Designer kamen."},
            {"en": "With a few good pieces you can dress well.", "de": "Mit ein paar guten Stücken kann man sich gut kleiden."},
            {"en": "The style of the old coat is timeless.", "de": "Der Stil des alten Mantels ist zeitlos."},
            {"en": "Both white shirts are ironed.", "de": "Beide weißen Hemden sind gebügelt."},
            {"en": "Some cheap clothes look expensive.", "de": "Manche billigen Kleider sehen teuer aus."},
            {"en": "In the elegant dress she felt confident.", "de": "In dem eleganten Kleid fühlte sie sich selbstbewusst."},
            {"en": "Many new trends disappear quickly.", "de": "Viele neue Trends verschwinden schnell."},
            {"en": "Despite the simple design it is beautiful.", "de": "Trotz des schlichten Designs ist es schön."},
            {"en": "With all these wonderful clothes I cannot choose.", "de": "Mit all diesen wunderbaren Kleidern kann ich mich nicht entscheiden."},
            {"en": "True elegance lies in well-chosen details.", "de": "Wahre Eleganz liegt in gut gewählten Details."},
        ],
    },

    ("B2", "personality"): {
        "note": (
            "📖 Personality — B2\n\n"
            "FUNCTION-VERB CONSTRUCTIONS for feelings & character\n"
            "Describe emotions and traits with noun + light verb (formal, idiomatic):\n"
            "  in Wut geraten (fly into a rage) · die Geduld verlieren (lose patience) ·\n"
            "  Mut fassen (take heart) · Rücksicht nehmen auf (be considerate of) ·\n"
            "  Vertrauen schenken (give trust) · Eindruck machen (make an impression) ·\n"
            "  in Verlegenheit geraten (get embarrassed) · zur Vernunft kommen (come to sense) ·\n"
            "  Stellung nehmen zu (take a position on) · Wert legen auf (value).\n"
            "• Er gerät schnell in Wut.  ·  Sie nimmt Rücksicht auf andere.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "He quickly flies into a rage.", "de": "Er gerät schnell in Wut."},
            {"en": "She is considerate of others.", "de": "Sie nimmt Rücksicht auf andere."},
            {"en": "He often loses his patience.", "de": "Er verliert oft die Geduld."},
            {"en": "She took heart and spoke.", "de": "Sie fasste Mut und sprach."},
            {"en": "He makes a good impression.", "de": "Er macht einen guten Eindruck."},
            {"en": "She gives everyone her trust.", "de": "Sie schenkt jedem ihr Vertrauen."},
            {"en": "He values honesty.", "de": "Er legt Wert auf Ehrlichkeit."},
            {"en": "She easily gets embarrassed.", "de": "Sie gerät leicht in Verlegenheit."},
            {"en": "Finally he came to his senses.", "de": "Endlich kam er zur Vernunft."},
            {"en": "She takes a clear position on the issue.", "de": "Sie nimmt klar Stellung zu dem Thema."},
            {"en": "He keeps his temper under control.", "de": "Er hat sein Temperament unter Kontrolle."},
            {"en": "She shows great patience.", "de": "Sie zeigt große Geduld."},
            {"en": "He took offense at the remark.", "de": "Er nahm Anstoß an der Bemerkung."},
            {"en": "She pays attention to detail.", "de": "Sie achtet auf Details."},
            {"en": "He puts himself in others' shoes.", "de": "Er versetzt sich in andere hinein."},
            {"en": "She never loses her composure.", "de": "Sie verliert nie die Fassung."},
            {"en": "He has a strong sense of responsibility.", "de": "Er hat ein starkes Verantwortungsgefühl."},
            {"en": "She takes criticism seriously.", "de": "Sie nimmt Kritik ernst."},
            {"en": "He gained the trust of his colleagues.", "de": "Er gewann das Vertrauen seiner Kollegen."},
            {"en": "She made an effort to stay calm.", "de": "Sie gab sich Mühe, ruhig zu bleiben."},
            {"en": "He gets nervous in front of crowds.", "de": "Er wird vor Menschenmengen nervös."},
            {"en": "She showed consideration for the elderly.", "de": "Sie nahm Rücksicht auf die Älteren."},
            {"en": "He has a tendency to exaggerate.", "de": "Er neigt dazu, zu übertreiben."},
            {"en": "She kept her promise.", "de": "Sie hielt ihr Versprechen."},
            {"en": "He drew attention to himself.", "de": "Er machte auf sich aufmerksam."},
            {"en": "She has the courage to say no.", "de": "Sie hat den Mut, Nein zu sagen."},
            {"en": "He took responsibility for the team.", "de": "Er übernahm die Verantwortung für das Team."},
            {"en": "She controls her emotions well.", "de": "Sie beherrscht ihre Gefühle gut."},
            {"en": "He brought the conflict to an end.", "de": "Er brachte den Konflikt zu einem Ende."},
            {"en": "She places great value on independence.", "de": "Sie legt großen Wert auf Unabhängigkeit."},
            {"en": "He fell into despair.", "de": "Er geriet in Verzweiflung."},
            {"en": "She has respect for other opinions.", "de": "Sie hat Respekt vor anderen Meinungen."},
            {"en": "He made the decision with a clear head.", "de": "Er traf die Entscheidung mit klarem Kopf."},
            {"en": "She takes pleasure in helping others.", "de": "Sie hat Freude daran, anderen zu helfen."},
            {"en": "He kept calm despite the pressure.", "de": "Er bewahrte trotz des Drucks die Ruhe."},
            {"en": "She came to terms with the situation.", "de": "Sie fand sich mit der Situation ab."},
            {"en": "He gives his friends good advice.", "de": "Er gibt seinen Freunden gute Ratschläge."},
            {"en": "She put her fear aside.", "de": "Sie legte ihre Angst beiseite."},
            {"en": "He has confidence in his abilities.", "de": "Er hat Vertrauen in seine Fähigkeiten."},
            {"en": "A calm mind makes the wisest decisions.", "de": "Ein ruhiger Geist trifft die klügsten Entscheidungen."},
        ],
    },

    ("B2", "business"): {
        "note": (
            "📖 Business — B2\n\n"
            "BUSINESS FUNCTION-VERB CONSTRUCTIONS (formal register)\n"
            "Essential for emails, meetings and reports:\n"
            "  in Anspruch nehmen (make use of / claim) · zur Verfügung stellen (provide) ·\n"
            "  in Frage stellen (call into question) · Bezug nehmen auf (refer to) ·\n"
            "  in Betrieb nehmen (put into operation) · zur Sprache bringen (raise) ·\n"
            "  in Kauf nehmen (accept as a downside) · Rechnung tragen (+Dat) (take into account) ·\n"
            "  unter Beweis stellen (prove) · in Aussicht stellen (hold out the prospect of).\n"
            "• Wir stellen Ihnen die Daten zur Verfügung.  ·  Dürfen wir Ihre Hilfe in Anspruch nehmen?\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "We provide you with the data.", "de": "Wir stellen Ihnen die Daten zur Verfügung."},
            {"en": "May we make use of your help?", "de": "Dürfen wir Ihre Hilfe in Anspruch nehmen?"},
            {"en": "He called the decision into question.", "de": "Er stellte die Entscheidung in Frage."},
            {"en": "We refer to your offer.", "de": "Wir nehmen Bezug auf Ihr Angebot."},
            {"en": "The machine was put into operation.", "de": "Die Maschine wurde in Betrieb genommen."},
            {"en": "She raised the problem at the meeting.", "de": "Sie brachte das Problem zur Sprache."},
            {"en": "We accept the higher costs as a downside.", "de": "Wir nehmen die höheren Kosten in Kauf."},
            {"en": "The plan takes the risks into account.", "de": "Der Plan trägt den Risiken Rechnung."},
            {"en": "He proved his competence.", "de": "Er stellte seine Kompetenz unter Beweis."},
            {"en": "They held out the prospect of a raise.", "de": "Sie stellten eine Gehaltserhöhung in Aussicht."},
            {"en": "We would like to make use of this offer.", "de": "Wir möchten dieses Angebot in Anspruch nehmen."},
            {"en": "The company provides the equipment.", "de": "Die Firma stellt die Ausrüstung zur Verfügung."},
            {"en": "The experts questioned the results.", "de": "Die Experten stellten die Ergebnisse in Frage."},
            {"en": "With reference to your letter, we agree.", "de": "Mit Bezug auf Ihr Schreiben stimmen wir zu."},
            {"en": "The new system will be put into operation soon.", "de": "Das neue System wird bald in Betrieb genommen."},
            {"en": "He brought the matter up at the conference.", "de": "Er brachte die Angelegenheit auf der Konferenz zur Sprache."},
            {"en": "We have to accept some delays.", "de": "Wir müssen einige Verzögerungen in Kauf nehmen."},
            {"en": "The strategy takes the customers into account.", "de": "Die Strategie trägt den Kunden Rechnung."},
            {"en": "She demonstrated her leadership skills.", "de": "Sie stellte ihre Führungsqualitäten unter Beweis."},
            {"en": "The boss held out the prospect of promotion.", "de": "Der Chef stellte eine Beförderung in Aussicht."},
            {"en": "We took advantage of the consulting service.", "de": "Wir nahmen den Beratungsdienst in Anspruch."},
            {"en": "The bank provides a loan.", "de": "Die Bank stellt einen Kredit zur Verfügung."},
            {"en": "The auditors questioned the figures.", "de": "Die Prüfer stellten die Zahlen in Frage."},
            {"en": "Referring to our agreement, we proceed.", "de": "Unter Bezug auf unsere Vereinbarung machen wir weiter."},
            {"en": "The factory was put into operation last year.", "de": "Die Fabrik wurde letztes Jahr in Betrieb genommen."},
            {"en": "He raised an important point.", "de": "Er brachte einen wichtigen Punkt zur Sprache."},
            {"en": "We accept the financial risk.", "de": "Wir nehmen das finanzielle Risiko in Kauf."},
            {"en": "The reform takes the workers into account.", "de": "Die Reform trägt den Arbeitern Rechnung."},
            {"en": "The team proved its efficiency.", "de": "Das Team stellte seine Effizienz unter Beweis."},
            {"en": "The contract holds out the prospect of cooperation.", "de": "Der Vertrag stellt eine Zusammenarbeit in Aussicht."},
            {"en": "We claim our legal rights.", "de": "Wir nehmen unsere Rechte in Anspruch."},
            {"en": "The firm makes the report available.", "de": "Die Firma stellt den Bericht zur Verfügung."},
            {"en": "Critics questioned the entire project.", "de": "Kritiker stellten das gesamte Projekt in Frage."},
            {"en": "He referred to the previous discussion.", "de": "Er nahm Bezug auf die vorherige Diskussion."},
            {"en": "The plant will be put into operation in spring.", "de": "Die Anlage wird im Frühjahr in Betrieb genommen."},
            {"en": "She brought the budget issue to attention.", "de": "Sie brachte die Budgetfrage zur Sprache."},
            {"en": "We must accept certain compromises.", "de": "Wir müssen gewisse Kompromisse in Kauf nehmen."},
            {"en": "The policy takes the environment into account.", "de": "Die Politik trägt der Umwelt Rechnung."},
            {"en": "The candidate proved her qualifications.", "de": "Die Kandidatin stellte ihre Qualifikationen unter Beweis."},
            {"en": "Good management turns challenges into opportunities.", "de": "Gutes Management macht aus Herausforderungen Chancen."},
        ],
    },

    ("B2", "physical_appearance"): {
        "note": (
            "📖 Physical Appearance — B2\n\n"
            "EXTENDED ATTRIBUTES + refined COMPARISON\n"
            "Describe appearance with packed pre-noun attributes:\n"
            "  die sorgfältig frisierten Haare · der modisch gekleidete Mann · "
            "ihre auffallend blauen Augen.\n"
            "COMPARISON refinements:\n"
            "  immer + comparative (more and more): Sie wird immer schöner.\n"
            "  je … desto with full clauses: Je älter er wird, desto distinguierter wirkt er.\n"
            "  viel/etwas/weit/bei weitem + comparative: viel größer, weit eleganter.\n"
            "  nicht so … wie · genauso … wie.\n"
            "• Er ist weit jünger, als er aussieht.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "The carefully styled hair looked perfect.", "de": "Die sorgfältig frisierten Haare sahen perfekt aus."},
            {"en": "The fashionably dressed man entered.", "de": "Der modisch gekleidete Mann trat ein."},
            {"en": "Her strikingly blue eyes impressed everyone.", "de": "Ihre auffallend blauen Augen beeindruckten alle."},
            {"en": "She is becoming more and more beautiful.", "de": "Sie wird immer schöner."},
            {"en": "The older he gets, the more distinguished he looks.", "de": "Je älter er wird, desto distinguierter wirkt er."},
            {"en": "He is much taller than his brother.", "de": "Er ist viel größer als sein Bruder."},
            {"en": "He is far younger than he looks.", "de": "Er ist weit jünger, als er aussieht."},
            {"en": "She is not as tall as her sister.", "de": "Sie ist nicht so groß wie ihre Schwester."},
            {"en": "He is just as elegant as his father.", "de": "Er ist genauso elegant wie sein Vater."},
            {"en": "The neatly trimmed beard suited him.", "de": "Der ordentlich gestutzte Bart stand ihm."},
            {"en": "Her beautifully manicured nails shone.", "de": "Ihre schön manikürten Nägel glänzten."},
            {"en": "The well-dressed woman drew attention.", "de": "Die gut gekleidete Frau erregte Aufmerksamkeit."},
            {"en": "He looks somewhat older with the beard.", "de": "Mit dem Bart sieht er etwas älter aus."},
            {"en": "The more she smiles, the prettier she seems.", "de": "Je mehr sie lächelt, desto hübscher wirkt sie."},
            {"en": "His freshly cut hair made him look younger.", "de": "Sein frisch geschnittenes Haar ließ ihn jünger aussehen."},
            {"en": "Her elegantly styled dress was admired.", "de": "Ihr elegant gestaltetes Kleid wurde bewundert."},
            {"en": "He is by far the most attractive of them.", "de": "Er ist bei weitem der attraktivste von ihnen."},
            {"en": "She is as slim as a model.", "de": "Sie ist so schlank wie ein Model."},
            {"en": "The man with the carefully chosen clothes stood out.", "de": "Der Mann mit der sorgfältig gewählten Kleidung fiel auf."},
            {"en": "Her naturally curly hair is gorgeous.", "de": "Ihr natürlich gelocktes Haar ist wunderschön."},
            {"en": "He looks healthier than ever.", "de": "Er sieht gesünder aus als je zuvor."},
            {"en": "The brightly colored shirt suited her.", "de": "Das knallbunt gefärbte Hemd stand ihr."},
            {"en": "She seems younger the more she laughs.", "de": "Sie wirkt jünger, je mehr sie lacht."},
            {"en": "His perfectly fitting suit looked expensive.", "de": "Sein perfekt sitzender Anzug sah teuer aus."},
            {"en": "Her smoothly combed hair was elegant.", "de": "Ihr glatt gekämmtes Haar war elegant."},
            {"en": "He is somewhat slimmer than last year.", "de": "Er ist etwas schlanker als letztes Jahr."},
            {"en": "The well-groomed gentleman greeted us.", "de": "Der gepflegte Herr begrüßte uns."},
            {"en": "The tighter the dress, the more elegant she looked.", "de": "Je enger das Kleid, desto eleganter sah sie aus."},
            {"en": "His deeply tanned skin showed he traveled.", "de": "Seine tief gebräunte Haut zeigte, dass er gereist war."},
            {"en": "She is far more graceful than before.", "de": "Sie ist weit anmutiger als zuvor."},
            {"en": "The carefully applied makeup looked natural.", "de": "Das sorgfältig aufgetragene Make-up sah natürlich aus."},
            {"en": "He grows more handsome every year.", "de": "Er wird jedes Jahr attraktiver."},
            {"en": "Her neatly braided hair was admired.", "de": "Ihr ordentlich geflochtenes Haar wurde bewundert."},
            {"en": "He is not nearly as old as he seems.", "de": "Er ist längst nicht so alt, wie er scheint."},
            {"en": "The fashionably cut coat fit perfectly.", "de": "Der modisch geschnittene Mantel passte perfekt."},
            {"en": "She looked more confident with the new haircut.", "de": "Mit dem neuen Haarschnitt sah sie selbstbewusster aus."},
            {"en": "His broad shoulders made him look strong.", "de": "Seine breiten Schultern ließen ihn stark aussehen."},
            {"en": "The more elegant the clothes, the better the impression.", "de": "Je eleganter die Kleidung, desto besser der Eindruck."},
            {"en": "Her radiantly smiling face lit up the room.", "de": "Ihr strahlend lächelndes Gesicht erhellte den Raum."},
            {"en": "True beauty grows more attractive with kindness.", "de": "Wahre Schönheit wird mit Freundlichkeit immer anziehender."},
        ],
    },

    ("B2", "town_city"): {
        "note": (
            "📖 Town & City — B2\n\n"
            "ADVANCED CONNECTORS — manner, contrast & condition\n"
            "indem (by …-ing, the means) — subordinate, verb to the END:\n"
            "• Man spart Zeit, indem man die U-Bahn nimmt.\n"
            "wohingegen / während (whereas, contrast):\n"
            "• Das Zentrum ist laut, wohingegen die Vororte ruhig sind.\n"
            "• Während die Altstadt klein ist, ist das Neubaugebiet riesig.\n"
            "je nachdem(, ob/wie/wo) (depending on whether/how/where):\n"
            "• Je nachdem, ob es regnet, gehen wir zu Fuß oder fahren.\n"
            "All four send the verb to the END of their clause.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "You save time by taking the metro.", "de": "Man spart Zeit, indem man die U-Bahn nimmt."},
            {"en": "The center is loud, whereas the suburbs are quiet.", "de": "Das Zentrum ist laut, wohingegen die Vororte ruhig sind."},
            {"en": "Depending on whether it rains, we walk or drive.", "de": "Je nachdem, ob es regnet, gehen wir zu Fuß oder fahren."},
            {"en": "While the old town is small, the new area is huge.", "de": "Während die Altstadt klein ist, ist das Neubaugebiet riesig."},
            {"en": "You reach the museum by following this street.", "de": "Man erreicht das Museum, indem man dieser Straße folgt."},
            {"en": "The streets are wide, whereas the alleys are narrow.", "de": "Die Straßen sind breit, wohingegen die Gassen eng sind."},
            {"en": "We improve the city by planting more trees.", "de": "Wir verbessern die Stadt, indem wir mehr Bäume pflanzen."},
            {"en": "Depending on how busy it is, we take a taxi.", "de": "Je nachdem, wie voll es ist, nehmen wir ein Taxi."},
            {"en": "The north is industrial, whereas the south is green.", "de": "Der Norden ist industriell, wohingegen der Süden grün ist."},
            {"en": "You find parking by using the app.", "de": "Man findet einen Parkplatz, indem man die App benutzt."},
            {"en": "While the city is modern, the village is traditional.", "de": "Während die Stadt modern ist, ist das Dorf traditionell."},
            {"en": "We reduce traffic by building bike lanes.", "de": "Wir reduzieren den Verkehr, indem wir Radwege bauen."},
            {"en": "Depending on the time, the square is empty or full.", "de": "Je nachdem, wie spät es ist, ist der Platz leer oder voll."},
            {"en": "The old district is charming, whereas the new one is dull.", "de": "Das alte Viertel ist charmant, wohingegen das neue langweilig ist."},
            {"en": "You learn a city by walking through it.", "de": "Man lernt eine Stadt kennen, indem man durch sie geht."},
            {"en": "While prices rise downtown, they fall outside.", "de": "Während die Preise im Zentrum steigen, fallen sie außerhalb."},
            {"en": "We keep the city clean by recycling.", "de": "Wir halten die Stadt sauber, indem wir recyceln."},
            {"en": "Depending on the weather, the market is open or closed.", "de": "Je nachdem, wie das Wetter ist, ist der Markt offen oder geschlossen."},
            {"en": "The east side is poor, whereas the west is wealthy.", "de": "Die Ostseite ist arm, wohingegen die Westseite wohlhabend ist."},
            {"en": "You avoid traffic by leaving early.", "de": "Man vermeidet den Verkehr, indem man früh losfährt."},
            {"en": "While the streets are crowded, the parks are peaceful.", "de": "Während die Straßen voll sind, sind die Parks friedlich."},
            {"en": "We make the city safer by adding lights.", "de": "Wir machen die Stadt sicherer, indem wir Lichter anbringen."},
            {"en": "Depending on whether you have a car, life is easier or harder.", "de": "Je nachdem, ob man ein Auto hat, ist das Leben leichter oder schwerer."},
            {"en": "The center is expensive, whereas the outskirts are affordable.", "de": "Das Zentrum ist teuer, wohingegen die Außenbezirke bezahlbar sind."},
            {"en": "You support local shops by buying there.", "de": "Man unterstützt lokale Geschäfte, indem man dort einkauft."},
            {"en": "While tourists love the cathedral, locals avoid it.", "de": "Während Touristen den Dom lieben, meiden ihn die Einheimischen."},
            {"en": "We connect the districts by extending the tram.", "de": "Wir verbinden die Stadtteile, indem wir die Straßenbahn verlängern."},
            {"en": "Depending on the season, the town is lively or quiet.", "de": "Je nachdem, welche Jahreszeit es ist, ist die Stadt lebhaft oder ruhig."},
            {"en": "The river divides the city, whereas the bridges unite it.", "de": "Der Fluss teilt die Stadt, wohingegen die Brücken sie verbinden."},
            {"en": "You discover hidden corners by getting lost.", "de": "Man entdeckt versteckte Ecken, indem man sich verläuft."},
            {"en": "While the architecture is old, the lifestyle is modern.", "de": "Während die Architektur alt ist, ist der Lebensstil modern."},
            {"en": "We fight pollution by reducing cars.", "de": "Wir bekämpfen die Verschmutzung, indem wir Autos reduzieren."},
            {"en": "Depending on where you live, the rent varies.", "de": "Je nachdem, wo man wohnt, ist die Miete unterschiedlich."},
            {"en": "The square is busy by day, whereas it is empty at night.", "de": "Der Platz ist tagsüber voll, wohingegen er nachts leer ist."},
            {"en": "You experience the culture by visiting the markets.", "de": "Man erlebt die Kultur, indem man die Märkte besucht."},
            {"en": "While the center attracts business, the edge offers space.", "de": "Während das Zentrum Geschäfte anzieht, bietet der Rand Platz."},
            {"en": "We revive the neighborhood by opening cafés.", "de": "Wir beleben das Viertel, indem wir Cafés eröffnen."},
            {"en": "Depending on traffic, the trip takes ten or thirty minutes.", "de": "Je nachdem, wie der Verkehr ist, dauert die Fahrt zehn oder dreißig Minuten."},
            {"en": "The historic part is protected, whereas the rest is developed.", "de": "Der historische Teil ist geschützt, wohingegen der Rest bebaut wird."},
            {"en": "A city grows livable by putting people before cars.", "de": "Eine Stadt wird lebenswert, indem sie Menschen vor Autos stellt."},
        ],
    },

    ("B2", "music"): {
        "note": (
            "📖 Music — B2\n\n"
            "CONCESSIVE & EMPHATIC STRUCTURES\n"
            "so + adjective/adverb + auch (however …) — the clause is concessive:\n"
            "• So gut er auch singt, er gewinnt nie. → However well he sings, he never wins.\n"
            "• So laut die Musik auch ist, ich kann schlafen.\n"
            "wie/was/wer auch immer (however / whatever / whoever):\n"
            "• Wie auch immer das Lied heißt, es ist schön.\n"
            "mögen for concession: Mag das Lied auch alt sein, es bleibt beliebt.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "However well he sings, he never wins.", "de": "So gut er auch singt, er gewinnt nie."},
            {"en": "However loud the music is, I can sleep.", "de": "So laut die Musik auch ist, ich kann schlafen."},
            {"en": "Whatever the song is called, it is beautiful.", "de": "Wie auch immer das Lied heißt, es ist schön."},
            {"en": "The song may be old, but it stays popular.", "de": "Mag das Lied auch alt sein, es bleibt beliebt."},
            {"en": "However hard she practices, it is never enough.", "de": "So sehr sie auch übt, es ist nie genug."},
            {"en": "Whoever sings this, it sounds great.", "de": "Wer auch immer das singt, es klingt großartig."},
            {"en": "However expensive the ticket is, I will buy it.", "de": "So teuer die Karte auch ist, ich kaufe sie."},
            {"en": "Whatever you play, I will listen.", "de": "Was auch immer du spielst, ich höre zu."},
            {"en": "However often I hear it, I love it.", "de": "So oft ich es auch höre, ich liebe es."},
            {"en": "The band may be small, but it is talented.", "de": "Mag die Band auch klein sein, sie ist talentiert."},
            {"en": "However long the concert lasts, nobody leaves.", "de": "So lange das Konzert auch dauert, niemand geht."},
            {"en": "Whatever happens, the show goes on.", "de": "Was auch immer passiert, die Show geht weiter."},
            {"en": "However tired the singer is, she performs.", "de": "So müde die Sängerin auch ist, sie tritt auf."},
            {"en": "Whoever wrote this melody was a genius.", "de": "Wer auch immer diese Melodie schrieb, war ein Genie."},
            {"en": "However modern the style is, the roots remain.", "de": "So modern der Stil auch ist, die Wurzeln bleiben."},
            {"en": "The lyrics may be simple, but they touch us.", "de": "Mögen die Texte auch einfach sein, sie berühren uns."},
            {"en": "However quietly he plays, you can hear the emotion.", "de": "So leise er auch spielt, man hört die Emotion."},
            {"en": "Whatever instrument she chooses, she masters it.", "de": "Welches Instrument sie auch wählt, sie beherrscht es."},
            {"en": "However much it costs, the festival is worth it.", "de": "So viel es auch kostet, das Festival lohnt sich."},
            {"en": "Whoever listens carefully will understand.", "de": "Wer auch immer genau zuhört, wird verstehen."},
            {"en": "However new the song is, it already feels familiar.", "de": "So neu das Lied auch ist, es fühlt sich schon vertraut an."},
            {"en": "The melody may be sad, but it is comforting.", "de": "Mag die Melodie auch traurig sein, sie tröstet."},
            {"en": "However badly the concert is organized, the fans come.", "de": "So schlecht das Konzert auch organisiert ist, die Fans kommen."},
            {"en": "Whatever genre you prefer, music connects us.", "de": "Welches Genre du auch bevorzugst, Musik verbindet uns."},
            {"en": "However famous he becomes, he stays humble.", "de": "So berühmt er auch wird, er bleibt bescheiden."},
            {"en": "Whoever plays last gets the most applause.", "de": "Wer auch immer zuletzt spielt, bekommt den meisten Applaus."},
            {"en": "However complex the piece is, she plays it perfectly.", "de": "So komplex das Stück auch ist, sie spielt es perfekt."},
            {"en": "The song may be short, but it is unforgettable.", "de": "Mag das Lied auch kurz sein, es ist unvergesslich."},
            {"en": "However late it gets, the musicians keep playing.", "de": "So spät es auch wird, die Musiker spielen weiter."},
            {"en": "Whatever the critics say, the audience loves it.", "de": "Was auch immer die Kritiker sagen, das Publikum liebt es."},
            {"en": "However softly she sings, every word is clear.", "de": "So leise sie auch singt, jedes Wort ist klar."},
            {"en": "Whoever discovers this band is lucky.", "de": "Wer auch immer diese Band entdeckt, hat Glück."},
            {"en": "However different our tastes are, we agree on this.", "de": "So unterschiedlich unser Geschmack auch ist, hier sind wir uns einig."},
            {"en": "The album may be old, but it still sells.", "de": "Mag das Album auch alt sein, es verkauft sich noch."},
            {"en": "However nervous he is, he never shows it on stage.", "de": "So nervös er auch ist, auf der Bühne zeigt er es nie."},
            {"en": "Whatever song comes next, the crowd is ready.", "de": "Welches Lied auch als Nächstes kommt, die Menge ist bereit."},
            {"en": "However simple the rhythm is, it makes you dance.", "de": "So einfach der Rhythmus auch ist, er bringt dich zum Tanzen."},
            {"en": "Whoever sang that high note deserves respect.", "de": "Wer auch immer diese hohe Note sang, verdient Respekt."},
            {"en": "However long I search, I cannot find that song.", "de": "So lange ich auch suche, ich finde dieses Lied nicht."},
            {"en": "However the world changes, music remains its heartbeat.", "de": "Wie sich die Welt auch verändert, die Musik bleibt ihr Herzschlag."},
        ],
    },

    ("B2", "weather"): {
        "note": (
            "📖 Weather — B2\n\n"
            "CONCESSIVE CLAUSES (although / even if)\n"
            "obwohl / obgleich / obschon (although — a real fact) — verb to the END:\n"
            "• Obwohl es regnet, gehen wir spazieren.\n"
            "auch wenn / selbst wenn (even if — hypothetical) — verb to the END:\n"
            "• Auch wenn es regnet, fahren wir los.\n"
            "• Selbst wenn es schneien würde, käme ich. (Konjunktiv II = very hypothetical)\n"
            "trotzdem / dennoch (nevertheless — adverb, position 2 + inversion):\n"
            "• Es regnet; trotzdem gehen wir.\n"
            "Note: obwohl = it IS so; auch wenn = even IF it were so.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "Although it is raining, we go for a walk.", "de": "Obwohl es regnet, gehen wir spazieren."},
            {"en": "Even if it rains, we set off.", "de": "Auch wenn es regnet, fahren wir los."},
            {"en": "Even if it snowed, I would come.", "de": "Selbst wenn es schneien würde, käme ich."},
            {"en": "It is raining; nevertheless we go.", "de": "Es regnet; trotzdem gehen wir."},
            {"en": "Although it is cold, she wears no jacket.", "de": "Obwohl es kalt ist, trägt sie keine Jacke."},
            {"en": "Even if it is hot, he wears a suit.", "de": "Auch wenn es heiß ist, trägt er einen Anzug."},
            {"en": "Although the sun is shining, it is freezing.", "de": "Obwohl die Sonne scheint, ist es eiskalt."},
            {"en": "Even if the storm comes, the festival continues.", "de": "Auch wenn der Sturm kommt, geht das Festival weiter."},
            {"en": "It was foggy; nevertheless the plane took off.", "de": "Es war neblig; dennoch startete das Flugzeug."},
            {"en": "Although it rained all day, we enjoyed the trip.", "de": "Obwohl es den ganzen Tag regnete, genossen wir den Ausflug."},
            {"en": "Even if it were warmer, I would not swim.", "de": "Selbst wenn es wärmer wäre, würde ich nicht schwimmen."},
            {"en": "Although the weather is bad, the mood is good.", "de": "Obwohl das Wetter schlecht ist, ist die Stimmung gut."},
            {"en": "Even if it is windy, we go sailing.", "de": "Auch wenn es windig ist, gehen wir segeln."},
            {"en": "Although it was snowing, the train ran on time.", "de": "Obwohl es schneite, fuhr der Zug pünktlich."},
            {"en": "It is cold; nevertheless the children play outside.", "de": "Es ist kalt; trotzdem spielen die Kinder draußen."},
            {"en": "Even if it rained for days, the river would not flood.", "de": "Selbst wenn es tagelang regnete, würde der Fluss nicht überschwemmen."},
            {"en": "Although the forecast was wrong, we were prepared.", "de": "Obwohl die Vorhersage falsch war, waren wir vorbereitet."},
            {"en": "Even if it gets dark, we keep hiking.", "de": "Auch wenn es dunkel wird, wandern wir weiter."},
            {"en": "Although it is humid, the evening is pleasant.", "de": "Obwohl es schwül ist, ist der Abend angenehm."},
            {"en": "Even if the temperature dropped, the plants would survive.", "de": "Selbst wenn die Temperatur sänke, würden die Pflanzen überleben."},
            {"en": "It was pouring; nevertheless they stayed outside.", "de": "Es goss in Strömen; trotzdem blieben sie draußen."},
            {"en": "Although the ice is thin, he skates on it.", "de": "Obwohl das Eis dünn ist, läuft er darauf Schlittschuh."},
            {"en": "Even if it is cloudy, we can see the mountains.", "de": "Auch wenn es bewölkt ist, können wir die Berge sehen."},
            {"en": "Although it thundered loudly, the dog stayed calm.", "de": "Obwohl es laut donnerte, blieb der Hund ruhig."},
            {"en": "Even if it froze tonight, the flowers would be fine.", "de": "Selbst wenn es heute Nacht fröre, wären die Blumen in Ordnung."},
            {"en": "Although there was a storm warning, they went out.", "de": "Obwohl es eine Sturmwarnung gab, gingen sie hinaus."},
            {"en": "It snowed heavily; nevertheless the roads stayed open.", "de": "Es schneite heftig; dennoch blieben die Straßen offen."},
            {"en": "Even if the rain stops, the ground stays wet.", "de": "Auch wenn der Regen aufhört, bleibt der Boden nass."},
            {"en": "Although the sky was grey, the day was warm.", "de": "Obwohl der Himmel grau war, war der Tag warm."},
            {"en": "Even if it were sunny, I would stay inside.", "de": "Selbst wenn es sonnig wäre, würde ich drinnen bleiben."},
            {"en": "Although it hailed, the car was not damaged.", "de": "Obwohl es hagelte, wurde das Auto nicht beschädigt."},
            {"en": "Even if a heatwave comes, we stay in the city.", "de": "Auch wenn eine Hitzewelle kommt, bleiben wir in der Stadt."},
            {"en": "It was windy; nevertheless we lit the fire.", "de": "Es war windig; trotzdem zündeten wir das Feuer an."},
            {"en": "Although the lake froze, nobody went skating.", "de": "Obwohl der See zufror, ging niemand Schlittschuh laufen."},
            {"en": "Even if it rained, the wedding would take place.", "de": "Selbst wenn es regnete, würde die Hochzeit stattfinden."},
            {"en": "Although clouds gathered, no rain fell.", "de": "Obwohl sich Wolken sammelten, fiel kein Regen."},
            {"en": "Even if the weather changes, our plan stays.", "de": "Auch wenn sich das Wetter ändert, bleibt unser Plan."},
            {"en": "It was stormy; nevertheless the ferry sailed.", "de": "Es war stürmisch; dennoch fuhr die Fähre."},
            {"en": "Although the morning was frosty, the afternoon was mild.", "de": "Obwohl der Morgen frostig war, war der Nachmittag mild."},
            {"en": "Even if the sky falls, a true friend stays.", "de": "Selbst wenn der Himmel einstürzt, bleibt ein wahrer Freund."},
        ],
    },

    ("B2", "shopping"): {
        "note": (
            "📖 Shopping — B2\n\n"
            "NEGATION & GRADING PARTICLES (precision)\n"
            "kein negates a noun (with ein/no article); nicht negates the rest:\n"
            "  Ich habe kein Geld. · Ich kaufe das nicht.\n"
            "Position of nicht: before the part it negates; at the END for the whole sentence:\n"
            "  Er kauft das Hemd nicht. vs Er kauft nicht das Hemd, sondern die Jacke.\n"
            "GRADING PARTICLES: sogar (even) · nur/bloß (only) · erst (not until) · "
            "schon (already) · fast/beinahe (almost) · kaum (hardly) · ausgerechnet (of all).\n"
            "• Das ist sogar im Angebot.  ·  Das Geschäft öffnet erst um zehn.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "I have no money.", "de": "Ich habe kein Geld."},
            {"en": "I am not buying that.", "de": "Ich kaufe das nicht."},
            {"en": "He is not buying the shirt.", "de": "Er kauft das Hemd nicht."},
            {"en": "He is not buying the shirt, but the jacket.", "de": "Er kauft nicht das Hemd, sondern die Jacke."},
            {"en": "That is even on sale.", "de": "Das ist sogar im Angebot."},
            {"en": "I only have ten euros.", "de": "Ich habe nur zehn Euro."},
            {"en": "The shop opens only at ten.", "de": "Das Geschäft öffnet erst um zehn."},
            {"en": "The store is already closed.", "de": "Das Geschäft ist schon geschlossen."},
            {"en": "The bag is almost free.", "de": "Die Tasche ist fast kostenlos."},
            {"en": "I hardly have any cash.", "de": "Ich habe kaum Bargeld."},
            {"en": "Of all days, the sale is today.", "de": "Ausgerechnet heute ist der Schlussverkauf."},
            {"en": "He bought not one but three shirts.", "de": "Er kaufte nicht ein, sondern drei Hemden."},
            {"en": "She does not like this dress at all.", "de": "Dieses Kleid gefällt ihr überhaupt nicht."},
            {"en": "Even the cheap shoes are sold out.", "de": "Sogar die billigen Schuhe sind ausverkauft."},
            {"en": "I only found out about the discount today.", "de": "Ich habe erst heute vom Rabatt erfahren."},
            {"en": "We have hardly any time to shop.", "de": "Wir haben kaum Zeit zum Einkaufen."},
            {"en": "The shop is not expensive, just popular.", "de": "Das Geschäft ist nicht teuer, nur beliebt."},
            {"en": "She bought almost everything in the store.", "de": "Sie kaufte fast alles im Laden."},
            {"en": "I do not need a new coat.", "de": "Ich brauche keinen neuen Mantel."},
            {"en": "He paid not with cash but with a card.", "de": "Er zahlte nicht mit Bargeld, sondern mit Karte."},
            {"en": "Even the salesperson was surprised.", "de": "Sogar der Verkäufer war überrascht."},
            {"en": "I have only been here once.", "de": "Ich war erst einmal hier."},
            {"en": "The product is hardly available anymore.", "de": "Das Produkt ist kaum noch erhältlich."},
            {"en": "She does not want the red one, but the blue one.", "de": "Sie will nicht das rote, sondern das blaue."},
            {"en": "The discount is only valid today.", "de": "Der Rabatt gilt nur heute."},
            {"en": "That is almost too good to be true.", "de": "Das ist fast zu schön, um wahr zu sein."},
            {"en": "They sell not only clothes but also shoes.", "de": "Sie verkaufen nicht nur Kleidung, sondern auch Schuhe."},
            {"en": "I did not see a single bargain.", "de": "Ich habe kein einziges Schnäppchen gesehen."},
            {"en": "He even haggled over the price.", "de": "Er handelte sogar um den Preis."},
            {"en": "The shop is open only on weekdays.", "de": "Das Geschäft ist nur werktags geöffnet."},
            {"en": "She had hardly entered when it closed.", "de": "Sie war kaum eingetreten, da schloss es."},
            {"en": "Of all things, the cheapest item broke.", "de": "Ausgerechnet das billigste Stück ging kaputt."},
            {"en": "I am not paying that much for a shirt.", "de": "So viel zahle ich nicht für ein Hemd."},
            {"en": "The store does not accept cash anymore.", "de": "Das Geschäft nimmt kein Bargeld mehr."},
            {"en": "Even online the prices are high.", "de": "Sogar online sind die Preise hoch."},
            {"en": "The delivery arrives only next week.", "de": "Die Lieferung kommt erst nächste Woche."},
            {"en": "He bought nothing, only looked around.", "de": "Er kaufte nichts, sah sich nur um."},
            {"en": "She almost forgot her wallet.", "de": "Sie hätte fast ihr Portemonnaie vergessen."},
            {"en": "We have not received the order yet.", "de": "Wir haben die Bestellung noch nicht erhalten."},
            {"en": "A good buyer asks not how much it costs, but whether it is worth it.", "de": "Ein guter Käufer fragt nicht, wie viel es kostet, sondern ob es sich lohnt."},
        ],
    },

    ("B2", "environment"): {
        "note": (
            "📖 Environment — B2\n\n"
            "NOMINAL STYLE + FUNCTION-VERBS (formal/academic register)\n"
            "Environmental and policy texts combine dense nouns, function-verbs and passive.\n"
            "Function-verbs here:\n"
            "  Maßnahmen ergreifen (take measures) · in Kraft treten (come into force) ·\n"
            "  Einfluss nehmen auf (influence) · zur Folge haben (result in) ·\n"
            "  in Angriff nehmen (tackle) · Verantwortung tragen (bear responsibility) ·\n"
            "  ins Leben rufen (launch/found).\n"
            "• Es müssen dringend Maßnahmen ergriffen werden.\n"
            "• Die Erderwärmung hat schwere Folgen.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "Urgent measures must be taken.", "de": "Es müssen dringend Maßnahmen ergriffen werden."},
            {"en": "The new law comes into force next year.", "de": "Das neue Gesetz tritt nächstes Jahr in Kraft."},
            {"en": "Industry influences the climate.", "de": "Die Industrie nimmt Einfluss auf das Klima."},
            {"en": "Global warming has serious consequences.", "de": "Die Erderwärmung hat schwere Folgen."},
            {"en": "We must tackle the problem now.", "de": "Wir müssen das Problem jetzt in Angriff nehmen."},
            {"en": "We have to have regard for nature.", "de": "Wir müssen Rücksicht auf die Natur nehmen."},
            {"en": "Everyone bears responsibility for the environment.", "de": "Jeder trägt Verantwortung für die Umwelt."},
            {"en": "The city launched a recycling program.", "de": "Die Stadt rief ein Recyclingprogramm ins Leben."},
            {"en": "Pollution results in health problems.", "de": "Die Verschmutzung hat Gesundheitsprobleme zur Folge."},
            {"en": "The protection of the forests is essential.", "de": "Der Schutz der Wälder ist wesentlich."},
            {"en": "Measures against waste were introduced.", "de": "Maßnahmen gegen Müll wurden eingeführt."},
            {"en": "The reduction of emissions is the goal.", "de": "Die Reduzierung der Emissionen ist das Ziel."},
            {"en": "The ban on plastic came into force.", "de": "Das Plastikverbot trat in Kraft."},
            {"en": "Climate change influences the whole planet.", "de": "Der Klimawandel nimmt Einfluss auf den ganzen Planeten."},
            {"en": "The clearing of forests has dramatic consequences.", "de": "Die Rodung der Wälder hat dramatische Folgen."},
            {"en": "The government must take responsibility.", "de": "Die Regierung muss Verantwortung tragen."},
            {"en": "The project was launched last year.", "de": "Das Projekt wurde letztes Jahr ins Leben gerufen."},
            {"en": "The use of solar energy is increasing.", "de": "Die Nutzung der Solarenergie nimmt zu."},
            {"en": "Strict measures were taken.", "de": "Es wurden strenge Maßnahmen ergriffen."},
            {"en": "The warming of the oceans alarms scientists.", "de": "Die Erwärmung der Ozeane alarmiert die Wissenschaftler."},
            {"en": "The recycling of materials saves resources.", "de": "Das Recycling von Materialien spart Ressourcen."},
            {"en": "We must tackle the energy crisis.", "de": "Wir müssen die Energiekrise in Angriff nehmen."},
            {"en": "The melting of the glaciers is accelerating.", "de": "Das Schmelzen der Gletscher beschleunigt sich."},
            {"en": "New regulations come into force in spring.", "de": "Neue Vorschriften treten im Frühjahr in Kraft."},
            {"en": "The pollution of the rivers must be stopped.", "de": "Die Verschmutzung der Flüsse muss gestoppt werden."},
            {"en": "Consumers influence the market.", "de": "Die Verbraucher nehmen Einfluss auf den Markt."},
            {"en": "The conservation of water is important.", "de": "Die Schonung des Wassers ist wichtig."},
            {"en": "Deforestation has irreversible consequences.", "de": "Die Abholzung hat unumkehrbare Folgen."},
            {"en": "Companies must bear more responsibility.", "de": "Die Unternehmen müssen mehr Verantwortung tragen."},
            {"en": "An initiative was launched to save bees.", "de": "Eine Initiative zur Rettung der Bienen wurde ins Leben gerufen."},
            {"en": "The protection of endangered species is urgent.", "de": "Der Schutz bedrohter Arten ist dringend."},
            {"en": "Effective measures must be taken immediately.", "de": "Es müssen sofort wirksame Maßnahmen ergriffen werden."},
            {"en": "The rise of sea levels threatens cities.", "de": "Der Anstieg des Meeresspiegels bedroht Städte."},
            {"en": "The agreement comes into force after ratification.", "de": "Das Abkommen tritt nach der Ratifizierung in Kraft."},
            {"en": "Air pollution results in respiratory diseases.", "de": "Die Luftverschmutzung hat Atemwegserkrankungen zur Folge."},
            {"en": "We must tackle climate change together.", "de": "Wir müssen den Klimawandel gemeinsam in Angriff nehmen."},
            {"en": "The preservation of biodiversity is crucial.", "de": "Die Erhaltung der Biodiversität ist entscheidend."},
            {"en": "Politics influences environmental protection.", "de": "Die Politik nimmt Einfluss auf den Umweltschutz."},
            {"en": "Future generations bear the burden of our decisions.", "de": "Künftige Generationen tragen die Last unserer Entscheidungen."},
            {"en": "The protection of the planet is the responsibility of all.", "de": "Der Schutz des Planeten ist die Verantwortung aller."},
        ],
    },

    ("B2", "advertising"): {
        "note": (
            "📖 Advertising — B2\n\n"
            "EMPHASIS & FOCUS STRUCTURES\n"
            "FRONTING (Vorfeld): put the focus first; the verb stays in position 2:\n"
            "• Diesen Preis bekommen Sie nur heute! · Genau das brauchen Sie.\n"
            "es as a placeholder opening (es-Vorfeld) to delay the subject:\n"
            "• Es lohnt sich, jetzt zu kaufen. · Es gibt kein besseres Angebot.\n"
            "zwar … aber (admittedly … but) — concede, then sell:\n"
            "• Das Produkt ist zwar teuer, aber es hält lange.\n"
            "nicht nur … sondern (auch) — intensify: Nicht nur günstig, sondern auch nachhaltig.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "You get this price only today!", "de": "Diesen Preis bekommen Sie nur heute!"},
            {"en": "That is exactly what you need.", "de": "Genau das brauchen Sie."},
            {"en": "It is worth buying now.", "de": "Es lohnt sich, jetzt zu kaufen."},
            {"en": "There is no better offer.", "de": "Es gibt kein besseres Angebot."},
            {"en": "The product is admittedly expensive, but it lasts long.", "de": "Das Produkt ist zwar teuer, aber es hält lange."},
            {"en": "Not only cheap, but also sustainable.", "de": "Nicht nur günstig, sondern auch nachhaltig."},
            {"en": "This quality you find nowhere else.", "de": "Diese Qualität finden Sie nirgendwo sonst."},
            {"en": "Today everything is half price.", "de": "Heute ist alles zum halben Preis."},
            {"en": "It pays to compare.", "de": "Es lohnt sich zu vergleichen."},
            {"en": "Admittedly it is small, but it is powerful.", "de": "Es ist zwar klein, aber leistungsstark."},
            {"en": "Exactly this product made us famous.", "de": "Genau dieses Produkt machte uns berühmt."},
            {"en": "Never was shopping so easy.", "de": "Nie war Einkaufen so einfach."},
            {"en": "There are many reasons to choose us.", "de": "Es gibt viele Gründe, uns zu wählen."},
            {"en": "Only with us do you get this guarantee.", "de": "Nur bei uns bekommen Sie diese Garantie."},
            {"en": "The price is admittedly high, but the quality convinces.", "de": "Der Preis ist zwar hoch, aber die Qualität überzeugt."},
            {"en": "Not only fast, but also reliable.", "de": "Nicht nur schnell, sondern auch zuverlässig."},
            {"en": "This offer you should not miss.", "de": "Dieses Angebot sollten Sie nicht verpassen."},
            {"en": "Right now is the best time to buy.", "de": "Genau jetzt ist die beste Zeit zu kaufen."},
            {"en": "It is no coincidence that we are number one.", "de": "Es ist kein Zufall, dass wir die Nummer eins sind."},
            {"en": "With this card you save every day.", "de": "Mit dieser Karte sparen Sie jeden Tag."},
            {"en": "The design is admittedly simple, but elegant.", "de": "Das Design ist zwar schlicht, aber elegant."},
            {"en": "Not only for you, but for the whole family.", "de": "Nicht nur für Sie, sondern für die ganze Familie."},
            {"en": "Such service you experience only here.", "de": "So einen Service erleben Sie nur hier."},
            {"en": "Rarely has a product been so popular.", "de": "Selten war ein Produkt so beliebt."},
            {"en": "It is time for something new.", "de": "Es ist Zeit für etwas Neues."},
            {"en": "Only the best is good enough for you.", "de": "Nur das Beste ist gut genug für Sie."},
            {"en": "Admittedly it costs more, but it saves energy.", "de": "Es kostet zwar mehr, aber es spart Energie."},
            {"en": "Not only today, but every day low prices.", "de": "Nicht nur heute, sondern jeden Tag niedrige Preise."},
            {"en": "This chance comes only once.", "de": "Diese Chance kommt nur einmal."},
            {"en": "Here begins your new life.", "de": "Hier beginnt Ihr neues Leben."},
            {"en": "It is worth taking a look.", "de": "Es lohnt sich, einen Blick zu werfen."},
            {"en": "Faster than ever you reach your goal.", "de": "Schneller als je erreichen Sie Ihr Ziel."},
            {"en": "The model is admittedly older, but proven.", "de": "Das Modell ist zwar älter, aber bewährt."},
            {"en": "Not only stylish, but also practical.", "de": "Nicht nur stilvoll, sondern auch praktisch."},
            {"en": "This experience you will never forget.", "de": "Dieses Erlebnis werden Sie nie vergessen."},
            {"en": "Nowhere else will you find such variety.", "de": "Nirgendwo sonst finden Sie solche Vielfalt."},
            {"en": "It is your decision that counts.", "de": "Es ist Ihre Entscheidung, die zählt."},
            {"en": "Only quality creates trust.", "de": "Nur Qualität schafft Vertrauen."},
            {"en": "Admittedly the brand is new, but convincing.", "de": "Die Marke ist zwar neu, aber überzeugend."},
            {"en": "Not the price but the value is what matters.", "de": "Nicht der Preis, sondern der Wert ist entscheidend."},
        ],
    },

    ("B2", "government"): {
        "note": (
            "📖 Government and Society — B2\n\n"
            "INDIRECT SPEECH — the full system (die vollständige indirekte Rede)\n"
            "Formal reports relay statements in Konjunktiv I; switch to Konjunktiv II when "
            "K I looks like the indicative.\n"
            "PRESENT: er sagt, er sei / habe / komme / könne …\n"
            "PAST (one perfect form for all past tenses): habe/sei + Partizip II:\n"
            "  Direct: Ich kam zu spät. → Er sagt, er sei zu spät gekommen.\n"
            "FUTURE: er sagt, er werde kommen.\n"
            "Questions: ob (yes/no) or W-word, verb to the END:\n"
            "  Er fragt, ob die Sitzung beginne. · Sie fragt, wann er komme.\n\n"
            "Tap Start: 40 sentences, easy → harder. 💪"
        ),
        "questions": [
            {"en": "He says he is the minister.", "de": "Er sagt, er sei der Minister."},
            {"en": "She says she has a plan.", "de": "Sie sagt, sie habe einen Plan."},
            {"en": "He says he will come to the session.", "de": "Er sagt, er werde zur Sitzung kommen."},
            {"en": "He says he arrived too late.", "de": "Er sagt, er sei zu spät gekommen."},
            {"en": "She says she has signed the law.", "de": "Sie sagt, sie habe das Gesetz unterschrieben."},
            {"en": "He asks whether the session is beginning.", "de": "Er fragt, ob die Sitzung beginne."},
            {"en": "She asks when he is coming.", "de": "Sie fragt, wann er komme."},
            {"en": "They say they have voted.", "de": "Sie sagen, sie hätten abgestimmt."},
            {"en": "The minister says the reform is necessary.", "de": "Der Minister sagt, die Reform sei notwendig."},
            {"en": "He says he did not know that.", "de": "Er sagt, er habe das nicht gewusst."},
            {"en": "She claims she was not there.", "de": "Sie behauptet, sie sei nicht da gewesen."},
            {"en": "The report says the economy will grow.", "de": "Der Bericht sagt, die Wirtschaft werde wachsen."},
            {"en": "He says the citizens have the right to vote.", "de": "Er sagt, die Bürger hätten das Wahlrecht."},
            {"en": "She asks whether the budget has been approved.", "de": "Sie fragt, ob das Budget genehmigt worden sei."},
            {"en": "He explains that the decision was made yesterday.", "de": "Er erklärt, die Entscheidung sei gestern getroffen worden."},
            {"en": "The president says he will resign.", "de": "Der Präsident sagt, er werde zurücktreten."},
            {"en": "They say they had already warned the government.", "de": "Sie sagen, sie hätten die Regierung bereits gewarnt."},
            {"en": "She says the taxes will be lowered.", "de": "Sie sagt, die Steuern würden gesenkt."},
            {"en": "He asks how the money was spent.", "de": "Er fragt, wie das Geld ausgegeben worden sei."},
            {"en": "The chancellor says she understands the concerns.", "de": "Die Kanzlerin sagt, sie verstehe die Sorgen."},
            {"en": "He claims he has always told the truth.", "de": "Er behauptet, er habe immer die Wahrheit gesagt."},
            {"en": "She says the meeting was postponed.", "de": "Sie sagt, die Sitzung sei verschoben worden."},
            {"en": "They say they will support the proposal.", "de": "Sie sagen, sie würden den Vorschlag unterstützen."},
            {"en": "He says the law came into force last week.", "de": "Er sagt, das Gesetz sei letzte Woche in Kraft getreten."},
            {"en": "The official asks whether the documents are complete.", "de": "Der Beamte fragt, ob die Unterlagen vollständig seien."},
            {"en": "She explains that the funds have been distributed.", "de": "Sie erklärt, die Mittel seien verteilt worden."},
            {"en": "He says he cannot answer that question.", "de": "Er sagt, er könne diese Frage nicht beantworten."},
            {"en": "They say the protests were peaceful.", "de": "Sie sagen, die Proteste seien friedlich gewesen."},
            {"en": "The minister says he will examine the case.", "de": "Der Minister sagt, er werde den Fall prüfen."},
            {"en": "She asks why the project was cancelled.", "de": "Sie fragt, warum das Projekt abgesagt worden sei."},
            {"en": "He claims the figures are correct.", "de": "Er behauptet, die Zahlen seien korrekt."},
            {"en": "They say they have fulfilled their promises.", "de": "Sie sagen, sie hätten ihre Versprechen erfüllt."},
            {"en": "She says the new rules will apply from January.", "de": "Sie sagt, die neuen Regeln würden ab Januar gelten."},
            {"en": "He explains that the vote will take place tomorrow.", "de": "Er erklärt, die Abstimmung werde morgen stattfinden."},
            {"en": "The report states that unemployment has fallen.", "de": "Der Bericht besagt, die Arbeitslosigkeit sei gesunken."},
            {"en": "He asks whether the citizens were informed.", "de": "Er fragt, ob die Bürger informiert worden seien."},
            {"en": "She says she has done everything in her power.", "de": "Sie sagt, sie habe alles in ihrer Macht Stehende getan."},
            {"en": "They claim they were misunderstood.", "de": "Sie behaupten, sie seien missverstanden worden."},
            {"en": "The president says the country will recover.", "de": "Der Präsident sagt, das Land werde sich erholen."},
            {"en": "A government, it is said, should serve the people, not rule them.", "de": "Eine Regierung, so heißt es, solle dem Volk dienen, nicht über es herrschen."},
        ],
    },

    # === append new lessons above this line ===
}
