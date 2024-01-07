# Task 3/4/5

import logging
from order import Client, InvalidOrderValue
from discount import Discount, RegularDiscount, SilverDiscount, GoldDiscount, InvalidDiscountValue

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

terminal_handler = logging.StreamHandler()
file_handler = logging.FileHandler('log.txt')

logging.basicConfig(level=logging.DEBUG)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
terminal_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(terminal_handler)
logger.addHandler(file_handler)

client_1 = Client('John', RegularDiscount(10))
client_2 = Client('Alice', SilverDiscount(15))
client_3 = Client('Bob', GoldDiscount(20))

order = {'item1': 10, 'item2': 20, 'item3': 15}

print(f'Regular client total price: {client_1.get_total_price(order)}')
print(f'Silver client total price: {client_2.get_total_price(order)}')
print(f'Gold client total price: {client_3.get_total_price(order)}')