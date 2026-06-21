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

    # === append new lessons above this line ===
}
