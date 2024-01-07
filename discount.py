import logging

logger = logging.getLogger(__name__)

class InvalidDiscountValue(Exception):
    def __init__(self, message='Invalid discount value: must be between 0 and 100.'):
        super().__init__(message)
        logger.error(message)

class Discount:
    def __init__(self, value):
        if not (0 <= value <= 100):
            raise InvalidDiscountValue()
        self.value = value
        logger.info(f'Discount created: {self.value}%')

    def apply_discount(self, total_price):
        discounted_price = total_price * (1 - self.value / 100)
        return discounted_price

class RegularDiscount(Discount):
    def discount(self):
        return 0.01

class SilverDiscount(Discount):
    def discount(self):
        return 0.05

class GoldDiscount(Discount):
    def discount(self):
        return 0.1