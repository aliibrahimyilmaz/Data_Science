planeten = [
"Merkur",
"Venus",
"Erde",
"Mars",
"Jupiter",
"Saturn",
"Uranus",
"Neptun"
]
print(planeten[0:2])
print(planeten[:-2])

# Aufgabe: alle Planeten aus der Liste in einer neuen Liste speichern, doe mit M oder N anfangen
# 1.Lösung:
c = []
for i in planeten:
    if i[0] == "M" or i[0] == "N":
        c.append(i)
print(c)
# 2.Lösung:
for planet in planeten:
    if planet.startswith("M") or planet.startswith("N") :
        print(planet, end=", ")
