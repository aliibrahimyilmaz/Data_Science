adressbuch = ["Moskau", "Dortmund", "Tokyo"]
# adressbuch[0] Moskau
print(id(adressbuch))

counter = 0
for city in adressbuch:
    print("City: ", city)
    print("ID der Variable city: ", id(city))
    city.upper()  # bringt nichts
    counter = counter + 1
    print(f"Element an Counter {counter}", adressbuch[counter-1])

print(adressbuch)

# Index pro Iteration
x = enumerate(adressbuch)
print(x.__next__())  # enumerate Objekt gibt pro Iteration einen Tupel zurück
print(x.__next__())  # (1, 'Dortmund')
print(x.__next__())  # (2, 'Tokyo')

for index, city in enumerate(adressbuch):
    print("City: ", city)
    print(index)
    print("ID der Variable city: ", id(city))
    adressbuch[index] = adressbuch[index].upper()
    print(adressbuch[index])
    if city == "Dortmund":
        break  # Iteration abbrechen

print(adressbuch)
print(id(adressbuch))

# mit continue aus dem aktuellen Loop und zur nächsten Iteration
for i in [1, 2, 3, 4, 5, 6]:
    if i % 2 == 0:
        print(i ** 2)
        continue
    print("i war ", i)