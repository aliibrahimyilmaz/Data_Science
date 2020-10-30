# unsortierte Liste
liste = [3, 5, 1, 9, 1]
print("unsortierte Liste: ", liste)

# sortierte Liste
liste = sorted(liste)
print("sortierte Liste: ", liste)

# sortierte Liste
liste = sorted(liste, reverse=True)
print("reversed sortierte Liste: ", liste)

# Buchstabenliste (über die Codepoints)
chars = ['a', 'f', 'c', 'd', 'e']
chars = sorted(chars)
print('chars: ', chars)

print("Unicode Dezimal Codepoint für das kleine a: ", ord('a'))

# Großbuchstaben kommen vor Kleinbuchstaben
chars = ['a', 'f', 'b', 'B', 'A', 'd', 'e']
chars = sorted(chars)
print(chars)

print("Unicode Dezimal Codepoint für das kleine a: ", ord('A'))
print("Unicode Dezimal Codepoint für das kleine a: ", ord('B'))

# Sortierung anhand von Kleinbuchstaben
chars = ['a', 'f', 'b', 'B', 'A', 'd', 'e']
chars = sorted(chars, key=lambda char: char.lower())
print(chars)

# Sortierung anhand von Großbuchstaben
chars = ['a', 'f', 'b', 'B', 'A', 'd', 'e']
chars = sorted(chars, key=lambda char: char.upper())
print(chars)

# Dictionary Sortierung nach Keys, Rückgabe ist eine Liste
snacks = {'Milka': 3.30, 'Kekse': 5.20, 'Snickers': 1.50}
snacks_sorted = sorted(snacks)
print("snacks_keys: ", snacks_sorted)

# nach Value Sortiert, Rückgabe ist eine Liste
snacks_sorted = sorted(snacks, key=lambda e: snacks[e], reverse=True)
print("snacks nach Value sortiert, absteigend: ", snacks_sorted)

snacks_sorted = sorted(snacks, key=snacks.get, reverse=True)  # snacks.get nimmt the key und ergibt the Value
print("snacks.get nach Value sortiert, absteigend: ", snacks_sorted)

snacks_sorted = sorted(snacks.items(), key=lambda e: e[1])  # element von snacks.items is Tuple
print("Snacks nach Value sortiert mit Tuple: ", snacks_sorted)

snacks_sorted = dict(sorted(snacks.items(), key=lambda e: e[1]))  # element von snacks.items is Tuple
print("Snacks nach Value sortiert mit Dict: ", snacks_sorted)

