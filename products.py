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


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)
        #self.quantity = 0

    def buy(self, buy_quantity):
        total_price = self.price * buy_quantity
        return total_price

    def show(self):
        """ Returns a string with information about the attributes of a product """
        return f"{self.name}, Price: {self.price}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, buy_quantity):
        super().buy(buy_quantity)
        try:
            if buy_quantity > self.maximum:
                raise Exception(f"The max Quantity to order is {self.maximum}")
        except Exception as e:
            print(e)
            buy_quantity = input("Enter a valid quantity: ")
        else:
            total_price = self.price * buy_quantity
            return total_price

    def show(self):
        """ Returns a string with information about the attributes of a product """
        return f"{self.name}, Price: {self.price}, max-Quantity: {self.maximum}"


# # TEST - Buy a LimitedProduct
#my_LimitedProduct = LimitedProduct('my_LimitedProduct', 120, 120, 1)
#print(my_LimitedProduct.show())
#my_LimitedProduct.buy(1)

# # TEST - Buy a NonStockedProduct without Stock Quantity
# my_NonStockedProduct = NonStockedProduct('NonStockedProduct', 120)
# print(my_NonStockedProduct.show())
# print(my_NonStockedProduct.buy(2))

# # TEST: - Product deactivate by buy/Quantity
# my_pr = Product('my_pr', 100, 100)
# print(my_pr.show())
# print(my_pr.is_active())
# my_pr.buy(100)
# print(my_pr.show())
# print(my_pr.is_active())
