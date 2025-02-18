"""
    This program prints an interface to allow the purchase of the products available in the store.
    The imported "store" module contains the class to be able to manage the orders.
    The imported "products" module contains a class to manage product attributes.
"""
import products
import store
import promotions


def input_int(prompt, length):
    """ Validates that the user input is an integer of a specified length. """
    while True:
        try:
            input_user = input(prompt)
            if input_user == "":
                return input_user
            if int(input_user) < 1:
                raise Exception(f"Expected a number between 1 and {length}")
            if int(input_user) > length:
                raise  Exception(f"Expected a number between 1 and {length}")
            if not str(input_user).isnumeric():
                raise Exception(f"Expected a number between 1 and {length}")
        except ValueError:
            print(f"Expected a positive number (1-{length})")
        except Exception as error:
            print(error)
        else:
            return int(input_user)


def input_numeric(prompt):
    """ Validates that the user's input is a positive integer """
    while True:
        try:
            input_user = input(prompt)
            if input_user == "":
                break
            if not input_user.isnumeric():
                raise Exception("Expected a positive number")
            if int(input_user) < 1:
                raise Exception("Expected a positive number")
        except ValueError:
            print("Expected a positive number")
        except Exception as error:
            print(error)
        else:
            return int(input_user)


def order_menu(store_name):
    """ Print the list of products and manage the order. """
    order_list = []
    print("------")
    store_name.get_all_products()
    print("------")
    while True:
        products_list_length = len(store_name.products_list)
        print("When you want to finish order, enter empty text.")

        input_order_product = str(input_int("Which product # do you want? ", products_list_length))
        input_order_quantity = input_numeric("What amount do you want? ")


        if input_order_product:
            if not input_order_quantity:
                continue

        if input_order_quantity == "" or input_order_product == "":
            print()
            print(f"Order made! Total payment: {store.order(order_list)}\n")
            break
        else:
            get_product_from_list = store_name.products_list[int(input_order_product) - 1]
            if type(get_product_from_list) == products.NonStockedProduct:
                order_list.append((get_product_from_list, int(input_order_quantity)))
                print("\nProduct added to list!\n")
            else:
                get_product_quantity = get_product_from_list.quantity
                if type(get_product_from_list) == products.LimitedProduct:
                    try:
                        if get_product_from_list.maximum < input_order_quantity:
                            raise Exception(f"\nError while making order! Only {get_product_from_list.maximum} is allowed from this product!\n")
                    except Exception as e:
                        print(e)
                    else:
                        order_list.append((get_product_from_list, int(input_order_quantity)))
                        print("\nProduct added to list!\n")
                else:
                    if get_product_quantity < int(input_order_quantity):
                        print("\nError while making order! Quantity larger than what exists\n")
                        break
                    else:
                        order_list.append((get_product_from_list, int(input_order_quantity)))
                        print("\nProduct added to list!\n")


def compare_prices(store_name):
    """
        Prompts the user for 2 products
        Gets the price of these products
        Compares the prices and return a string with the result
    """
    store_name.get_all_products()
    length_list = len(store_name.products_list)
    input_prod_a = input_int("Enter the number of product A to compare: ", length_list)
    input_prod_b = input_int("Enter the number of product B to compare: ", length_list)
    product_a = store_name.products_list[input_prod_a-1]
    product_b = store_name.products_list[input_prod_b-1]
    if product_a < product_b:
        print(f"\nThe price of {product_a.name} ({product_a.price}) is lower that the price of {product_b.name} ({product_b.price})\n")
    else:
        print(f"\nThe price of {product_b.name} ({product_b.price}) is lower that the price of {product_a.name} ({product_a.price})\n")


def print_menu():
    """ Prints the menu options """
    print("\tStore Menu\n"
          "\t----------")
    print("1. List all products in store\n"
          "2. Show total amount in store\n"
          "3. Make an order\n"
          "4. Compare product prices\n"
          "5. Quit")


def start(best_buy):
    """ Controls the menu by allowing the user to select a menu option. """
    options_menu = {
        '1': best_buy.get_all_products,
        '2': best_buy.get_total_quantity,
        '3': order_menu,
        '4': compare_prices
    }
    while True:
        print_menu()
        input_menu_option = input_int(f"Select a number from the menu (1-{len(options_menu)+1}):", len(options_menu)+1)
        if input_menu_option == "":
            print(f"\nExpected a positive number (1-{len(options_menu) + 1})\n")
        elif input_menu_option == len(options_menu)+1:  # 4 exit the app
            print("\n Bye Bye! ")
            break
        elif input_menu_option == 3:
            order_menu(best_buy)
        elif input_menu_option == 4:
            compare_prices(best_buy)
        # elif input_menu_option == 5:
        #     product_exist(best_buy)
        else:
            options_menu[str(input_menu_option)]()


def main():
    """ Create the store and put it to work """
    # Setup initial stock of inventory
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    pixel = products.Product("Google Pixel 7", price=500, quantity=250)
    windows_license = products.NonStockedProduct("Windows License", price=125)
    shipping = products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)

    # Setup list of products
    product_list = [mac, bose, pixel, windows_license, shipping]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    mac.promotion = second_half_price
    bose.promotion = third_one_free
    windows_license.promotion = thirty_percent

    # Running the store
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == '__main__':
    main()
