# Task 1

class Account:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    @property
    def balance(self):
        return self.__balance

    def __setattr__(self, name, value):
        if name == 'balance':
            raise AttributeError('Direct modification of balance is not allowed')
        else:
            object.__setattr__(self, name, value)

    def __getattr__(self, name):
        raise AttributeError('Property does not exist')

account = Account(1000)
print('Initial balance:', account.balance)

try:
    account.balance = 1500
except AttributeError as e:
    print(f'Error: {e}')

# Task 2

class User:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    def __setattr__(self, key, value):
        if key in ('first_name', 'last_name'):
            raise AttributeError("Can't set attribute")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return 'No such attribute'

user = User('John', 'Doe')

try:
    user.first_name = 'Jane'
except AttributeError as e:
    print(f'Error: {e}')

try:
    print(user.someOtherProperty)
except AttributeError as e:
    print(f'Error: {e}')

# Task 3

class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def __setattr__(self, key, value):
        if key in ('width', 'height'):
            if not value:
                pass
            elif value <= 0:
                raise ValueError(f'Property does not exist')
            elif f'_Rectangle__{key}' not in self.__dict__:
                self.__dict__[f'_Rectangle__{key}'] = value
        else:
            object.__setattr__(self, key, value)
    
    def area(self):
        return self.__width * self.__height

rectangle = Rectangle(5, 8)

try:
    rectangle.width = 10
except AttributeError as e:
    print(f'Error: {e}')

try:
    print(rectangle.someOtherProperty)
except AttributeError as e:
    print(f'Error: {e}')

print('Area of the rectangle:', rectangle.area())