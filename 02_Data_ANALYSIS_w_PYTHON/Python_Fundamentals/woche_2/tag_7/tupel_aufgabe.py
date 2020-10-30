# gewünschtes Ergebnis für Key Frodo
# {'salutation': 'Mr.', 'first_name': 'Frodo', 'last_name': 'Baggins', 'street': 'Bag End 1', 'city': 'Hobbiton'}
# {'salutation': 'Mr.', 'first_name': 'Samwise', 'last_name': 'Gamgee', 'street': 'Bagshot Row 2', 'city': 'Hobbiton'}
# addresses['Frodo']['street'] Bag End 1
# addresses['Samwise']['street'] Bagshot Row 2
# addresses['Frodo']['first_name'] Frodo
from pprint import pprint
address_list = [
    ("salutation", "first_name", "last_name", "street", "city",),
    ("Mr.", "Frodo", "Baggins", "Bag End 1", "Hobbiton",),
    ("Mr.", "Samwise", "Gamgee", "Bagshot Row 2", "Hobbiton",),
    ("Mr.", "Gandalf", "the Grey", "Wizard street 42", "somewhere", ),
]


def get_dict(address_list):
    head = address_list.pop(0)
    address_dict = {}
    for i, a in enumerate(address_list):
        # key wird der key für das Adress-Dict
        key = a[1]
        address_dict[key] = dict(zip(head, address_list[i]))
    return address_dict


address_dict = get_dict(address_list)
pprint(address_dict)
print(address_dict["Frodo"].get('street', 'Prüfe deine Eingabe'))





