VERSION = 1  # Python kennt das Konzept von Konstanten nur als Konvention


def summe(a, b):
    '''addiert zwei Zahlen'''  # dokumentation ist wichtig!
    return a + b


print(summe.__doc__)  # dunder attribute (double under), magic


# Beispiel Seiteneffekt:

def fn(liste):
    liste += [2, 3, 4, 5]

a = [1, 2]
print(a)
# a = fn(a) # return None
fn(a)  # seiteneffekt
print(a)

# Unix Philosophie:
# Eine Funktion soll eine und genau eine Aufgabe haben.

# Prinzip DRY: Don't Repeat Yourself.