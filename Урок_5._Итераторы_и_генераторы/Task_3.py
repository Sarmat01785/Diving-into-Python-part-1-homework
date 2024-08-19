"""
Задача 3

Создайте функцию генератор чисел Фибоначчи
"""


def fibonacci_generator(limit=None):
    a, b = 0, 1
    count = 0

    while limit is None or count < limit:
        yield a
        a, b = b, a + b
        count += 1


fib_gen = fibonacci_generator(limit=10)
print(list(fib_gen))
