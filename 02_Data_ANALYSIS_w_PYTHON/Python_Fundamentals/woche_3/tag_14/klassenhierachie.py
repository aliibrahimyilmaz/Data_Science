# Aufgabe: Klassenhierachie Personen an Uni


class Person:
    """BAsis Klasse aller Personen, die sich an einer Uni finden"""
    def __init__(self, first_name: str, last_name: str, birthday: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday


class Student(Person):
    """Student hat Matrikelnummer
        ali = Student('Ali', 'Yilmaz', '01.01.1999', '78/323343')
    """

    def __init__(self, first_name: str, last_name: str, birthday: str, nr: str) -> None:
        super().__init__(first_name, last_name, birthday)
        self.nr = nr
        self.fachbereich = None

    def set_fachbereich(self, v):
        self.fachbereich = v

    def info(self):
        print(f"Student {self.first_name} {self.last_name} im Fachbereich {self.fachbereich} hat die Nummer: {self.nr}")


class Mitarbeiter(Person):
    """Mitarbeiter hat Steuernummer
        emil = Mitarbeiter('Emil', 'Brown', '01.01.1993', '93/212112')
    """

    def __init__(self, first_name: str, last_name: str, birthday: str, steuer_nr: str) -> None:
        super().__init__(first_name, last_name, birthday)
        self.steuer_nr = steuer_nr
        self.chefid = None

    def set_chef_id(self, id: int) -> None:
        self.chefid = id

    def info(self):
        print(f"Mitarbeiter {self.first_name} {self.last_name} mit der Steuernummer {self.steuer_nr} hat die ChefId: {self.chefid}")


ali = Student('Ali', 'Yilmaz', '01.01.1999', '78/323343')
ali.set_fachbereich("Python")
ali.info()

emil = Mitarbeiter('Emil', 'Brown', '01.01.1993', '93/212112')
emil.set_chef_id(2)
emil.info()




