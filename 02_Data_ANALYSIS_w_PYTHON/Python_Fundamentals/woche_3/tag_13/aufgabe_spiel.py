class Wanderer:

    def __init__(self, name):
        self.name = name
        self.position = (0, 0)
        self.fahrt = [(0, 0)]

    def __repr__(self):
        return f"{self.name}"

    def go_left(self):
        if self.position[0] != 0:
            self.position = (self.position[0] - 1, self.position[1])
            self.fahrt.append(self.position)
        else:
            print("Man darf nicht negative Bereichen betreten!")

    def go_right(self):
        self.position = (self.position[0] + 1, self.position[1])
        self.fahrt.append(self.position)

    def go_up(self):
        self.position = (self.position[0], self.position[1] + 1)
        self.fahrt.append(self.position)

    def go_down(self):
        if self.position[1] != 0:
            self.position = (self.position[0], self.position[1] - 1)
            self.fahrt.append(self.position)
        else:
            print("Man darf nicht negative Bereichen betreten!")

    def show_fahrt(self):
        print(self.fahrt)

    def get_position(self):
        return self.position

alfa = Wanderer("Bernd")

while True:
    print(f"Du bist jetzt an/auf {alfa.get_position()}")
    user_input = input("Bitte bewegt dein Wanderer! ODER zum Abbruch 'q': ")
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
    else:
        print("Dieses Method befindet sich nicht!")

