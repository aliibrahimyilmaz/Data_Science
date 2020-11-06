class Person:
    name = "Spock"  # Classen Attribute

    def say_hello(self):  # Wir haben hier eine Methode definiert.
        """Methode say_hello sagt hello"""
        print("self.name aus Methode say_hello(): ", self.name)
        print("hello")

# Zugriff auf Attribute erfolgt über Dot-Notation
p1 = Person()
p1.age = 23  # Objekten Attribute, Instance oder Variable
p1.name = "Horst"
p1.hair_color = "black"
print(p1.name, p1.age, p1.hair_color)
p1.say_hello()  # wir haben hier eine Methode .say_hello()
print(p1)  # ahnlich mit zeile 6
############################################################
p2 = Person()
p2.age = 43
print(p2.name, p2.age)
p2.say_hello()

# Zugriff auf Methode get der Dict-Klasse via Dot-Notation
d = {
    "k": 3
}
d.get("k")  # d ist eine Objekte von Classen Dict, und Classe hat einen methode get().

# .get() is eine Methode oder Klassenfunktionen


