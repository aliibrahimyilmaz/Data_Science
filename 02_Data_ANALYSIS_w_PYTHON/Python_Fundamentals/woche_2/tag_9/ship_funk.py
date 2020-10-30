'''
Schiffe versenken
In der Liste ships finden sich zwei Schiffe, die durch Listen mit Tupel mit den x- und y- Koordinaten
repräsentiert werden. Schiff 1 ist ein horizontalliegendes, Schiff 2 ein vertikalliegendes
Schiff.
'''
ships = [
    [(2, 3), (3, 3), (4, 3)],
    [(2, 5), (2, 6), (2, 7)]
]


def fn_user_input():
    """Annahme des User-Eingabes als String"""
    user_input = input("Bitte geben Sie die x und y Koordinate ein ODER zum Abbruch 'q': ")
    if user_input == "q":
        print("Du hast das Spiel Verlassen, Auf Wiedersehen")
    return user_input


def fn_tuple_generator(user_string):
    """umwandelt User-Eingabe als Tuple"""
    input_x, input_y = user_string.split()
    user_input = (int(input_x), int(input_y))
    # print(user_input)
    return user_input


def fn_beobachter(user_input):
    """beobachtet der Schuss und gibt eine Bewertung zurück"""
    treffer = False
    for ship in ships:
        if user_input in ship:
            treffer = True
            inx = ship.index(user_input)
            del ship[inx]
            if ship == []:
                print("Treffer, versenkt!")
                inx_ship = ships.index(ship)
                del ships[inx_ship]
            else:
                print("Treffer!")
            break
    if treffer == False:
        print("Wasser!")
    if ships == []:
        print("Herzlichen Glückwünsch! Du hast gewonnen!")
    print(ships)


while True:
    user_string = fn_user_input()
    if user_string == "q":
        break
    else:
        user_input = fn_tuple_generator(user_string)
        fn_beobachter(user_input)


