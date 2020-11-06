# Übungsaufgabe: Klasse Ellipse modellieren und davon KLasse Circle ableiten
from math import pi
class Ellipse:
    """
    Diese Klasse beschreibt ein Ellipse mit zwei Axis
    e = Ellipse(a, b)
    """
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def area(self) -> float:
        """
        calculate the area of ellipse
        """
        return round((pi * self.a * self.b), 3)


class Circle(Ellipse):
    """
        Diese Circle ist ein Spezialfall von Ellipse
        c = Circle(a)
    """
    def __init__(self, a: float):
        super().__init__(a, a)


e = Ellipse(3, 5)
print("Ellipse area:", e.area())

c = Circle(4)
print("Circle area:", c.area())
