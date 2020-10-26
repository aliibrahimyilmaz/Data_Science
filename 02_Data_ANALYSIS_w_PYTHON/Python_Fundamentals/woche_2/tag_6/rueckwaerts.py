# 4. Rückwärts
# Schreibe eine Funktion reverse_name(), die einen String entgegennimmt,
# diesen zu Kleinbuchstaben transformiert, den ersten und letzten Index abschneidet
# und das Ergebnis umgedreht zurückgibt:
# Beispiel:
# reversed = reverse_name("Petersburg")
# // rubsrete

# Erweitere den Prozess um einen Userinput in einem while-loop (mit Abbruchbedingung "quit" o.ä.)

def reverse_name(your_str):
    your_str = your_str.lower()
    your_str = your_str[1:-1]
    return your_str[-1::-1]

while True:
    user_input = input("Bitte geben Sie ein Wort ein oder zum Abbruch 'quit': ")
    if user_input == "quit":
        print("Auf Wiedersehen")
        break
    else:
        reversed = reverse_name(user_input)
        print(reversed)


