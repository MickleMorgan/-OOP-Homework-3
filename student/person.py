class Person:
    """
        Class representing a person.

        Attributes:
            name (str): First name of the person.
            surname (str): Last name of the person.
            sex (str): Sex of the person.
            age (int): Age of the person.
            nationality (str): Nationality of the person.
    """
    def __init__(self, name, surname, sex, age, nationality):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age
        self.nationality = nationality

    def __str__(self):
        """
                Returns a string representation of the person.

                Raises:
                    TypeError: If the person's nationality is Russian.

                Returns:
                    str: String representation of the person.
        """
        if self.nationality.lower() == ('russian'):
            raise TypeError('russian ship go to hell')
        else:
            return f'Name: {self.name} {self.surname}\nSex: {self.sex}\nAge {self.age} years\n' \
                   f'Nationality {self.nationality}'