import random


class Wanderer:

    def __init__(self, name: str, position: tuple = (0, 0)) -> None:
        self.name = name
        self.position = position
        self.fahrt = [(0, 0)]

    def __repr__(self) -> str:
        return f"{self.name}"

    def go_left(self) -> None:
        if self.position[0] != 0:
            self.position = (self.position[0] - 1, self.position[1])
            self.fahrt.append(self.position)
        else:
            print("Man darf nicht negative Bereichen betreten!")

    def go_right(self) -> None:
        self.position = (self.position[0] + 1, self.position[1])
        self.fahrt.append(self.position)

    def go_up(self) -> None:
        self.position = (self.position[0], self.position[1] + 1)
        self.fahrt.append(self.position)

    def go_down(self) -> None:
        if self.position[1] != 0:
            self.position = (self.position[0], self.position[1] - 1)
            self.fahrt.append(self.position)
        else:
            print("Man darf nicht negative Bereichen betreten!")

    def show_fahrt(self) -> None:
        print(self.fahrt)

    def get_position(self) -> tuple:
        return self.position

    def get_name(self) -> str:
        return self.name


alfa = Wanderer("Bernd")
beta = Wanderer("Zauberer", (random.randint(1, 4), random.randint(1, 4)))

while True:
    print(f"{alfa.get_name()} ist jetzt an/auf {alfa.get_position()}")
    print(f"Zauberer ist jetzt an/auf {beta.get_position()}")
    user_input = input("Bitte bewege deinen Wanderer mit 'WASD'! ODER zum Abbruch 'q': ")
    if user_input == "a":
        alfa.go_left()
    elif user_input == "d":
        alfa.go_right()
    elif user_input == "s":
        alfa.go_down()
    elif user_input == "w":
        alfa.go_up()
    elif user_input == "show":
        alfa.show_fahrt()
    elif user_input == "q":
        print("Du hast das Spiel verlassen! Auf Wiedersehen!")
        break
    elif alfa.get_position() == beta.get_position():
        print("Bernd hat das Spiel verloren!")
        break
    else:
        print("Diese Methode existiert nicht!")

    random.choice([beta.go_up, beta.go_down, beta.go_left, beta.go_right])()

    if alfa.get_position() == beta.get_position():
        print("Bernd hat das Spiel verloren!")
        break
    elif abs(alfa.get_position()[0] - beta.get_position()[0]) + abs(alfa.get_position()[1] - beta.get_position()[1]) <= 4:
        print("Zauberer wirft einen Blitz auf Bernd!")
        x = random.choice([0, 1])  # %50 Chance
        if x == 1:
            print("getroffen!")
            print("Bernd hat das Spiel verloren!")
            break
        else:
            print("verfehlt!")

