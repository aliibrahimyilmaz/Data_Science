'''
Gruppenaufgabe 1.1

Der Trump Parser

Für unser Auftraggeber, die Newscom-Presseagentur, sollen wir einen Parser entwickeln, der
einige Reden von Donald Trump einliest und nach gewissen Kriterien filtert oder ausgibt.

Parsen bedeutet in diesem Zusammenhang: Text aufsplitten, von Leer- Satz- und Steuerzeichen bereinigen und
in einer Liste verfügbar machen. Hinweis: they're ist kein Wort!

Über ein input soll der User einen Modus wählen können. In Abhängigkeit der Eingabe startet der Parser.

Der Parser soll folgende Modi haben:

1. Modus SENTENCE

der Datei-Content wird in Sätze gesplittet. Ein Punkt gilt als Ende eines Satzes.
Wenn das eingegebene Suchwort in diesem Satz enthalten ist, drucke den Satz aus

Die Usereingabe ist festgelegt und soll wie folgt aussehen:
SEN <SUCHWORT>

z.b.
SEN America

soll nur Sätze ausdrucken, in denen America vorkommt.

Hinweise: nutze für diesen Modus split(), for-loop, in-element-Operator

2. Modus WORD

der Datei-Content wird in Wörter gesplittet. Jedes Wort sollte von Kommas und Punkten bereinigt werden.
Wenn das eingegebene Suchwort in diesem Wort enthalten ist, füge es einer Ergebnis-Liste hinzu (zb. word_list)
Diese Liste sollte von doppelten Elementen bereinigt werden. Diese Liste muss sortiert ausgegeben werden.

Die Usereingabe ist festgelegt und soll wie folgt aussehen:
WORD <SUCHWORT>

z.b.
WORD Am

es sollen sich nur Wörter in der liste befinden, die Am beinhalten.
'Americans', 'America', 'Amendment', [..]

Hinweise: nutze für diesen Modus split(), for-loop, in-element-Operator

3. Modus TOP

Ninja-Level

der Datei-Content wird in Wörter gesplittet. Jedes Wort sollte von Kommas und Punkten bereinigt werden.
Wenn das eingegebene Suchwort in diesem Wort enthalten ist, füge es einer Ergebnis-Liste hinzu (zb. word_list)
Gesucht ist die TOP-TEN aller Wortnennungen inklusive Anzahl der Vorkommen. Es sollen nur Worte
berücksichtigt werden, die > 5 Zeichen haben, um zumindest Pronomen und Füllwörter etwas auszuschließen.
Hierbei bitte Groß- und Kleinshreibung NICHT beachten (case-insensitive)

Die Usereingabe ist festgelegt und soll wie folgt aussehen:
TOP

z.b.
TOP

[('people', 964), ('because', 762),

Hinweise: nutze für diesen Modus split(), for-loop, in-element-Operator, sorted.
Für diese Aufgabe muss der Datentyp Dict verwenden werden. Dict ist ein Key-Value-Pair (Hashmap)

final_list = {}
final_list["america"] = 1
final_list["america"] += 1
# america ist der Key, 1 der Value. Der Value kann hochgezählt (inkrementiert) werden

Hilfreiche Artikel
https://kite.com/python/answers/how-to-increment-a-value-in-a-dictionary-in-python
https://thomas-cokelaer.info/blog/2017/12/how-to-sort-a-dictionary-by-values-in-python/

HINWEIS:
In der Entwicklungsphase den geladenen Text-Content auf 500 Zeichen kürzen.
content = file.read()[0:500]
'''
from pprint import pprint
file = open("trump_speeches.txt", "r", encoding="utf-8" )
content = file.read()
search = input("Bitte gebe deine Schlüssel Wort und Suchttext: ")
schlüssel = search.split()[0]
text = search.split()[1]

# MODUS: SENTENCE
if schlüssel == "SEN":
    sentence_list = content.split('.')
    sen_list = []
    for sen in sentence_list:
        if text in sen:
            sen_list.append(sen.strip())
    pprint(sen_list)
    print(len(sen_list))

# MODUS: WORD
elif schlüssel == "WORD":
    # bereinigen
    content = content.replace("?", "").replace("[", "").replace("]", "").replace("´", " ").replace("'", " ")\
        .replace('"', "").replace("-", " ").replace("\n", " ").replace("\t", " "). replace(",", "").replace("’", " ")\
        .replace(".", "").replace("”", "").replace("“", "").replace("–", "")
    word_list = content.split()
    search_word_list = []
    for w in word_list:
        if text in w:
            search_word_list.append(w.strip())
    pprint(search_word_list)
    print(len(search_word_list))

# MODUS: TOP
elif schlüssel == "TOP":
    # BEREINIGEN
    content = content.replace("?", "").replace("[", "").replace("]", "").replace("´", " ").replace("'", " ") \
        .replace('"', "").replace("-", " ").replace("\n", " ").replace("\t", " ").replace(",", "").replace("’", " ") \
        .replace(".", "").replace("”", "").replace("“", "").replace("–", "")
    word_list = content.split()
    search_word_list = []
    # SUCHEN
    for w in word_list:
        if text in w:
            search_word_list.append(w.strip())
    # ZÄHLEN
    counter = {}
    for element in search_word_list:
        if element in counter:
            counter[element] += 1
        else:
            counter[element] = 1
    sorted_top = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    pprint(sorted_top)



