# 1. Übungen zu Addition, Multiplikation, Subtraktion, Potenz, Modulo
import math
# 1.1 Addition
a, b = 2, 2.3
c = a + b
d = b + c
print("1.1 d: ", d)

# 1.2 Addition
a, b = 12.3, 3553
c = a + b
print("1.2 c: ", c)

# 1.3 Division
a, b = 12.3, 3553
c = a / b
d = c / a  # a/b/a
print("1.3 d: ", round(d, 8))

# 1.4 Division
a, b = 1, 0.1
c = a / b
d = 1 / c  # (b / a)
print("1.4 d: ", d)

# 1.5 Division
a, b = 1, 0.11
c = a / b
d = 1 / c  # (b / a)
print("1.5 d: ", round(d, 4))

# 1.6 Division
a, b = 1, 1
c = a / b
d = 1 / c  # (b / a)
print("1.6 d: ", d)

# 1.7 Subtraktion
a, b = 12.3, 12
c = a - b
d = b - a
print("1.7 c: ", round(c, 2))
print("1.7 d: ", round(d, 2))

# 1.8 Multiplikation
a, b = 12.3, -12
c = a * b
d = b * a
print("1.8 c: ", round(c, 2))
print("1.8 d: ", round(d, 2))

# 1.9 Multiplikation
a, b = 0.0, 0
c = a * b
d = b * a
print("1.9 c: ", c)
print("1.9 d: ", d)

# 1.10 Exponent
a, b = 2, 4
c = b ** a
d = a ** b
print("1.10 c: ", c)
print("1.10 d: ", d)

# 1.11 Exponent
a = 0
b = 2
c = a ** b
d = b ** a
print("1.11 c: ", c)
print("1.11 d: ", d)

# 1.12 Rechnen mit Rest (Modulo) (%)
a = 43
b = 3
rest = a % b
print("1.12 rest: ", rest)

# 2. Exponentiation
# Berechne das Ergebnis für d
a = 2
b = 0
d = a ** b
# Erhöhe b schrittweise um 1 bis 4.
print("2. d: ", d, a ** 1, a ** 2, a ** 3, a ** 4)

# 3. Berechne den Flächeninhalt f der Rechtecke:
a, b = 2, 4
f = a * b
print("3. f_inhalt: ", f)
a, b = 0, 20
f = a * b
print("3. f_inhalt: ", f)

# 4. Berechne das Volumen v folgender rechteckiger Körper:
a, b, c = 2, 4, 3
v = a * b * c
print("4. volume: ", v)
a, b, c = 1, 1.1, 4
v = a * b * c
print("4. volume: ", v)

# 5. Fahrenheit nach Celcius umrechnen (Internet recherchieren):
celcius = 20
fahrenheit = celcius * 1.8 + 32
print("5. Fahrenheit: ", fahrenheit)

# 6. Berechne die Distanz zweier Punkte p1(x1,y1) und p2(x2, y2)
x1 = 10
y1 = 30
x2 = 30
y2 = 28
# Nutze dazu das math-Modul und die sqrt-Methode().

distanz = math.sqrt((x2-x1)**2 - (y2-y1)**2)
print("6. distanz: ", round(distanz, 4))
