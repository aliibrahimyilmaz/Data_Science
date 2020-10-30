# https://fahrweg.dbnetze.com/resource/blob/1355946/b11c535e55adddd572ffae700f3dfa48/rw_481-0101A01-data.pdf
# Funkalphabet Übersetzer
# Worte sollen in das deutsche Funk-Alphabet übersetzt werden.
# Hans
# Heinrich – Anton – Nordpol - Siegfried

#with open("NATO_alphabet.txt", "r", encoding="utf-8") as file:
with open("buchstabiertafel.txt", "r", encoding="utf-8") as file:
    word_list = []
    for zeile in file:  # alle Zeilen sind getrennt
        word_list.append(zeile.strip().split("\n"))

# Erstellung eine Dict
print(word_list)
alphabet = []
word = []
for element in word_list:
    alpha, beta = element[0].strip().split()
    alphabet.append(alpha)
    word.append(beta)
print(len(alphabet), alphabet)
print(len(word), word)
tafel_dict = dict(zip(alphabet, word))
print(tafel_dict)


def translator(user_input):
    """User-Eingabe wird in das Funkalphabet übertragen und zurückgegeben"""
    alpha_list = list(user_input.upper().strip())
    funk_list = []
    for element in alpha_list:
        funk_list.append(tafel_dict[element])
    result = "-".join(funk_list)
    return result


# Übertragung in das Funkalphabet
while True:
    user_input = input("Hallo, Willkommen beim Alfatraining Funkalphabet Übersetzer! Bitte gebe ein Wort ein! ODER zum Abbruch 'q': ")
    if user_input.lower() == "q":
        print("Auf Wiedersehen")
        break
    print(translator(user_input))

# Zusatzaufgabe:
# Im Programm gibt es eine Konfigurations-Variable, anhand der sich das Alphabet umschalten lässt,
# z.b. in das Nato-Funkalphabet (Alfa, Bravo, Charlie….)