"""
Module for custom Negative_price exception.
"""


class Negative_price(Exception):
    """
    Exception to handle negative or zero price values.
    """

    def __init__(self):
        pass

    def __str__(self):
        return f'Price can\'t be negative or zero'
