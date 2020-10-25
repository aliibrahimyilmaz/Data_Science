print("Ganzahl Division: ", 5 // 4)
# Aufgabe
# Berechne den Rauminhalt eines Würfels mit Seitenlänge a = 20
print("Rauminhalt eines Würfels: ", 20*20*20)
a = 20
volume = a ** 3
print("Rauminhalt: ", volume)

# Typ-Umwandlung von Float nach Int
a = 4
b = 3
c = a/b
print(int(c), c)

print(float(int(c)))

# Schreibe ein Programm, welches zwei Floats a und b addiert
# Wandle das Ergebnis in ein Integer
a = 4.2
b = 3.4 # benennen = name
c = a + b
print(c, int(c))
print(c)
c = int(c)
print(c)

# Runden, round()
c = 3/ 2.2
print(c)
y = round(c,2)  # Zweite parameter ist optionäl
print(y)
x = round(c)  # nur ganzahl geben
print(x)

