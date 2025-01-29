""" This module manages product attributes.
    It allows to calculate the total price for a given quantity of the product.
"""

import promotions


class Product:
    """ Allows you to create product instances with their own attributes """
    def __init__(self, name, price, quantity):
        self.promotion = None
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

    def get_price_by_promotion(self, buy_quantity):
        # Update final price by promotion
        if type(self.promotion) == promotions.PercentDiscount:
            final_price = self.promotion.apply_promotion(self, buy_quantity)
            return final_price

        if type(self.promotion) == promotions.ThirdOneFree:
            final_price = self.promotion.apply_promotion(self, buy_quantity)
            return final_price

        if type(self.promotion) == promotions.SecondHalfPrice:
            final_price = self.promotion.apply_promotion(self, buy_quantity)
            return final_price

        final_price = self.price * buy_quantity
        return final_price

    def buy(self, buy_quantity):
        """ Returns the total price for a given quantity of a product
            Validates the given quantity, which has to be a positive number.
            If there is not enough in stock, a warning is printed.
        """
        try:
            if buy_quantity > self.quantity:
                #print("Error while making order! Quantity larger than what exists")
                raise Exception("Error while making order! Quantity larger than what exists")
            if buy_quantity < 1:
                raise Exception("Quantity must be a positive number and at least 1")
        except TypeError:
            return "buy_quantity have to be an integer."
        else:
            # Update Quantity
            self.quantity -= buy_quantity
            self.set_quantity(self.quantity)
            # Update final price by promotion
            final_price = self.get_price_by_promotion(buy_quantity)
            return final_price

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promo):
        """ Sets a promotion to the product by promo name """
        self.promotion = promo

    def __str__(self):
        """ Returns a string with information about the attributes of a product """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)
        self.quantity = 0

    def buy(self, buy_quantity):
        # Update final price by promotion
        final_price = self.get_price_by_promotion(buy_quantity)
        return final_price

    def __str__(self):
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
            # Update final price by promotion
            final_price = self.get_price_by_promotion(buy_quantity)
            return final_price

    def __str__(self):
        """ Returns a string with information about the attributes of a product """
        return f"{self.name}, Price: {self.price}, Limited to {self.maximum} per order!"


# # Create product
# new_pro = Product("prod_with_promo", 100, 100)
#
# # Buy products
# print(new_pro.buy(200))

# # Create a NonStockedProduct
# new_NonStockedProduct = NonStockedProduct('new_NonStockedProduct', 100)

# Create promotion
# new_promo_percent_discount = promotions.PercentDiscount('30 % OFF', 30)
# new_promo_ThirdOneFree = promotions.ThirdOneFree('3ht free')
# new_promo_SecondHalfPrice = promotions.SecondHalfPrice('MY Second Halp Price!')
#
# Set promotion to products
#new_pro.set_promotion(new_promo_SecondHalfPrice)
# new_NonStockedProduct.set_promotion(new_promo_ThirdOneFree)
#


# GET QUANTITY
#print(prod_with_promo.get_quantity())
#print(new_NonStockedProduct.buy(1))

