"""
Задача 2
Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""
# Вариант 1

num = int(input("Введите число от 1 до 100_000: "))

if num <= 0 or num > 100_000:
    print("Число вне допустимого диапазона")

elif num == 1:
    print("Число 1 не является ни простым ни составным")

else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"Число {num} является простым")
    else:
        print(f"Число {num} является составным")



# Вариант 2
def is_prime(number):
    """
    Это docstring функции, описывающий ее поведение, аргументы и возвращаемое значение.
    Функция is_prime проверяет, является ли число простым. Число считается простым, если
    оно больше 1 и не имеет делителей, кроме 1 и самого себя.
    """
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

try:
    number = int(input("Введите число в диапазоне от 1 до 100000: "))
    if number == 1:
        print("1 не является ни простым, ни составным числом.")
    elif number <= 0 or number > 100000:
        print("Число вне допустимого диапазона.")
    elif is_prime(number):
        print(f"Число {number} является простым.")
    else:
        print(f"Число {number} является составным.")
except ValueError:
    print("Введены некорректные данные. Необходимо ввести целое число.")












