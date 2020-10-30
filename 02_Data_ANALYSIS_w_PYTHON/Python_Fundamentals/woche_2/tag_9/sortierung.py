from pprint import pprint
# 1. Sortiere nach Einwohner
lst = [
    (19542209, "New York") ,
    (4887871, "Alabama"),
    (1420491, "Hawaii"),
    (626299, "Vermont"),
    (1805832, "West Virginia"),
    (39865590, "California")
]
lst.sort()
print("1. Sortierung nach Einwohner : ", lst)

# 2. Sortiere nach Bundesstaaten
states = [
    (19542209, "New York"),
    (4887871, "Alabama"),
    (1420491, "Hawaii"),
    (626299, "Vermont"),
    (1805832, "West Virginia"),
    (39865590, "California")
]
states.sort(key=lambda e:e[1])
print("2. Sortierung nach Bundesstaaten : ", states)

# 3. Sortiere absteigend
lst = [500, 1000, 400, 40000, 999, 2, 0.5, 17]

lst.sort(reverse=True)
print("3. Sortierung absteigend: ", lst)

# 4. Sortiere nach Vornamen
people = [
    {'first':'Barack', 'last':'Obama', 'email':'president@whitehouse.gov'},
    {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.kremlin.ru'},
    {'first':'Angela', 'last':'Merkel', 'email':'angela@merkel.de'},
 ]
people.sort(key=lambda e: e["first"])
print("4. Sortierung nach Vornamen: ", people)

# 5. Sortiere nach Punkten (aufsteigend)
player = {
    "peter": 100,
    "klaus": 34,
    "wizz": 222,
    "angela": 23,
    "sabine": 400
}

sorted_player = dict(sorted(player.items(), key=lambda e: e[1]))
print("5. Sortierung nach Punkten (aufsteigend): ", sorted_player)

# 6. Sortiere nach name
user = {
    1: {'name': 'Ali', 'age': 13, 'city': 'New York'},
    2: {'name': 'Ali', 'age': 33, 'city': 'Paris'},
    3: {'name': 'Ali', 'age': 19, 'city': 'Bogota'},
    4: {'name': 'Ali', 'age': 43, 'city': 'Kairo'},
    5: {'name': 'Ali', 'age': 8, 'city': 'Dortmund'},
    6: {'name': 'Alex', 'age': 2, 'city': 'Berlin'},
    7: {'name': 'Alex', 'age': 12, 'city': 'Hamburg'},
}

sorted_user = dict(sorted(user.items(), key=lambda e: e[1]['name']))
print("6. Sortierung nach name: ", sorted_user)
#pprint(sorted_user, width=1, sort_dicts=False)

