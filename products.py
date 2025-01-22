""" This module manages product attributes.
    It allows to calculate the total price for a given quantity of the product.
"""

class Product:
    """ Allows you to create product instances with their own attributes """
    def __init__(self, name, price, quantity):
        try:
            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = True

            if name == "":
                raise Exception("The name of the product is empty")

            if price < 0:
                raise Exception("The price can't be negative")

            if quantity < 0:
                raise Exception("The quantity can't be negative")

        except TypeError:
            print("Type value is invalid")


    def get_quantity(self):
        """ Return the quantity of a product """
        return self.quantity

    def set_quantity(self, quantity):
        """ Sets the available quantity of a product
            If the Quantity is 0, it deactivates the product
        """
        try:
            self.quantity = int(quantity)
        except ValueError:
            print("Quantity have to be an integer")
        if quantity == 0:
            self.deactivate()

    def is_active(self):
        """ Returns True or False depending on whether the product is active or not. """
        return self.active

    def activate(self):
        """ Activate the product """
        self.active = True

    def deactivate(self):
        """ Deactivate the product """
        self.active = False

    def show(self):
        """ Returns a string with information about the attributes of a product """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, buy_quantity):
        """ Returns the total price for a given quantity of a product
            Validates the given quantity, which has to be a positive number.
            If there is not enough in stock, a warning is printed.
        """
        try:
            if buy_quantity > self.quantity:
                print("Error while making order! Quantity larger than what exists")
                #raise Exception("Not enough Quantity in stock")
            if buy_quantity < 1:
                raise Exception("Quantity must be a positive number and at least 1")
            total_price = self.price * buy_quantity
            self.quantity -= buy_quantity
            self.set_quantity(self.quantity)
        except TypeError:
            print("buy_quantity have to be an integer.")
        else:
            return total_price


# TEST: Product deactivate by buy/Quantity
# my_pr = Product('my_pr', 100, 100)
# print(my_pr.show())
# print(my_pr.is_active())
# my_pr.buy(100)
# print(my_pr.show())
# print(my_pr.is_active())