# string methoden
# https://www.w3schools.com/python/python_ref_string.asp
# strings sind unveränderlich. Daher erzeugen (create) diese String-Methoden immer einen neuen String.
test = "hamburg"
test = test.upper()
print(test)

# ersetze alle a durch b
string = "ac/ac"
string = string.replace("/", "")
print(string)
print(string.find("c"))
print(string.find("d"))
print(string.index("c"))
# print(string.index("d")) # Fehler
string = "a-b-c-d-e"
print(string.split("-"))
str4 = "alfatraining"
print(list(str4))


# Aufgabe: Speichere das Ergebnis der Integerdivision von a (=34) und b(=5) in der Variable c und
# konvertiere das Ergebnis nach string.
a = 34
b = 5
c = a // b
print(str(c))
print(type(str(c)))

# String in Zahl konvertieren mit der Funktion int()
user_input = "3"
zahl = int(user_input)
print(zahl)
