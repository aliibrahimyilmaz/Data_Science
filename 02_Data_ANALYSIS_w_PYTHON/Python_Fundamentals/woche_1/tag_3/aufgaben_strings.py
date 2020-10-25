import random
'''
Übungsaufgaben zu Strings

1. Gegeben sind zwei Strings. Verkette sie zu einem:
'''
a = "A"
b = "C"
c = a + b
print(c)
d = "Banana"
e = "rama"
f = d + e
print(f)

'''
2. Gegeben sind zwei Strings. Prüfe, ob b in a vorkommt
'''
a = "Bellavista"
b = "vis"
if b in a:
    print(f"ja. {b} ist in {a}")
a = "Rom"
b = "Rome"
if b in a:
    print(f"ja. {b} ist in {a}")
else:
    print("Nein")

'''3. String Ersetzung
Ersetze alle Vorkommen von b in a durch c'''

a = "Bellavista"
print("old a: ", a)
b = "Bella"
c = "Buena"
a = a.replace(b, c)
print("new a", a)

a = "Nordpol"
b = "pol"
c = "kap"
a = a.replace(b, c)
print("new a", a)

'''4. String Slicing
Bereinige folgende Zeichenketten von X. Nicht die replace-Methode nutzen'''
a = "ABAX"
print(a[:-1])
a = "XXXAAA"
print(a[3:])
a = "Xconfig.pyX"
print(a[1:-1])
a = "XXXAAAXXX"
print(a[3:6])
a = "XaXXxEXX22222X"
print(a[1] + a[5] + a[8:-1])

'''5. Random String
Erzeuge einen Zufallsstring der Länge 7 (oder variabel) im Wertebereich
von 65 - 90 und 97 bis 122 entsprechend der Ascii Tabelle.
Nutze dazu das Random-Modul und die builtin-Funktion chr().
Diese Funktion erzeugt aus einer Ganzzahl eine Zeichenentsprechung zb.
61 ist das große A
http://www.asciitable.com/'''
print(type(chr(65)))
a = ""
for i in range(2):
    a = a + chr(random.randint(65, 90))
    for j in range(2):
        a = a + chr(random.randint(97, 122))
a = a + chr(random.randint(65, 90))
print(a)