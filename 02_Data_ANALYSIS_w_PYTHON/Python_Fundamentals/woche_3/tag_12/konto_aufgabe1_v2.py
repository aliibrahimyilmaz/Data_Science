class Konto:
    """Diese Klasse haben einen Kontostand und Funktionen,
     um Geld einzuzahlen und Geld auszahlen."""

    def __init__(self, konto_stand: float):  # konto_stand
        self.konto_stand = konto_stand

    def einzahlen(self, einzahlen: float) -> None:
        self.konto_stand = self.konto_stand + einzahlen

    def auszahlen(self, auszahlen: float) -> None:
        self.konto_stand = self.konto_stand - auszahlen

    def stand_anzeigen(self) -> None:
        print(f"Konto Stand: {self.konto_stand}")


my_konto = Konto(0)
my_konto.einzahlen(200)
my_konto.auszahlen(80)
my_konto.stand_anzeigen()
