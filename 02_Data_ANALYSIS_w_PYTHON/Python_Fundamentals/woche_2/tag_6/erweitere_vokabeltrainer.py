# https://quizlet.com/94137074/top-2000-englishgerman-die-2000-wichtigsten-worter-englischdeutsch-flash-cards/
# es besteht aus 2000 Wörter, wegen der wiederholenden Wörter nur 1790 benutz.
# .txt datei isr hier geöffnet
with open("eng_de_words.txt", "r", encoding="utf-8") as file:
    word_list = []
    for zeile in file:  # alle Zeilen sind getrennt
        word_list.append(zeile.strip().split("\n"))

#  Erstellung eine DE-ENG dict
print(word_list)
eng_word = []
de_word = []
counter = 0
for element in word_list:
    if counter % 3 == 0:
        eng_word.append(element[0])
    elif counter % 3 == 1:
        de_word.append(element[0])
    else:
        pass
    counter += 1
print(len(eng_word), eng_word)
print(len(de_word), de_word)

# Wie viele gleiche Wörter haben wir in de_word Liste?
counter = {}
for element in de_word:
    if element in counter:
        counter[element] += 1
    else:
        counter[element] = 1
sorted_top = sorted(counter.items(), key=lambda item: item[1], reverse=True)
print(sorted_top)

wiederholung = 0
for element in sorted_top:
    if element[1] > 1:
        wiederholung = wiederholung + element[1] - 1
print(wiederholung)

# Nach der Trennung haben wir hier zwei Liste als dict gebunden
zip_objekt = zip(de_word, eng_word)
de_eng_dict = dict(zip_objekt)
print(len(de_eng_dict), de_eng_dict)

# Sorted Dict nach Deutsch
de_en = {k: v for k, v in sorted(de_eng_dict.items(), key=lambda item: item[0])}
print(len(de_en), de_en)

# Unser Translator
def translator(wort):
    if wort.capitalize() in de_en:
        print(de_en[wort.capitalize()])
    elif wort in de_en:
        print(de_en[wort])
    elif wort.lower() in de_en:
        print(de_en[wort.lower()])
    else:
        print("Tut mir leid, dieses Wort befindet sich nicht in meinem Wortschatz.")

while True:
    user_input = input("Hallo, Willkommen beim Alfatraining Vokabeltrainer!"
                       " Bitte gebe ein deutsches Wort ein! ODER zum Abbruch 'x': ")
    if user_input == "x":
        print("Auf Wiedersehen")
        break
    translator((user_input))


