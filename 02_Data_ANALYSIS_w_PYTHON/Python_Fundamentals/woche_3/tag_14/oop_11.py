class Rectangle:
    """
    Diese Klasse beschreibt ein Rechteck Länge, Breite
    r = Rectangle(3, 8)
    """
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def area(self) -> float:
        """
        calculate the area of rect
        """
        return self.a * self.b


class Square(Rectangle):
    """
        Diese Square ist ein Spezialfall von Rectangle
        Seitenlänge
        r = Square(4)
    """
    def __init__(self, a: float):
        super().__init__(a, a)


r = Rectangle(3, 8)
print("rectangle area:", r.area())

s = Square(4)
print("square area:", s.area())
