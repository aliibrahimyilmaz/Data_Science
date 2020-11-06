class Person:
    """beschreibt eine Person"""

    _counter = 0


    def __init__(self, first_name: str, last_name: str, age: int):
        print(id(self))
        self.first_name = first_name
        first_name = first_name + "2"  # lokale Variable in init
        self.last_name = last_name
        self.age = age
        # print("counter: ", self._counter)
        Person._counter += 1  # Klasse Ebene Variablen, wie viele Objekte bis jetzt erstellt.

    def set_name(self, first_name):
        self.first_name = first_name

    def get_name(self):
        return f"{self.first_name} {self.last_name}"

    def how_many_persons():
        return Person._counter


maria = Person("Maria", "Petrochenkova", 20)
markus = Person("Markus", "Bacher", 20)
print(markus.get_name())
# markus.first_name = "Mark" # verletzt die Konvension
markus.set_name('Mark')
print(markus.get_name())

print(id(maria))
# maria.first_name = "Maria"  # theoretisch möglich, aber verletzt OOP stil
print(maria.first_name)
print(Person._counter)
print("Anzahl erstellter Personen: ", Person.how_many_persons())

"""
1. Lokale Variable
2. Methode Variable
3. Klasse Variable
"""