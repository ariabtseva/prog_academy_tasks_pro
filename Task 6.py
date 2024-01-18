# Task 2.1 / 6.1 / 7.1

class Product:
    
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f'{self.name} - ${self.price:.2f}\n {self.description}'

class Cart:
    
    def __init__(self, customer):
        self.products = {}
        self.customer = customer

    def add_product(self, product: Product, quantity: int = 1):
        if not isinstance(product, Product):
            raise ValueError('Not a product')
        
        if product.name in self.products:
            self.products[product.name]['quantity'] += quantity
        else:
            self.products[product.name] = {'product': product, 'quantity': quantity}

    def calculate_total(self):
        total = sum(item['product'].price * item['quantity'] for item in self.products.values())
        return total
    
    def __iadd__(self, other):
        if not isinstance(other, Cart):
            raise ValueError('Invalid type for Cart addition')
        
        for product_name, item in other.products.items():
            if product_name in self.products:
                self.products[product_name]['quantity'] += item['quantity']
            else:
                self.products[product_name] = item

        return self

    def __iter__(self):
        self._iter_items = iter(self.products.values())
        return self

    def __next__(self):
        try:
            item = next(self._iter_items)
            return f'{item["product"]} x{item["quantity"]}'
        except StopIteration:
            raise StopIteration

    def __str__(self):
        cart_str = f'Shopping Cart for {self.customer}:\n'
        cart_str += '\n'.join(self)
        cart_str += f'\nTotal: ${self.calculate_total():.2f}'
        return cart_str

product_1 = Product('Sofa', 599.99, 'Comfortable and stylish sofa for your living room')
product_2 = Product('Coffee Maker', 49.99, 'Drip coffee maker with programmable timer')
product_3 = Product('Bedroom Set', 899.00, 'Complete bedroom set with bed, dresser, and nightstands')

cart_1 = Cart('James Smith')
cart_1.add_product(product_1, 2)
cart_1.add_product(product_3, 1)

cart_2 = Cart("John Doe")
cart_2.add_product(product_2, 1)

cart_1 += cart_2

print(cart_1)

# Task 2.2 / 6.2 / 7.2

class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f'{self.name} - ${self.price:.2f}\n {self.description}'

class MenuCategory:
    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes

    def __str__(self):
        category_str = f'{self.name}:\n'
        category_str += '\n'.join(map(str, self.dishes))
        return category_str

class RestaurantMenu:
    def __init__(self, categories):
        self.categories = categories

    def __str__(self):
        menu_str = 'Restaurant Menu:\n'
        for category in self.categories:
            menu_str += f'{category}\n'
        return menu_str

class Order:
    def __init__(self):
        self.items = []

    def __iadd__(self, other):
        if isinstance(other, Dish):
            self.items.append(other)
            return self
        else:
            raise ValueError('Can only add Dish objects to the order')

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total
    
    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index < len(self.items):
            item = self.items[self._iter_index]
            self._iter_index += 1
            return item
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.items[index]

    def __str__(self):
        order_str = 'Order:\n'
        for item in self.items:
            order_str += f'{item}\n'
        order_str += f'Total: ${self.calculate_total():.2f}'
        return order_str

dish_1 = Dish('Caesar Salad', 'Classic Caesar salad with chicken', 10.99)
dish_2 = Dish('Spaghetti Bolognese', 'Traditional Italian pasta with meat sauce', 12.99)
dish_3 = Dish('Cheesecake', 'Creamy shortcake', 7.99)

category_appetizers = MenuCategory('Appetizers', [dish_1])
category_main_courses = MenuCategory('Main Courses', [dish_2])
category_desserts = MenuCategory('Desserts', [dish_3])

restaurant_menu = RestaurantMenu([category_appetizers, category_main_courses, category_desserts])

print(restaurant_menu)

order = Order()

order += dish_1
order += dish_2

print(order[0])

# Task 6.3

import math

class ProperFraction:
    def __init__(self, numerator, denominator):
        common_divisor = math.gcd(numerator, denominator)
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return (self.numerator * other.denominator) < (other.numerator * self.denominator)

    def operate(self, other, operator):
        new_numerator = operator(self.numerator * other.denominator, other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)
    
    def __add__(self, other):
        return self.operate(other, lambda x, y: x + y)

    def __sub__(self, other):
        return self.operate(other, lambda x, y: x - y)

    def __mul__(self, other):
        return self.operate(other, lambda x, y: x * y)

fraction1 = ProperFraction(1, 2)
fraction2 = ProperFraction(3, 4)

sum_result = fraction1 + fraction2
difference_result = fraction1 - fraction2
product_result = fraction1 * fraction2

print(f'Fraction 1: {fraction1}')
print(f'Fraction 2: {fraction2}')
print(f'Sum: {fraction1 + fraction2}')
print(f'Difference: {fraction1 - fraction2}')
print(f'Product: {fraction1 * fraction2}')