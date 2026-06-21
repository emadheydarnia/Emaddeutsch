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

    # === append new lessons above this line ===
}
