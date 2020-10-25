from pprint import pprint  # prettyprint

person = {
    "name": {
        "first_name": "Ali",
        "last_name": "Yilmaz",
    },
    "age": 23,
    "adress": {
        'street': 'Musterstrasse3',
        'zip': '92823',
        'place': 'Kassel',
    }
}
# Aufgabe: auf die Straße zugreifen
# pprint(person, width=1)

print(person["adress"]["street"])
print(person['name']['first_name'], person['name']['last_name'])

# updaten values
person['name']['first_name'] = 'Ibrahim'

print(person.get('adress', {}))  # das Ergebnis ist auch Dict. Wir können tiefer gehen
print(person.get('adress', {}).get("streets", {}))

# Aufgabe: Vor- und Nachname ausgeben lassen

print(
    person.get('name', {}).get('first_name', None),
    person.get('name', {}).get('last_name', None),
)

# update() methoden
person.get('adress').update(
    {
        'street': 'Kurze Str 3a'
    }
)
print(person)
