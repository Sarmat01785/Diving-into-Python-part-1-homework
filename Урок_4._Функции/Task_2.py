'''
Задача 2

Напишите функцию принимающую на вход только ключевые параметры 
и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление.
'''
def args_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            hash(value)
        except TypeError:
            value = str(value)
        result[value] = key
    return result

result_dict = args_to_dict(name="Alice", age=25, salary="10000")
print(result_dict)
