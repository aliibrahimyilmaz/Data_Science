import random
import collections

class Spieler:

    def __init__(self, name: str, marker: tuple = None, counter: int = 0) -> None:
        self.name = name
        self.marker = marker
        self.matris = []
        self.counter = counter

    def __repr__(self):
        return f"{self.name}"

    def set_marker(self, user_marker: tuple):
        self.marker = user_marker
        self.matris.append(self.marker)

    def get_marker(self):
        return self.marker

    def set_counter(self):
        self.counter += 1

    def get_counter(self):
        return self.counter

    def get_brett(self):
        return self.matris

    def get_name(self):
        return self.name


def fn_status(spieler_list):
    x_value_list = list(map(lambda x: x[0], spieler_list))
    y_value_list = list(map(lambda x: x[1], spieler_list))
    counter_x = collections.Counter(x_value_list)  # eine dict
    counter_y = collections.Counter(y_value_list)
    # print(counter_x)
    # print(counter_y)
    diagonal_down = 0
    diagonal_up = 0
    for i in spieler_list:
        if i in [(0, 0), (1, 1), (2, 2)]:
            diagonal_down += 1
        if i in [(0, 2), (1, 1), (2, 0)]:
            diagonal_up += 1
    if counter_x.most_common(1)[0][1] == 3 or counter_y.most_common(1)[0][1] == 3\
       or diagonal_down == 3 or diagonal_up == 3:
        # print("Game Over!")
        return True
    else:
        return False

def show_brett(feld_list):
    for x in range(3):  # für Zeilen
        for y in range(3):  # für Spalten
            if (x, y) in feld_list:
                indx = feld_list.index((x, y))
                if indx % 2 == 0:
                    print("X", end="")
                else:
                    print("O", end="")
            else:
                print(" ", end="")
            if y < 2:
                print("|", end="")
        print()

dict_spiegel = {
    (0, 0): (2, 2),
    (2, 2): (0, 0),
    (2, 0): (0, 2),
    (0, 2): (2, 0),
    (0, 1): (2, 1),
    (2, 1): (0, 1),
    (1, 0): (1, 2),
    (1, 2): (1, 0)
}
gamer = Spieler("Ali")
gegner = Spieler("Computer")
spielfeld = []

while True:
    # print("spielfeld: ", spielfeld)
    # print("gamer: ", gamer.get_brett())
    print("gegner: ", gegner.get_brett())
    user_input = input("Bitte gebe ein koordinat (x, y) bis 2 für deinen Marker X ODER zum Abbruch 'q': ")
    if user_input == "q":
        print("Auf Wiedersehen!")
        break
    else:
        input_x, input_y = user_input.split()
        user_input = (int(input_x), int(input_y))  # umwandelt User-Eingabe als Tuple

        if user_input not in spielfeld:
            gamer.set_marker(user_input)
            spielfeld.append(gamer.get_marker())
            print(f"{gamer.get_name()} hat ein X in {gamer.get_marker()} gesetzt")
            show_brett(spielfeld)
            if fn_status(gamer.get_brett()):
                print(f"{gamer.get_name()} hat gewonnen!")
                print("Game Over!")
                break
            while True:  # für gegner
                if len(spielfeld) < 9:
                    if gegner.get_counter() == 0:  # erste Zug
                        if (1, 1) not in spielfeld:
                            rand_tuple = (1, 1)
                            gegner.set_marker(rand_tuple)
                            spielfeld.append(gegner.get_marker())
                            print(f"{gegner.get_name()} hat ein O in {gegner.get_marker()} gesetzt")
                            gegner.set_counter()
                            show_brett(spielfeld)
                            break
                        else:
                            # rand_tuple = random.choice([(0, 0), (0, 2), (2, 0), (2, 2)])
                            rand_tuple = (random.randint(0, 2), random.randint(0, 2))
                            gegner.set_marker(rand_tuple)
                            spielfeld.append(gegner.get_marker())
                            print(f"{gegner.get_name()} hat ein O in {gegner.get_marker()} gesetzt")
                            gegner.set_counter()
                            show_brett(spielfeld)
                            break
                    else:
                        if dict_spiegel.get(gamer.get_marker()) not in spielfeld:
                            rand_tuple = dict_spiegel.get(gamer.get_marker())
                        else:
                            rand_tuple = (random.randint(0, 2), random.randint(0, 2))
                        if rand_tuple not in spielfeld:
                            gegner.set_marker(rand_tuple)
                            spielfeld.append(gegner.get_marker())
                            print(f"{gegner.get_name()} hat ein O in {gegner.get_marker()} gesetzt")
                            show_brett(spielfeld)
                            if fn_status(gegner.get_brett()):
                                print(f"{gegner.get_name()} hat gewonnen!")
                                print("Game Over!")
                                break
                            break
                else:
                    print(f"Einstand! Keine Sieger!")
                    break
        else:
            print("Der Platz ist schon besetzt! Finde einen leeren Platz!")

        if len(spielfeld) == 9 or fn_status(gegner.get_brett()):
            break

