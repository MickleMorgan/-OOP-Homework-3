"""
Module for Customer class.
"""


class Customer:
    """
    Class that defines a customer with its name, surname and phone number.
    """

    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return f'{self.name}, {self.surname}, Phone: {self.phone}'
