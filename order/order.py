"""
Module for Order class.
"""
from products import Products


class Order:
    """
    Class that defines an order with a customer and a cart of products.
    """

    def __init__(self, customer):
        self.customer = customer
        self.cart = {}

    def add_product(self, product, quantities):
        """
        Add a product to the cart of the order.

        :param product: Products object, product to add to the cart.
        :param quantities: int, number of products to add to the cart.
        """
        self.cart.update({product: quantities})

    def summa_of_order(self):
        """
        Calculate the total price of the order.

        :return: float, total price of the order.
        """
        summa = 0
        for item in self.cart:
            summa += item.price * self.cart[item]
        return summa

    def __str__(self):
        """
        String representation of the order.

        :return: str, customer's name, surname and phone number, products in the cart and total price of the order.
        """
        result = f'{self.customer.name}, {self.customer.surname}\nPhone: {self.customer.phone}\n'
        for item in self.cart:
            result += f'Product - {item}, quantities {self.cart[item]}\n'
        result += f'Total price {str(self.summa_of_order())} $\n'
        return result
