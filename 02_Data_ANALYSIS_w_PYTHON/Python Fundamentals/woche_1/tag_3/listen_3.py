# Sortieren
names = ["Dieter", "Bernd", "Martin"]
print(names, id(names))

names.sort()
print(names, id(names))

# Aufsteigend Sortieren
numbers = [12, 3, 4, 99, 2, 0.2]
numbers.sort()
print(numbers)

# Absteigend Sortieren
numbers = [12, 3, 4, 99, 2, 0.2]
numbers.sort(reverse=True)
print(numbers)

# 2D Listen
personen = [
    ["Arne", "Dudel"],
    ["Ali Ibrahim", "Yilmaz"],
    ["Deniz", "Gürzoglu"]
]
personen.sort()
print(personen)

