# Task 1
# Напишіть функцію, яка застосує до списку чисел довільну функцію користувача і поверне суми елементів отриманого списку.

def apply_function_and_sum(numbers, custom_function):
    result_sum = sum(custom_function(number) for number in numbers)
    return result_sum

def double_function(x):
    return x * 2

numbers_list = [1, 2, 3, 4, 5]

res = apply_function_and_sum(numbers_list, double_function)
print(f'Sum of the doubles of each element in the list: {res}')

# Task 2
# Напишіть декоратор, який зберігає результати обчислення функції у файл для подальшого використання.

import functools
import json

def cache_result(file_path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try: return json.load(open(file_path, 'r'))
            except (FileNotFoundError, json.JSONDecodeError):
                result = func(*args, **kwargs)
                with open(file_path, 'w') as file: json.dump(result, file)
                return result
        return wrapper
    return decorator

@cache_result('cached_result.json')
def square_function(x):
    print(f'Calculating square for {x}')
    return x ** 2

result1 = square_function(5)
print(f'Result of the first call: {result1}')

result2 = square_function(5)
print(f'Result of the second call: {result2}')

# Task 3
# Напишіть декоратор, який вимірює час виконання функції.

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'Execution time of function {func.__name__}: {elapsed_time:.4f} seconds')
        return result
    return wrapper

@measure_time
def some_function():
    time.sleep(2)

some_function()

# Task 4
# Напишіть декоратор, який обмежує кількість викликів функції.

import functools

def limit_calls(max_calls):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            wrapper.call_cache.setdefault(key, {'calls': 0, 'result': None})
            if wrapper.call_cache[key]['calls'] < max_calls:
                wrapper.call_cache[key]['calls'] += 1
                return func(*args, **kwargs)
            else:
                print(f'Maximum number of calls reached for the function {func.__name__} with arguments {key}')
                return wrapper.call_cache[key]['result']
        
        wrapper.call_cache = {}
        return wrapper
    return decorator

@limit_calls(3)
def some_function():
    print('Function call')

some_function()
some_function()
some_function()
some_function()

# Task 5
# Напишіть декоратор, який кешує результати обчислення функції і повертає їх з кешу при наступних викликах з тими самими аргументами.

from functools import wraps

def cache_results(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper

@cache_results
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# First call (calculates and caches the result)
res1 = fibonacci(10)
print(f'Result of the first call: {res1}')

# Second call (uses the cached result)
res2 = fibonacci(10)
print(f'Result of the second call (using cache): {res2}')