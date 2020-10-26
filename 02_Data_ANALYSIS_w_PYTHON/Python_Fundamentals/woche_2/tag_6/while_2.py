# Zahlenratespiel
# Zufallszahl errechnen(mit random.randint), zb.4
# maximale Rateversuche: 4
# whileloop
# pro Loop ein User Input. Ist user input nicht gleich der Zufallszahl
# leider falsch, bitte nochmal raten
# im Glück gehabt, du hast gewonnen!
# falls die Anzahl der Rateversuche >= der maximalen Rateversuche, Game over

import random
min_num = 1
max_num = 10
zahl = random.randint(min_num, max_num)
print(zahl)
versuch = 0
max_versuch = 4
win = False

while versuch < max_versuch:
    user_input = int(input("Bitte gebe eine Zahl ein: "))
    if user_input == zahl:
        print("Super, du hast die Zahl erraten")
        win = True
        break

    print("Leider wurde die Zahl nicht erraten")
    versuch += 1

if not win:
    print("Leider! Game Over!")
else:
    print("Glück gehabt. Du hast gewonnen!")

