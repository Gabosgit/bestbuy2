"""
    Setup promotions to be applied to products
"""
from abc import ABC, abstractmethod


class Promotion(ABC):
    """ Create an abstract class to set up promotions """
    def __init__(self, promo_name):
        self.promo_name = promo_name


    @abstractmethod
    def apply_promotion(self, product, quantity):
        """ To set up the application of promotions """
        pass


    def __str__(self):
        return self.promo_name


class PercentDiscount(Promotion):
    def __init__(self, promo_name, percent):
        super().__init__(promo_name)
        self.percent = percent


    def apply_promotion(self, product, quantity):
        """ Applies the promotion returning a final price """
        super().apply_promotion(product, quantity)
        price_prod = product.price
        final_price = price_prod * 0.70 * quantity
        return final_price


class ThirdOneFree(Promotion):
    def __init__(self, promo_name):
        super().__init__(promo_name)


    def apply_promotion(self, product, quantity):
        """ Applies the promotion returning a final price """
        super().apply_promotion(product, quantity)
        amount_promos_to_apply = quantity // 3
        quantity_to_apply = quantity - amount_promos_to_apply
        price_prod = product.price
        final_price = price_prod * quantity_to_apply
        return final_price


class SecondHalfPrice(Promotion):
    def __init__(self, promo_name):
        super().__init__(promo_name)


    def apply_promotion(self, product, quantity):
        """ Applies the promotion returning a final price """
        price_prod = product.price
        amount_promos_to_apply = quantity // 2
        price_applied = amount_promos_to_apply * (price_prod / 2)
        amount_normal_price = quantity - amount_promos_to_apply
        price_normal = amount_normal_price * price_prod
        final_price = price_applied + price_normal
        return final_price
