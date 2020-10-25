import random
# https://www.w3schools.com/python/module_random.asp
# https://realpython.com/python-conditional-statements/
geburtsort = "Hamburg"
if geburtsort == "Hamburg":
    print("user ist aus hamburg")
else:
    print("User ist nicht aus Hamburg")

# Aufgabe: User gibt Zahl ein. Das Programm soll prüfen, ob die Zahl größer ist als 3.
# Ansonsten soll eine Fehlermeldung ausgegeben werden
"""
num = int(input("Bitte gebe ein ganze Zahl ein: "))
if num > 3:
    print("Ja. {} is großer als 3".format(num))
    print(f"Ja. {num} is großer als 3")
else:
    print("Nein. {} is nicht großer als 3".format(num))
    print(f"Nein. {num} is nicht großer als 3")
"""

zufallszahl = random.randint(1, 6)
print("zufallszahl", zufallszahl)
if zufallszahl > 4:
    print(f"{zufallszahl} größer als 4")
elif zufallszahl >= 2:
    print(f"{zufallszahl} größergleich 2 und kleinergleich 4")
else:
    print(f"{zufallszahl} kleiner als 2")

"""
# This is a sassy code. It doesn't like your age, no matter what you type in.
print("How old are you?")
age = input("Age: ")
if age > 30:
print("Wow. You are old.")
elif 30>=int(age) and int(age)>=12:
print("Are you still in puberty?")
elif 0<int(age)<12:
print("You`re a little kid")
elif int(age) == 12 or int(age) == 30:
print("Your're at the borderline age between the two worst ages.")
else:
print("That doesn`t make sense")
"""

