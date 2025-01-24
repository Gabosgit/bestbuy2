"""
"""

from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, promo_name):
        self.promo_name = promo_name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass

class PercentDiscount(Promotion):
    def __init__(self, promo_name, percent):
        super().__init__(promo_name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        super().apply_promotion(product, quantity)


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        return "Price with applied discount"

class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        return "Price with applied discount"

# TEST class Promotion
#new_promotion = PercentDiscount('new_promotion')