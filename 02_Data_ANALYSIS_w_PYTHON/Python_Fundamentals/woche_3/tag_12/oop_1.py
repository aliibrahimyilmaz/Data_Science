class House:
    pass

small_house = House()  # small_house is ein Objekt, wie a = 1
big_house = House()
print("Datentype Objekt small_house: ", type(small_house))
print("Datentype Objekt small_house: ", type(big_house))
print("Type vpn 1: ", type(1))  # Alle Datentypen sind objekten von classen

print(House)
print(type(House))

print("instance of: ", isinstance(small_house, House))  # wir prüfen ob small_house eine Objekte der classe House
print("instance of: ", isinstance(1, int))
print("instance of: ", isinstance("1", int))



