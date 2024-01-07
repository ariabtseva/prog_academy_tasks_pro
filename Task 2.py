# Task 2.1

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

    def __str__(self):
        cart_str = f'Shopping Cart for {self.customer}:\n'
        for item in self.products.values():
            cart_str += f'{item["product"]} x{item["quantity"]}\n'
        cart_str += f'Total: ${self.calculate_total():.2f}'
        return cart_str

product_1 = Product('Sofa', 599.99, 'Comfortable and stylish sofa for your living room')
product_2 = Product('Coffee Maker', 49.99, 'Drip coffee maker with programmable timer')
product_3 = Product('Bedroom Set', 899.00, 'Complete bedroom set with bed, dresser, and nightstands')

cart = Cart('James Smith')
cart.add_product(product_1, 2)
cart.add_product(product_2, 1)
cart.add_product(product_3, 1)

print(cart)

# Task 2.2

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
        for dish in self.dishes:
            category_str += f'{dish}\n'
        return category_str
    
class RestaurantMenu:
    def __init__(self, categories):
        self.categories = categories

    def __str__(self):
        menu_str = 'Restaurant Menu:\n'
        for category in self.categories:
            menu_str += f'{category}\n'
        return menu_str
    
dish_1 = Dish('Caesar Salad', 'Greek salad', 10.99)
dish_2 = Dish('Spaghetti Bolognese', 'Pasta with cream sauce', 12.99)
dish_3 = Dish('Cheesecake', 'Tiramisu', 7.99)

category_appetizers = MenuCategory('Appetizers', [dish_1])
category_main_courses = MenuCategory('Main Courses', [dish_2])
category_desserts = MenuCategory('Desserts', [dish_3])

restaurant_menu = RestaurantMenu([category_appetizers, category_main_courses, category_desserts])

print(restaurant_menu)