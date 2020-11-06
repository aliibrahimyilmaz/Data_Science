class Person:
    """beschreibt eine Person"""

    def __init__(self, first_name: str, last_name: str, phone_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.id = (self.first_name, self.last_name)

    def __repr__(self):
        """
        https://www.python-course.eu/python3_magic_methods.php
        Magic Methods, zb. __repr__, Magic Attributes, __doc__
        String Representation des Objektes"""
        return f"{self.first_name} {self.last_name} {self.phone_number}"

    def get_first_name(self):
        return self.first_name


class Telefonbuch:

    def __init__(self, name: str) -> None:
        self.name = name
        self.personen = {}  # {('Maria', 'Petrochenkova'): Maria Petrochenkova +49 742 2112412}

    def __repr__(self):
        return f"{self.name}"

    def add(self, person: Person):  # wir fügen eine Neue Person in unser App
        self.personen.update({person.id:person})

    def show_entry(self, first_name, last_name):
        return self.personen.get((first_name, last_name))

    def remove_entry(self, first_name, last_name):
        self.personen.pop((first_name, last_name), None)  # None, Dict löscht

    def show_entries(self, **kwargs):  # Filter
        # print("Personen: ", self.personen)
        if "filter_firstname" in kwargs:
            for element in self.personen.values():
                fn = element.get_first_name()
                if fn.startswith(kwargs.get("filter_firstname")):
                    print(fn)
                    #print(element)
        else:
            print(self.personen)

telefonbuch = Telefonbuch("Privates Telefonbuch")
p1 = Person("Maria", "Petrochenkova", "+49 742 2112412")
p2 = Person("Markus", "Bacher", "+49 142 234567")
p3 = Person("Markus", "Schöpf", "+49 742 2112412")
p4 = Person("Mona", "Elyamany", "+49 142 234567")

telefonbuch.add(p1)
telefonbuch.add(p2)
telefonbuch.add(p3)
telefonbuch.add(p4)
telefonbuch.show_entries(filter_firstname='M')
telefonbuch.show_entries()  # print self.personen



