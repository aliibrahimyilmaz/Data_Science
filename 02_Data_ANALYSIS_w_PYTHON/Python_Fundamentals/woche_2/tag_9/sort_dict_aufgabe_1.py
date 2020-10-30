# Schreibe eine Funktion, die das folgende Dict nach absteigender Größe (Einwohner) sortiert.
# Nutze dazu eine Lambda funktion und die Funktion sorted()
cities = {
'Köln': 1200000,
'Moskau': 10000000,
'Berlin': 3400000,
'München': 1600000,
'Paris': 3800000,
}

cities_sorted = dict(sorted(cities.items(), key=lambda e: e[1], reverse=True))
print("Cities nach absteigender Größe (Einwohner): ", cities_sorted)

cities_sorted = sorted(cities, key=cities.get, reverse=True)
print("Cities nach absteigender Größe (Einwohner): ", cities_sorted)
