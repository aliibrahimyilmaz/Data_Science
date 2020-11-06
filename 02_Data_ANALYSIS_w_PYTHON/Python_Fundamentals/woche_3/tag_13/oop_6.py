class Car:

    def __init__(self, name, fuel):
        self.name = name
        self.__zaehler = 0
        self.__fuel = fuel  # privates Attribute


    def get_fuel(self):
        return self.__fuel

    def _min(self):  # protected Funktion
        self._int = 3

    def __zaehlerstand(self):  # private Funktionen
        self.__zaehler += 1

    def drive(self):
        self.__zaehlerstand()

    def print_name(self):
        print(self.name)

car = Car('Audi A8', 1000)
print(car.name)  # Sichtbar von Attribute name ist public
car.print_name()  # Sichtbarkeit der Methode print_name is public
car.__fuel = 100  # ???
print(car.get_fuel())
print(car.__dict__)  # alle Attribute eines Objektes zeigen
"""{'name': 'Audi A8', '_Car__fuel': 1000, '__fuel': 100} mangling"""
car.drive()
print(car.__dict__)  # alle Attribute eines Objektes zeigen
