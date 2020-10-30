# Aufgabe: Snacks sortieren nach Preis
snacks = {
    1: {'name': 'Erdnüsse', 'price': 200, 'amount': 50},
    2: {'name': 'Milka', 'price': 400, 'amount': 20},
    3: {'name': 'Snickers', 'price': 100, 'amount': 10},
}

snacks_sorted = sorted(snacks.items(), key=lambda e: e[1]["price"], reverse=True)
print("snacks nach absteigender Price: ", snacks_sorted)

snacks_sorted = dict(sorted(snacks.items(), key=lambda e: e[1]["price"], reverse=True))
print("snacks nach absteigender Price: ", snacks_sorted)