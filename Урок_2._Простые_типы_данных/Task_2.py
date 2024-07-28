"""
Задача 2
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions
"""

from fractions import Fraction


def calculate_fractions(frac1: str, frac2: str) -> tuple[Fraction, Fraction]:
    """
    Вычисляет сумму и произведение двух дробей, представленных в виде строк.

    Параметры:
    frac1 (str): Строка, представляющая первую дробь в формате 'a/b'.
    frac2 (str): Строка, представляющая вторую дробь в формате 'a/b'.

    Возвращает:
    tuple[Fraction, Fraction]: Кортеж из двух объектов Fraction, где первый элемент — это сумма дробей,
                               а второй элемент — произведение дробей.
    """
    # Преобразование строк в объекты Fraction
    fraction1 = Fraction(frac1)
    fraction2 = Fraction(frac2)

    # Сложение дробей
    sum_of_fractions = fraction1 + fraction2
    # Умножение дробей
    product_of_fractions = fraction1 * fraction2

    return sum_of_fractions, product_of_fractions


# Запрос ввода двух дробей от пользователя
frac1 = input("Введите первую дробь в формате 'a/b': ")
frac2 = input("Введите вторую дробь в формате 'a/b': ")

# Вычисление суммы и произведения дробей
sum_fraction, product_fraction = calculate_fractions(frac1, frac2)
print(f"Сумма дробей: {sum_fraction}")
print(f"Произведение дробей: {product_fraction}")
