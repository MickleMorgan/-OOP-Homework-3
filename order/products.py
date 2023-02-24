"""
Module for Products class.
"""
from negative_price import Negative_price


class Products:
    """
    Class that defines a product with its name and price.
    """

    def __init__(self, name, price):
        """
        Constructor method to create a product.

        :param name: str, name of the product.
        :param price: float, price of the product.
        :raises: Negative_price if the price is negative or zero.
        """
        if price <= 0:
            raise Negative_price
        self.price = price
        self.name = name

    def __str__(self):
        return f'{self.name}, cost {self.price} $'
