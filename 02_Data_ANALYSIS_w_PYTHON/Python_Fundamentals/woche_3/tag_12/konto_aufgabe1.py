class Konto:
    """Diese Klasse haben einen Kontostand und Funktionen,
     um Geld einzuzahlen und Geld auszahlen."""

    def set_stand_anzeigen(self, einzahlen: float, auszahlen: float) -> None:
        self.stand_anzeigen = einzahlen - auszahlen

    def get_stand_anzeigen(self):
        return self.stand_anzeigen

    def set_einzahlen(self, einzahlen: float) -> None:
        self.einzahlen = einzahlen

    def get_einzahlen(self):
        return self.einzahlen

    def set_auszahlen(self, auszahlen: float) -> None:
        self.auszahlen = auszahlen

    def get_auszahlen(self):
        return self.auszahlen

    def infos(self):
        print(f"Konto Stand: {self.stand_anzeigen}, Einzahlen: {self.einzahlen}, Auszahlen: {self.auszahlen}")


my_konto = Konto()
my_konto.set_einzahlen(200)
my_konto.set_auszahlen(0)
my_konto.set_stand_anzeigen(my_konto.get_einzahlen(), my_konto.get_auszahlen())
my_konto.infos()
my_konto.set_auszahlen(100)
my_konto.set_stand_anzeigen(my_konto.get_einzahlen(), my_konto.get_auszahlen())
my_konto.infos()