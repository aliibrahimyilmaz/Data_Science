class Person:
    """beschreibt eine Person"""

    _counter = 0

    def __init__(self, first_name: str, last_name: str, age: int):
        #print(id(self))
        self.first_name = first_name
        # first_name = first_name + "2"  # lokale Variable in init
        self.last_name = last_name
        self.age = age
        self.city = None
        # print("counter: ", self._counter)
        Person._counter += 1  # Klasse Ebene Variablen, wie viele Objekte bis jetzt erstellt.

    def __repr__(self):
        """
        https://www.python-course.eu/python3_magic_methods.php
        Magic Methods, zb. __repr__, Magic Attributes, __doc__
        String Representation des Objektes"""
        return f"{self.first_name} {self.last_name} {self.age}"

    def set_city(self, city: str):
        self.city = city  # another attribute

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_name(self):
        return f"{self.first_name} {self.last_name}"

    def how_many_persons():
        return Person._counter


maria = Person("Maria", "Petrochenkova", 20)
print("maria objekt:", maria)  # __repr__ ergibt das
markus = Person("Markus", "Bacher", 20)


# wird geliefert aus CSV-Datei o.ä:
personen_liste = [
    {"fn": "Markus", "ln": "Bacher", "age": 22},
    {"fn": "Tom", "ln": "Bach", "age": 18},
    {"fn": "Micky", "ln": "Cher", "age": 25}
]

person_objects = []

for person in personen_liste:
    first_name = person.get("fn")
    last_name = person.get("ln")
    age = person.get("age")
    p = Person(first_name, last_name, age)
    person_objects.append(p)  # jedes element in Liste ist ein Object

print(person_objects)  # das ist ein represantation
print(person_objects[0].get_name())


print("Anzahl erstellter Personen: ", Person.how_many_persons())
