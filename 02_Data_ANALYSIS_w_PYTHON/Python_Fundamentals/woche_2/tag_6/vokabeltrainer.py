# Aufgabe:
# Bei User-Eingabe des deutschen Wortes bekommt er die englische Entsprechung des Wortes.
# Das Programm bzw. der Userinput läuft in einem while-Loop und
# terminiert erst bei Eingabe des Buchstabens X.

# Kommandozeile Beispiele
# „Hallo, Willkommen beim Alfatraining Vokabeltrainer! Bitte gebe ein deutsches Wort ein!“
# Blatt
# „Tut mir leid, dieses Wort befindet sich nicht in meinem Wortschatz. „
# Haus
# „house“

# Es soll ein einfacher Vokabeltrainer DE EN  programmiert werden.
# Die Vokabelliste ist als dict hinterlegt und sieht in einfacher Form so aus:
# De_en = {
# 	„Haus“: „house“,
#	 „Straße“: „street“
# }
# Dieses Dict kann unbegrenzt erweitert werden.
de_en = {
    "Haus": "house",
    "Straße": "street",
    "Auto": "car",
}
def translator(wort):
    if wort.capitalize() in de_en:
        print(de_en[wort.capitalize()])
    else:
        print("Tut mir leid, dieses Wort befindet sich nicht in meinem Wortschatz.")

while True:
    user_input = input("Hallo, Willkommen beim Alfatraining Vokabeltrainer!"
                       " Bitte gebe ein deutsches Wort ein! ODER zum Abbruch 'x': ")
    if user_input == "x":
        print("Auf Wiedersehen")
        break
    translator((user_input))