# Task 1

import math

class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length, self.width = length, width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1, self.side2, self.side3 = side1, side2, side3

    def calculate_area(self):
        s = sum((self.side1, self.side2, self.side3)) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def calculate_perimeter(self):
        return sum((self.side1, self.side2, self.side3))

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)

for shape in [circle, rectangle, triangle]:
    print(f'{shape.__class__.__name__} - Area: {shape.calculate_area()}, Perimeter: {shape.calculate_perimeter()}')

# Task 2

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class CreditCard(PaymentMethod):
    def make_payment(self, amount):
        print(f'Credit Card: {amount}')

class BankTransfer(PaymentMethod):
    def make_payment(self, amount):
        print(f'Bank Transfer: {amount}')

class EWallet(PaymentMethod):
    def make_payment(self, amount):
        print(f'E-Wallet: {amount}')

class PaymentProcessor:
    def __init__(self):
        self.payment_methods = []

    def add_payment_method(self, payment_method):
        self.payment_methods.append(payment_method)

    def make_payment(self, amount, method_index):
        try:
            method = self.payment_methods[method_index]
            method.make_payment(amount)
        except IndexError:
            print('Invalid payment method')

credit_card, bank_transfer, e_wallet = CreditCard(), BankTransfer(), EWallet()

payment_processor = PaymentProcessor()
payment_processor.add_payment_method(credit_card)
payment_processor.add_payment_method(bank_transfer)
payment_processor.add_payment_method(e_wallet)

payment_processor.make_payment(50, 0)  
payment_processor.make_payment(100, 1)  
payment_processor.make_payment(30, 2) 
