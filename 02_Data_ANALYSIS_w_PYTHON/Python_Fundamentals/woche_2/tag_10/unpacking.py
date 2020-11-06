# a, b, c, d = [1, 2, 3]  # für d Fehler!
# d, e = (4, 5, 6)  # für 6 Fehler!

a, *b = [1, 2, 3, 4, 5]  # Unpacking
print(a)  # a: 1
print(b)  # b: [2, 3, 4, 5]

*d, e = (4, 5, 6)  # *wildcard
print(d)  # d: [4, 5]
print(e)  # e: 6

# String in Liste entpacken
*x, y = "teststring"
print(x, y)  # Ergebnis ist sehr interessant

# Liste entpacken bei funktions aufruf
def test(a, b):
    print(a, b)

liste_a = [1, 2]
test(*liste_a)



