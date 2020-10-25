a = True
if a:
    print("a ist wahr")

a = 1
b = 2
if a < b:
    # das wird ausgeführt, wenn a kleiner als b ist
    print("a ist kleiner")

if "Hamburg" == "Hamburg":
    print("der Stadt is gleich")

a = "Hamburg"
if a != b or a == "Hamburg":
    print("Städte sind ungleich")

# AUFGABE:
a = None  # None ist auch Falsch gewertet
b = 4
if not a or not b:
    print("not None ist wahr")
    print(a)

if "a":  # False
    print(1)

if "":  # False
    print(1)

# Logisch nicht wahr
 # der boolschen Wert False
 # null werte (0, 0.0)
 # leere Zeichenkette
 # leere Listen, leere Tupel
 # leere Dict
 # spezielle Wert None

# Hinweis : negative Zahlen zählt als True

x = "test"
if x.find("y"): # index methode ist besser, weil find -1 ergibt
    print("ja")

# Aufgabe
a = 10
b = 3
# prüfe, ob die Summe von a und b kleiner als 8 ist ODER ob b größer als 2 ist.
# Gib eine Meldung aus, wenn True
summe = a + b
if summe < 8 or b > 2:
    print("die Summe von a und b ist {} und es ist kleiner als 8 ODER b:{} ist größer als 2".format(summe, b))

# Membership-Operator - Teilmengenoperator
if "a" in "amerika":
    print("ja")

if "A" in "amerika":  # case_sensitive
    print("ja")

if "ab" in "amerika":
    print("ja")

print(ord("a"))  # 97 ZeichenSatz-UNICODE Project
print(ord("A"))  # 65 ZeichenSatz-UNICODE

# Liste ist auch eine Sequenz
fruit = "apple"
fruits = ["apple", "cherry", "banana"]
if fruit in fruits:
    print("ja, das ist in fruits enhaltet")


