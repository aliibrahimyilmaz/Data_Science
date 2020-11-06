import random
import collections

class Spieler:

    def __init__(self, name: str, marker: tuple = None) -> None:
        self.name = name
        self.marker = marker
        self.matris = []

    def __repr__(self):
        return f"{self.name}"

    def set_marker(self, user_marker: tuple):
        self.marker = user_marker
        self.matris.append(self.marker)

    def get_marker(self):
        return self.marker

    def get_brett(self):
        return self.matris

    def get_name(self):
        return self.name


gamer = Spieler("Ali")
gegner = Spieler("Computer")
spielfeld = []

def fn_status(spieler_list):
    x_value_list = list(map(lambda x: x[0], spieler_list))
    y_value_list = list(map(lambda x: x[1], spieler_list))
    counter_x = collections.Counter(x_value_list)  # eine dict
    counter_y = collections.Counter(y_value_list)
    print(counter_x)
    print(counter_y)
    diagonal_down = 0
    diagonal_up = 0
    for i in spieler_list:
        if i in [(0, 0), (1, 1), (2, 2)]:
            diagonal_down += 1
        if i in [(0, 2), (1, 1), (2, 0)]:
            diagonal_up += 1
    if counter_x.most_common(1)[0][1] == 3 or counter_y.most_common(1)[0][1] == 3\
       or diagonal_down == 3 or diagonal_up == 3:
        print("Game Over!")
        return True
    else:
        return False

while True:
    print("spielfeld: ", spielfeld)
    print("gamer: ", gamer.get_brett())
    print("gegner: ", gegner.get_brett())

    user_input = input("Bitte gebe ein koordinat (x, y) bis 2 für deinen Marker X ODER zum Abbruch 'q': ")
    input_x, input_y = user_input.split()
    user_input = (int(input_x), int(input_y))  # umwandelt User-Eingabe als Tuple

    if user_input not in spielfeld:
        gamer.set_marker(user_input)
        spielfeld.append(gamer.get_marker())
        print(f"{gamer.get_name()} hat {gamer.get_marker()} markiert")
        if fn_status(gamer.get_brett()):
            print(f"{gamer.get_name()} hat gewonnen!")
            break
        while True:  # für gegner
            if len(spielfeld) < 9:
                rand_tuple = (random.randint(0, 2), random.randint(0, 2))
                if rand_tuple not in spielfeld:
                    gegner.set_marker(rand_tuple)
                    spielfeld.append(gegner.get_marker())
                    print(f"{gegner.get_name()} hat {gegner.get_marker()} markiert")
                    if fn_status(gegner.get_brett()):
                        print(f"{gegner.get_name()} hat gewonnen!")
                        break
                    break
            else:
                print(f"Der Spiel ist Einstand")
                break
    else:
        print("Der Platz ist schon besetzt! Finde einen leeren Platz!")

    if len(spielfeld) == 9:
        break

"""    if fn_status(gamer.get_brett()):
        print(f"{gamer.get_name()} hat gewonnen!")
        break"""

"""    if fn_status(gegner.get_brett()):
        print(f"{gegner.get_name()} hat gewonnen!")
        break"""


