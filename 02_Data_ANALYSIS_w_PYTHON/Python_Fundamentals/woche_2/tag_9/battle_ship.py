'''
Schiffe versenken
In der Liste ships finden sich zwei Schiffe, die durch Listen mit Tupel mit den x- und y- Koordinaten
repräsentiert werden. Schiff 1 ist ein horizontalliegendes, Schiff 2 ein vertikalliegendes
Schiff.
'''
import pandas as pd
from pprint import pprint
ships = [
    [(2, 3), (3, 3), (4, 3)],
    [(2, 5), (2, 6), (2, 7)]
]

draft_list = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
columns = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9]
df_operation_area = pd.DataFrame(data=draft_list, columns=columns, index=index)  # von PANDAS MODULE


def fn_ship_allocator(area):
    for ship in ships:
        for koordinate in ship:
            x = koordinate[0]
            y = koordinate[1]
            area.loc[x, y] = "S"
    return area


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
            print(ships)
            break
    if treffer == False:
        print("Wasser!")
        print(ships)
    return treffer

def fn_position_updater(user_input, area, treffer = False):
    x = user_input[0]
    y = user_input[1]
    if treffer:
        area.loc[x, y] = "X"  # "Treffer"
    else:
        area.loc[x, y] = "W"  # "Wasser"
    return area

user_schuss_list = []
while True:
    df_operation_area = fn_ship_allocator(df_operation_area)
    print(df_operation_area)
    user_string = fn_user_input()
    if user_string == "q":
        break
    else:
        user_input = fn_tuple_generator(user_string)  # (String)
        if user_input not in user_schuss_list:
            user_schuss_list.append(user_input)
            treffer = fn_beobachter(user_input)  # (Tuple)
            df_operation_area = fn_position_updater(user_input, df_operation_area, treffer)  # (Tuple, Bool)
            if ships == []:
                print("Herzlichen Glückwünsch! Du hast gewonnen!")
                break
        else:
            print("Du hast schon gleiche Koordinate geschossen!")
