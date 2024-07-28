"""
Задача 1
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата.
"""

def int_to_base(n: int, base: int) -> str:
    """Преобразует целое число в строковое представление в заданной системе счисления."""
    if n == 0:
        return "0"

    digits = "0123456789ABCDEF"
    res = ""
    while n > 0:
        res = digits[n % base] + res
        n //= base

    return res


def convert_number(num: int) -> tuple[str, str, str, str]:
    """
    Преобразует число num в двоичное, восьмеричное, строковое и шестнадцатеричное представление.
    :param num: Целое число, которое нужно преобразовать.
    :return: Кортеж с четырьмя строками: двоичным, восьмеричным, строковым и шестнадцатеричным представлением числа.
    """
    binary = int_to_base(num, 2)
    octal = int_to_base(num, 8)
    string = str(num)
    hexadecimal = int_to_base(num, 16)
    return binary, octal, string, hexadecimal


num = int(input("Введите целое число: "))
binary, octal, string, hexadecimal = convert_number(num)
print("Двоичное представление:", binary)
print("Восьмеричное представление:", octal)
print("Строковое представление:", string)
print("Шестнадцатеричное представление:", hexadecimal)

# Проверка результата с использованием встроенных функций bin, oct и hex
print("Проверка:")
print("Двоичное представление (bin):", bin(num)[2:])
print("Восьмеричное представление (oct):", oct(num)[2:])
print("Шестнадцатеричное представление (hex):", hex(num)[2:].upper())
