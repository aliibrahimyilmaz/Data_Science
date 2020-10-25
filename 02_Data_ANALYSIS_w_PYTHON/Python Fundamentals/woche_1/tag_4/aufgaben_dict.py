from pprint import pprint
# Übungsaufgaben zu Strings

# 1. Gegeben ist ein Dictionary. Lese seine Keys und Values aus
a = {
    "name":  "Zerkov",
    "power": 100,
    "status": True,
}
print('name: ', a.get('name'))
print('power: ', a.get('power'))
print('status: ', a.get('status'))

# 2. Gegeben ist eine Liste mit Dictionaries.
# Iteriere über diese Liste und speichere in einer Liste
# (berlin_addresses), die in Berlin leben (city == "Berlin").
addresses = [
    {"name": "tom sawyer", "zip": 10987, "city": 'Berlin'},
    {"name": "captain crunch", "zip": 10928, "city": 'Berlin'},
    {"name": "Sponge Bob", "zip": 24242, "city": 'Ozean'},
    {"name": "Maus vom Mars", "zip": 9999, "city": 'Mars'},
]
berlin_addresses = []
for address in addresses:
    if address.get('city') == 'Berlin':
        berlin_addresses.append(address)
pprint(berlin_addresses, width=1)

# 3. Erweitere das Dictionary a um einen weiteren Eintrag (Paris:44).
# Nutze dazu die update - Methode
a = {
    "Berlin": 22,
    "London": 33,
}
a.update({'Paris': 44})
pprint(a, width=1)

# 4. Zähle die Vorkommen von "a" in output.
# Nutze dazu NICHT die count() Methode, sondern ein Dictionary.

output = "afipaijaösdijpdsifasdfaafdpaiejaösdfjaöf"

counter = {}
for element in output:
    if element in counter:
        counter[element] += 1
    else:
        counter[element] = 1
#pprint(counter, width=1)
print('a: ', counter.get("a"))

