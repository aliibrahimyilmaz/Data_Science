# aus Liste einen Tuple erstellen
liste = [1, 2, 3, 4]
tu = tuple(liste)
print(tu)

# aus Tuple eine Liste erstellen
liste = list(tu)
print(liste)

# aus string einen Tuple erstellen
a = "berlin"
print(id(a))
a = tuple(a)
print(id(a))
print(a)