import pytest
import products

# Create a normal product
def test_create_prod():
    test_product = products.Product("my_prod", price=100, quantity=100)
    assert type(test_product) == products.Product

# Empty name
def test_empty_name():
    with pytest.raises(Exception):
        products.Product("", price=1450, quantity=100)

# Negative Price()
def test_negative_price():
    with pytest.raises(Exception):
        products.Product("MacBook Air M2", price=-10, quantity=100)

# Product is inactive
def test_prod_inactive():
    my_prod = products.Product("MacBook Air M2", price=10, quantity=10)
    my_prod.quantity = 0
    assert my_prod.is_active() == False

# Test that product purchase modifies the quantity and returns the right output.
def test_update_quantity():
    my_prod = products.Product("MacBook Air M2", price=10, quantity=10)
    my_prod.buy(5)
    assert my_prod.quantity == 5

# Test that buying a larger quantity than exists invokes exception.
def test_buying_larger_quantity():
    with pytest.raises(Exception):
        my_prod = products.Product("MacBook Air M2", price=10, quantity=10)
        my_prod.buy(11)
