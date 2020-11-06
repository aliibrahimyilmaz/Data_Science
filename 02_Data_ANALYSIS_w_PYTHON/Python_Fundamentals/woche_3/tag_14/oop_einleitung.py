# Vererbung: Inheritance

# Basisklasse Tier
class Tier:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"{self.name} sagt Hallo!")

# Klasse Hund erbt von Tier
class Hund(Tier):

    # Methode say_hello wurde von Hund überschreiben
    def say_hello(self):
        print(f"{self.name} sagt HavHav..!")

# Klasse Dackel als Spezialfall von Hund
class Dackel(Hund):
    # Dackel macht bisher nichts anderes als Hund
    pass


tier = Tier("Fiffi")
tier.say_hello()
dog = Hund("Wuffi")
dog.say_hello()

dackel = Dackel("Pipa")
dackel.say_hello()
