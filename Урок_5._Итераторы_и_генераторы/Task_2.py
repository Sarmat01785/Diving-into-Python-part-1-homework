"""
Задача 2

Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
Имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
Сумма рассчитывается как ставка умноженная на процент премии.
"""


def create_premium_dictionary(names, rates, premiums):
    return {
        name: rate * (float(premium.strip("%")) / 100)
        for name, rate, premium in zip(names, rates, premiums)
    }


names = ["Анна", "Борис", "Виктор"]
rates = [50000, 60000, 70000]
premiums = ["10.25%", "15.5%", "12%"]

print(create_premium_dictionary(names, rates, premiums))
