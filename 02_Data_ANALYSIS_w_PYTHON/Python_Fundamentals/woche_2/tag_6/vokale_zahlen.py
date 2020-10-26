# 1. Vokale zählen
# Schreibe eine Funktion count_vocals() die einen String als Parameter erwartet,
# und alle Vokale  in diesem String zählt.
# Der Rückgabewert der Funktion ist die Anzahl der Vokale (int).
# Beispiel:
# number_of_vocals = count_vocals("teleport").
# // 3
def count_vocals(my_str):
    vocals = ["a", "e", "i", "o", "u"]
    my_list = list(my_str)
    counter = 0
    for element in my_list:
        if element.lower() in vocals:
            counter += 1
    #print(counter)
    return counter

number_of_vocals = count_vocals("teleport")
print(number_of_vocals)


