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

while True:
    user_input = input("Bitte geben Sie die x und y Koordinate ein ODER zum Abbruch 'q': ")
    if user_input == "q":
        print("Du hast das Spiel Verlassen, Auf Wiedersehen")
        break
    else:
        input_x, input_y = user_input.split()
        user_input = (int(input_x), int(input_y))
        print(user_input)
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
        if treffer == False:
            print("Wasser!")
        if ships == []:
            print("Herzlichen Glückwünsch! Du hast gewonnen!")
            break
        print(ships)
