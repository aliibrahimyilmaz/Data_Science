names = [
    ["Andi", "Kolb", 1],
    ["Peter", "Meier", 2],
    ["Andreas", "Walter", 3],
    ["Sandra", "Schneider", 4]
]

def sort_nachname(element):
    """Parameter element Beispiel: ['Andi', 'Kolb']"""
    return element[2]

names.sort()
print("Sortierung nach Vornamen (default): ", names)

# sort-Methode()
names.sort(key=sort_nachname)
print("Sortierung nach Nachname: ", names)

# Gleiches Ergebnis mit sorted()
names = sorted(names, key=sort_nachname)
print("Sortierung nach Nachname: ", names)
