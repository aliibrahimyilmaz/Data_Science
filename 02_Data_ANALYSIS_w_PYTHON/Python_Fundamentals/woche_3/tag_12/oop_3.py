class Animal:
    """diese Klasse beschreibt ein Tier"""

    def set_name(self, name: str) -> None:
        """Setter Methode, um Attribute zu setzen (set)"""
        self.name = name

    def get_name(self) -> str:
        """Getter Methode, um Zugriff auf Attribute zu gewährleisten : garantieren"""
        return self.name

    def set_type(self, type: str):
        self.type = type

    def get_type(self) -> str:
        return self.type

    def infos(self) -> None:
        print(f"Das Tier heisst {self.name} und ist ein {self.type}")  # man kann alle Werte ausgeben

tier1 = Animal()
tier1.set_type("dog")
tier1.set_name("Fiffi")

print(tier1.name)  # direktes Zugreifen auf Attribute ist schlechter Stil
print("über get-Methode", tier1.get_name())
print(tier1.type)
print("über get-Methode", tier1.get_type())
tier1.infos()
