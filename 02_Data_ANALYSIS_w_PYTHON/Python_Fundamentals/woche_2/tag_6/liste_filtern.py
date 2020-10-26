# 3. Liste filtern
# Schreibe eine Funktion filter_input(), die eine Liste A entgegennimmt und
# anhand einer weiteren Liste B mit erlaubten Werten prüft, ob diese Werte zulässig sind.
# Rückgabewert der Funktion ist eine Liste mit Werten, die mithilfe B geprüft worden sind.

# Beispiel
# input_filtered = filter_input([1, 3, 4, 5, 3], [3, 4])
# // [3, 4, 3]

# input_filtered = filter_input(["gold", "gelb", "gelb", "rot", "gelb"], ["gelb", "rot"])
# // ["gelb", "gelb", "gelb", "rot"]

def filter_input(list_a, list_b):
    filtered_list = []
    for wert in list_a:
        if wert in list_b:
            filtered_list.append(wert)
    return filtered_list

input_filtered = filter_input(["gold", "gelb", "gelb", "rot", "gelb"], ["gelb", "rot"])
print(input_filtered)