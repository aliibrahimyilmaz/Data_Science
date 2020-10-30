# Herkömmliche Schreibweise einer Funktion
def summe(x, y):
    return x+y
print("Herkömmlich: ", summe(3, 3))

summe2 = summe
print(summe2)

z = 3  # freien Variable, außerhalb der Funktion übergeben werden können, aber verboten
summe2 = lambda x, y: x + y + z
print(summe2)
print("Lambda: ", summe2(2, 3))

