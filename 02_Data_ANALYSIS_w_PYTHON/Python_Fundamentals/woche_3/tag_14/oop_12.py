# @staticmethod, @classmethod,
# https://www.programiz.com/python-programming/methods/built-in/classmethod

class Person:
    """BAsis Klasse aller Personen, die sich an einer Uni finden"""
    def __init__(self, first_name: str, last_name: str, birthday: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday

    @staticmethod
    def is_adult(age):
        return age > 18

class Student(Person):
    """Student hat Matrikelnummer
        ali = Student('Ali', 'Yilmaz', '01.01.1999', '78/323343')
    """

    def __init__(self, first_name: str, last_name: str, birthday: str, nr: str) -> None:
        super().__init__(first_name, last_name, birthday)
        self.nr = nr
        self.fachbereich = None
        # self.energy = 20

    """ HERKÖMMLICHE WEG
    def set_energy(self, value):
        self.value = value
    
    def get_energy(self):
        return self.energy
    """

    @property  # wie eine get_energy
    def energy(self):
        return self._energy

    @energy.setter  # wie eine set_energy
    def energy(self, value):
        self._energy = value

    @classmethod
    def create_student(cls, fn, ln, b, nr):
        return Student(fn, ln, b, nr)

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
# ali = Student.create_student('Ali', 'Yilmaz', '01.01.1999', '78/323343')  # Klassen Methode decorator
# print(ali.energy)  # das ist schlecht
ali.energy = 20  # direkt zuweisung ist möglich mit property
print(ali.energy)

emil = Mitarbeiter('Emil', 'Brown', '01.01.1993', '93/212112')
emil.set_chef_id(2)
emil.info()




