# Aufgabe: User muss solange einen Wert über die Eingabeaufforderung eingeben, bis dieser
# nach Int geparst werden kann.
# im Fehlerfall soll wieder die Eingabeaufforderung kommen. Nutze while, input, try/except
# User must enter any input value, till this value can be properly converted to an Integer.
# in case of an exception, the input field should appear again.

def int_parse(value: str) -> bool:
    try:
        int(value)
        print(int(value))
        print("Es hat gut geklappt!")
        return False
    except:
        print("Das geht nicht! ")
        print("False")
        return True


value = " "
while int_parse(value):
    value = input("Bitte geben Sie eine Zahl ein: ")
