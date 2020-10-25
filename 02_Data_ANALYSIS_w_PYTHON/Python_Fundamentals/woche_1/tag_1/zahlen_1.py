# Ganzzahl = integer

x = 1
y = 2
result = x + y

print(result)

x = 2
print(id(x))
x = 3
print(id(x))
x1 = 2
print(id(x1))

# Aufgabe: Lege drei Variablen a, b, c
# mit Ganzzahlen an und speichere das Ergebnis
# in einer Variable d
a = 1
b = 2
c = 3
d = a + b + c
print("Ergebnis der Addition: ", d)
print(type(d))

r1, r2 = 9, 3
r = r1 / r2  # produziert immer float
print("Ergebnis der Division: ", r)
print(type(r))

# Fließkommazahlen = float
f1 = 1.0
g = 1
print('Datentyp der Addition float + int: ', type(f1 + g))