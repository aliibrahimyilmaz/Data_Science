# Aufgabe
# Definiere die Funktion is_float(), die prüft,
# ob eine String in ein Float gewandelt werden kann
# define function is_float(), which determines,
# if a given string can be converted to float
# Rückgabewert bool, Parameter str.

def is_float(value: str = "my_str") -> bool:
    try:
        float(value)
        return True
    except ValueError:
        print("Your string can not be converted to float!")
        return False

my_str = "0,3"
print(is_float(value=my_str))
