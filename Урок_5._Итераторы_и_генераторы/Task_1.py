"""
Задача 1

Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

import os


def get_file_info(path):
    dir_path, filename = os.path.split(path)

    name, ext = os.path.splitext(filename)

    return dir_path, name, ext


print("\n")
print(get_file_info(r"C:\Users\Сармат\Documents\Обучение\Новый текстовый документ.txt"))
