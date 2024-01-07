import logging

logger = logging.getLogger(__name__)

class InvalidOrderValue(Exception):
    def __init__(self, message='Invalid order value: must be bigger than zero.'):
        super().__init__(message)
        logger.error(message)

class Client:
    def __init__(self, name, discount):
        self.name, self.discount = name, discount
        logger.info(f'Client "{self.name}" created with discount: {self.discount.value}%')

    def get_total_price(self, order):
        total_price = sum(order.values())
        discounted_price = self.discount.apply_discount(total_price)
        logger.info(f'Total price calculated for {self.name}: {discounted_price}')
        return discounted_price