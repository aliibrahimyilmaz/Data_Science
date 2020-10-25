'''Übungsaufgaben zu Listen.

1. Iteration über Liste
Iteriere über Liste und gebe die Elemente aus!
Zusatz: gebe zusätzlich den enstprechenden Index aus, zb. für Banane den Index 0'''
fruits = ["Banane", "Apfel", "Kirsche"]
for indx, element in enumerate(fruits):
    print(element, indx)

'''2. Filtern einer Liste 1
Erstelle aus einer gegebenen Liste eine neue Liste filtered_fruits.
Die neue Liste darf nur Elemente enthalten, die mit einem großen B anfangen.'''
fruits = ["Banane", "Apfel", "Kirsche", "Birne"]
filtered_fruits = []
for i in fruits:
    if i[0] == "B":
        filtered_fruits.append(i)
print(filtered_fruits)

'''3. Filtern einer Liste 2
Erstelle aus einer gegebenen Liste eine neue Liste filtered_numbers.
Die neue Liste darf nur Elemente enthalten, die größer als 5 sind und kleiner als 100.
Die filtered_numbers-Liste muss sortiert ausgegeben werden.'''
numbers = [1, 4, 5, 2, 42, 2, 1, 99, 23, 23]
filtered_numbers = []
for i in numbers:
    if i >= 100:
        continue
    elif i <= 5:
        continue
    else:
        filtered_numbers.append(i)
filtered_numbers.sort()
print(filtered_numbers)

'''4. Listeninhalt prüfen
Über eine Eingabeaufforderung (input()) soll der User einen String-Wert eingeben.
Danach wird geprüft, ob sich dieser Wert in der Liste befindet.'''
symbols = ["AA", "CA", "DD", "CAS"]
user_input = input("Bitte gebe einen groß geschiriebene String-Wert!: ")
if user_input in symbols:
    print("ja")
else:
    print("nein")

'''5. das letzte Element
Gegeben ist eine Liste, die auch leer sein kann.
Prüfe, ob sich mindests ein Element in der Liste befindet
und printe das letzte Element in der Liste.'''
symbols = ["B", "C"]
symbols2 = []  # Das ist als Falsch angenommen
if symbols2:
    print("letzte Element: ", symbols2[-1])
else:
    print("Das ist eine leere Liste")

'''6. erlaubte Werte
Gegeben sind zwei Listen:
eine Ausgangsliste a und eine Liste mit erlaubten Werten allowed_values.
Prüfe für jedes Element in a, ob es in der erlaubten Liste enthalten ist,
und füge es einer neuen Liste c hinzu.'''
a = [50, 100, 40, 20, 200, 50, 100, 10]
allowed_values = [50, 100, 200]
c = [] # sollte nur 50, 100 und 200 enthalten
for i in a:
    if i in allowed_values and i not in c:
        c.append(i)
print("allowed values: ", c)

'''7. Bereinigen von Listenelementen
Gegeben ist eine Liste a mit String-Elementen.
Bereinige diese Elemente von _ (underscore) und speichere sie in einer neuen Liste.
Leere Elemente sollen nicht in die neue Liste'''
a = ["x_x", "alpha_beta", "_"]
c = []  # [xx, alphabeta]
for i in a:
    new = i.replace("_", "")
    if new == "":
        continue
    c.append(new)
print(c)

'''8. Bereinigen von Listen 2
Gegeben ist eine Liste a mit String-Elementen.
Bereinige diese Elemente von Whitespace und Steuerzeichen.
Entferne alle x aus den Strings.'''
a = ["haxlt ", "\nandx", "\tcatch ", " xfire "]  # ["halt", "and", "catch", "fire"]
c = []
for i in (a):
    new = i.replace("\t", '').replace("\n", '').replace(' ', '').replace('x', '')
    c.append(new)
print(c)

'''9. Zusammenführen von Listen
Gegeben sind zwei Listen a und b, wobei Liste a eine variable Länge aufweisen kann
(auch leere Mengen sind erlaubt) und Liste b immer eine Länge von 5 Elementen hat.
a = ["A", "B", "C", "D", "E", "F"]
b = [1, 2, 3, 4, 5]
Führe diese beiden Listen zu einer zusammen, und zwar so,
dass jeweils der selbe Index zusammengeführt wird.
Ist a kleiner als b, wird die Zusammenführung entsprechend reduziert.
Ist a größer als b, werden die überschüssigen Elemente ignoriert.
   Beispiele:
c = ["A1", "B2", "C3"] (wenn a ["A", "B", "C"]
c = ["A1"] (wenn a["A"])
c = [] (wenn a[])
c = ["A1", "B2", "C3", "D4", "E5"] wenn  ["A", "B", "C", "D", "E", "F"]'''

a = ["A", "B", "C"]
b = [1, 2, 3, 4, 5]
if len(a) <= len(b):
    print(b[:len(a)])
else:
    print(b)



