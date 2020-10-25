a = [1, 2, 3, 4, 5]

# range(start, stop-1, Schrittweite) Funktion erzeugt ein Range Objekt
a = range(1,11)  # 10 ist exclusive
print(type(a), a)

for x in a:
    print(x)

b = range(1, 11, 2)  # [:11]
for x in b:
    print(x)

# https://www.python-kurs.eu/python3_listen.php