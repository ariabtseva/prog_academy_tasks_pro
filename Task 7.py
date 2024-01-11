# Task 3
# Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії.

def geometric_progression(a, r, n):
    current_term = a
    for x in range(n):
        yield current_term
        current_term *= r

print(list(geometric_progression(2, 3, 5)))

# Task 4
# Реалізуйте свій аналог генераторної функції range().

def range(start, stop, step=1):
    current = start
    while current < stop if step > 0 else current > stop:
        yield current
        current += step

for i in range(1, 10, 2):
    print(i)

# Task 5
# Напишіть генераторну функцію, яка повертатиме прості числа. Верхня межа діапазону повинна бути 
# задана параметром цієї функції.

def prime(n):
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i

for x in prime(20):
    print(x)

# Task 6
# Напишіть генераторний вираз для заповнення списку. Список повинен бути заповнений кубами чисел від 2 
# до вказаної вами величини.

n = 9
cubes_list = [x**3 for x in range(2, n + 1)]

print('List of cubes:', cubes_list)

# Task 7
# Реалізуйте генераторну функцію, яка повертатиме елементи послідовності чисел Фібоначчі.

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))

# Task 8
# Реалізуйте генераторну функцію для генерації послідовності дат. Початкова та кінцеві дати мають бути 
# задані параметрами цієї функції.

from datetime import timedelta, date

def dates(start, end):
    while start <= end:
        yield start
        start += timedelta(days=1)

start = date(2024, 1, 1)
end = date(2024, 1, 10)

date_sequence = list(dates(start, end))
print(f'Date sequence from {start} to {end}: {date_sequence}')