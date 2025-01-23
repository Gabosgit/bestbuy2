import pytest
import products

#Create a normal product
def test_create_prod():
    products.Product("my_prod", price=100, quantity=100)

# Empty name
def test_empty_name():
    with pytest.raises(Exception):
        products.Product("", price=1450, quantity=100)

def test_negative_price():
    with pytest.raises(Exception):
        products.Product("MacBook Air M2", price=-10, quantity=100)

def test_prod_inactive():
    my_prod = products.Product("MacBook Air M2", price=10, quantity=10)
    my_prod.set_quantity(0)
    if my_prod.is_active() == False:
        return True



# test_empty_name()
# test_negative_price()


