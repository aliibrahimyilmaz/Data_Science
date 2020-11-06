class Car:
    """this class represents a car
    # color, manufacturer, type, doors, year
    """
    features = {}
    used_by = []  # häufiger Fehler
    def set_color(self, color: str) -> None:
        """Setter Methode, um Attribute zu setzen (set)"""
        self.color = color

    def get_color(self) -> str:
        """Getter Methode, um Zugriff auf Attribute zu gewährleisten : garantieren"""
        return self.color

    def set_manufacturer(self, m: str) -> None:
        """Setter Methode, um Attribute zu setzen (set)"""
        self.manufacturer = m

    def get_manufacturer(self) -> str:
        """Getter Methode, um Zugriff auf Attribute zu gewährleisten : garantieren"""
        return self.manufacturer

    def set_type(self, type: str) -> None:
        """Setter Methode, um Attribute zu setzen (set)"""
        self.type = type

    def get_type(self) -> str:
        """Getter Methode, um Zugriff auf Attribute zu gewährleisten : garantieren"""
        return self.type

    def set_year(self, year: int) -> None:
        """Setter Methode, um Attribute zu setzen (set)"""
        self.year = year

    def get_year(self) -> int:
        """Getter Methode, um Zugriff auf Attribute zu gewährleisten : garantieren"""
        return self.year

    def set_features(self, f):
        """set features dictionary"""
        self.features = f

    def set_used_by(self, driver_name: str) -> None:
        """append mit Methode benutzt"""
        self.used_by.append(driver_name)

    def infos(self):
        print(self.used_by)
        print(f"{self.manufacturer} {self.type} {self.year} {self.color} Features: {self.features}")

special_features = {
    "radio": True,
    "v8_engine" : False,
    "sun_roof" : True,
}

bmw = Car()  # Instanziierung  # eine Objekte zurück
bmw.set_manufacturer("BMW")
bmw.set_color("weiss")
bmw.set_year(1983)
bmw.set_type("Z3")
bmw.set_features(special_features)
bmw.set_used_by("ali")
bmw.set_used_by("stan")
bmw.set_used_by("wiebke")
bmw.infos()
print(bmw.__dict__)  # dict, alle Attribute, die dieses Objekt gerade enthält: SUPER!

audi = Car()  # Instanziierung  # eine Objekte zurück
audi.set_manufacturer("Audi")
audi.set_color("rot")
audi.set_year(1998)
audi.set_type("A3")
audi.set_used_by("wiebke")
audi.set_used_by("sara")
# audi.set_features(special_features)
audi.infos()
# print(audi.__dict__)  # dict, alle Attribute, die dieses Objekt gerade enthält: SUPER!

