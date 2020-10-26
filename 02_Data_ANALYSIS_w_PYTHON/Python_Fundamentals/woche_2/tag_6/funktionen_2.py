# from lib.functions import permutate_string

day = "Dienstag"  # Global scope
number = 2  # Global scope
liste = [1, 2, 3]

# Variablen aus dem äußeren Scope werden nur verwendet, aber nicht wieder zugewiesen
# Globale Variablen können nicht in der Funktion verändert werden, aber Liste ja.
def print_day(d):
    print("day aus dem äußeren Scope: ", number)  # man kann nur das hier verwenden.
    # number = 3  # nicht funktuniert, Fehler
    x = 1
    day = d
    print("das ist das Funktions day: ", day)
    liste.append(4)  # keine Fehler hier
    liste[0] = 3  # es geht für Listen

print_day("Montag")
print("das ist day: ", day)
# print(x)  # Fehler
print(liste)

# summe(3, 4)

# aufgabe
# permutate_string("elisa")  # argument

from lib.functions import permutate_string
while True:
    user_input = input("Bitte geben Sie eine Vorname ein, zum Abbrechen bitte geben Sie q ein: ")
    if user_input == "q":
        print("Auf Wiedersehen!")
        break
    else:
        permutate_string(user_input)

