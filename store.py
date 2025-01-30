"""
    This module manages the list of products in the store.
"""
import products


class Store:
    """ Creates a store by starting it with a list of products """
    def __init__(self, products_list):
        try:
            if type(products_list) is not list:
                raise Exception("To create a Store instance, you have to enter a list of products as argument")
        except Exception as error:
            print(error)
        else:
            self.products_list = products_list


    def __contains__(self, product):
        return product in self.products_list


    def __add__(self, other):
        sum_lists = self.products_list + other.products_list
        return Store(sum_lists)


    def add_product(self, prod):
        """ Allows to add a product to the product list """
        try:
            if not isinstance(prod, products.Product):
                raise Exception("The product have to be created as a class Product from products.py")
        except Exception as error:
            print(error)
            return
        else:
            self.products_list.append(prod)


    def remove_product(self, product):
        """ Allows to remove a product from the product list """
        self.products_list.remove(product)


    def get_total_quantity(self):
        """ Prints the total of products in the store """
        total_quantity = 0
        for product in self.products_list:
            total_quantity += product.quantity
        print(f"\nTotal of {total_quantity} items in store\n")


    def get_all_products(self):
        """
            Check if the product is active.
            If it is not active it removes it from the products list to not show it
            and not count it as a purchase option.
            Prints a numbered list of products
        """
        print()
        for product in self.products_list:
            if not product.is_active():
                self.remove_product(product)

        for index, product in enumerate(self.products_list):
            if not product.is_active():
                self.remove_product(product)
            elif product.is_active():
                promo = product.promotion
                print(f"{index+1}. {product}. Promotion: {promo}")
        print()


def order(shopping_list):
    """
        Gets a list of tuples from the user.
        Each tuple contains the product index and the quantity of this product to order.
        Returns the total price for the entire purchase
    """
    total_order = 0
    for product, quantity in shopping_list:
        total_product_price = product.buy(quantity) # Product price * quantity
        total_order = total_order + total_product_price # Result of all products purchased
    return total_order
