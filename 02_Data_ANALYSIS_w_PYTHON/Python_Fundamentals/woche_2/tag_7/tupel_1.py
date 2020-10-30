# tupel definieren
x = 1,
print(type(x))

# tupel kann auch mit Klammer definiert werden
y = (2, 3)

# tupel über index addressieren
print("Wert von y an index 1: ", y[1])

# über einen tupel iterieren
for element in y:
    print("element : ", element)

# tupel als key von Dictionary
d = {}
d[1, 2] = "test"
print(d)
print(d[1, 2])