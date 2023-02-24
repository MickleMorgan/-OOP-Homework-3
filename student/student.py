from person import Person


class Student(Person):
    def __init__(self, name, surname, sex, age, nationality, status):
        super().__init__(name, surname, sex, age, nationality)
        self.status = status

    def __str__(self):
        return f'{super().__str__()}\nStatus:{self.status}\n'
