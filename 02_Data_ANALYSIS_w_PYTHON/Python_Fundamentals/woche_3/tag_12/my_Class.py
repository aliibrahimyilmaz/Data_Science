class Tablet:
    """this class represents alle Tabletten
        # manufacturer, color, screen, ram, harddisk
    """
    def __init__(self, manufacturer: str, color: str, screen: float, ram: float, harddisk: int) -> None:
        self.manufacturer = manufacturer
        self.color = color
        self.screen = screen
        self.ram = ram
        self.harddisk = harddisk

    def set_manufacturer(self, manufacturer: str) -> None:
        self.manufacturer = manufacturer

    def set_color(self, color: str) -> None:
        self.color = color

    def set_screen(self, screen: str) -> None:
        self.screen = screen

    def set_ram(self, ram: str) -> None:
        self.ram = ram

    def get_ram(self):
        return self.ram

    def set_harddisk(self, harddisk: str) -> None:
        self.harddisk = harddisk

    def infos(self):
        print(f"{self.manufacturer}, {self.color}, {self.screen} inches, {self.ram} GB RAM, {self.harddisk} GB HARDDISK")

iphone = Tablet("Apple", "white", 10.5, 3, 32)
iphone.infos()  # man kann die attributen sowohl mit infos() methode aufrufen als auch mit get() methode
iphone.set_manufacturer("LG")  # man braucht set() methode auch für das Update der Attributen
print(f"iphone_ram: {iphone.ram} GB")  # Nutzung der Attribute wie hier ist nicht OOP
print(f"iphone_ram: {iphone.get_ram()} GB")  # get() Methode ist pythonisch und man muss das für attributen benutzen.

samsung = Tablet("Samsung", "black", 9.7, 2, 16)
samsung.infos()

