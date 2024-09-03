'''
Задача:
1. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
Результаты обхода сохраните в файлы json, csv и pickle.

○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

2. Соберите из созданных в рамках домашнего задания функций пакет для работы с файлами разных форматов.
'''
import os
import json
import csv
import pickle

def get_directory_size(path):
    """Возвращает размер директории с учетом всех файлов."""
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            total += get_directory_size(entry.path)
    return total

def serialize_directory(path, output_dir):
    """Сериализует информацию о директории в JSON, CSV и pickle форматы."""
    data = []

    for root, dirs, files in os.walk(path):
        for name in files:
            file_path = os.path.join(root, name)
            data.append({
                'parent_directory': root,
                'name': name,
                'type': 'file',
                'size': os.path.getsize(file_path)
            })
        for name in dirs:
            dir_path = os.path.join(root, name)
            data.append({
                'parent_directory': root,
                'name': name,
                'type': 'directory',
                'size': get_directory_size(dir_path)
            })

    # JSON
    with open(os.path.join(output_dir, 'directory_data.json'), 'w') as json_file:
        json.dump(data, json_file, indent=4)

    # CSV
    with open(os.path.join(output_dir, 'directory_data.csv'), 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['parent_directory', 'name', 'type', 'size'])
        writer.writeheader()
        for item in data:
            writer.writerow(item)

    # Pickle
    with open(os.path.join(output_dir, 'directory_data.pickle'), 'wb') as pickle_file:
        pickle.dump(data, pickle_file)

# serialize_directory(r'C:\Users\Сармат\Documents\Обучение\Погружение в Python. Часть 1 Домашняя работа', r'D:\Новая папка')
# serialize_directory(r'Укажите путь к вашей директории (input_dir)', r'Укажите путь к вашей директории (output_dir)')
path = input('Укажите путь к вашей директории (input_dir): ')
output_dir = input('Укажите путь к вашей директории (output_dir): ')
serialize_directory(path, output_dir)
