from pprint import pprint
# dict() für 2D Listen
letter_list = [
    ['A', 'Anton'],
    ['B', 'Berta'],
    ['C', 'Ceasar'],
]

a = dict(letter_list)
print(a)

# liste
a = [1, 2, 3]
print(type(a))

# tuple
a = 1, 2, 3  # ODER (1, 2, 3) mit oder ohne Klammen
print(type(a))

# Dict erstellen via zip()
countries = ["Deutschland", "Türkei", "USA", "Russland", "Spanien"]
food = ["Currywurst", "Pilav", "Hamburger", "Pelmeni", "Empanada"]

zip_objekt = zip(countries, food)
print(zip_objekt)
world_food = dict(zip_objekt)
print(world_food)

# so ein dict wollen wir aus zwei listen erstellen
zip_objekt_2 = zip(countries[0:2], food[0:2])
food_2 = dict(zip_objekt_2)
pprint(food_2, width=1)