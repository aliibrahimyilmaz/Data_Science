erste_liste = [1, 3, "hallo"]
print(erste_liste)
print(type(erste_liste))

fruits = ["apple", "banana", "cherry", "pineapple"]
print(fruits)

erster_index = fruits[1]
print("Element an Index 1: ", fruits[1])
print(type(erster_index))

erster_index = fruits[1][3]
print("Element an Index 1: ", fruits[1][3])
print(type(erster_index))

# len() isr für alle seq. Datentypen
print("Länge der Liste: ", len(fruits))

# index von Wert zurückgeben lassen
print("Banana steht an Index: ", fruits.index("banana"))

fruits[0] = "Strawberry"  # apple geht weg
print("neue Liste: ", fruits)

# Liste erweitern geht mit append()
fruits.append("Melon")
print("Liste Fruits mit Melon: ", fruits)

# Liste insert(index, Value): Element an Index einfügen, die anderen werden verschoben
fruits.insert(1, "lemon")
print(fruits)

# Liste anfügen an fruits_Liste anhängen
fruits2 = ["coconut", "strawberry", "apple"]
fruits = fruits + fruits2
print("neue fruits", fruits)
print(id(fruits))

# weitere Möglichkeit, liste anzuhängen
fruits.extend(["Orange", "Quitte"])  # kann man mehrere sachen append
print("neue fruits", fruits)
print("id der neuen Liste:", id(fruits))

# Prüfen, ob Element in Liste
if "coconut" in fruits:
    print("ja, Coconut ist in der Liste fruits enthalten")

# Elemente aus der Liste addressieren
a = fruits[0]

# letztes Element aus Liste holen und aus Liste löschen
b = fruits.pop()
print("b mit pop()", b)
print(fruits)

# Element mit index aus Liste holen und aus Liste löschen
b = fruits.pop(0)
print("b mit pop(0)", b)
print(fruits)

# Aufgabe
# Hänge an die leere Liste die drei Städte "München", "Berlin" und "Hamburg" an.
# Prüfe, an welcher Stelle "Hamburg" steht. Lösche Hamburg aus der Liste
cities = []
cities.extend(["München", "Berlin", "Hamburg"])
print(cities)
cities.index("Hamburg")
cities.pop()
print(cities)

# https://www.programiz.com/python-programming/methods/list

print(fruits)
# Weist man einer Variablen eine Liste zu, speichert man die Liste nicht.
a = [1, 2, 3]
b = a  # das heißt nicht eine Kopie
a.append(4)
print(b) # a ist verändert sowie b, weil Beide gleiche Referenz benutzen

