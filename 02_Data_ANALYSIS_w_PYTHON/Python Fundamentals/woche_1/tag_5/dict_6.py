population = {
'Berlin': 3748148,
'Hamburg': 1822445,
'München': 1471508,
'Cologne': 1085664,
}
# über ein Dictionary iterieren
for element in population.items():
    print(element)

for key, value in population.items():
    print(key, value)

if population:
    pass  # für lücke oder geplannte coden
print("Hallo")

# keys() Methode, nicht so heufig
for key in population.keys():
    print('key aus population: ', key)

# values() Methode, nicht so heufig
for value in population.values():
    print('value aus population:', value)

# Aufgabe: Gebe jeweils den Vornamen aus
namen = {
"lists": [
{"name": "Peter"},
{"name": "Daniel"},
{"name": "Bernd"},
{"name": "Abdelrahman"},
]
}
for element in namen.get("lists"):
    print(element.get("name"))
# ODER
for x in namen["lists"]:
    print(x["name"])
