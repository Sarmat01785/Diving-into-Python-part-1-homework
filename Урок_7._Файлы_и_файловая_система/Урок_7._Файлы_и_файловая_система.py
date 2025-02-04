'''
Задача: 
Напишите функцию группового переименования файлов. Она должна:
a. Принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. Принимать параметр количество цифр в порядковом номере.
c. Принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. Принимать параметр расширение конечного файла.
e. Принимать диапазон сохраняемого оригинального имени.

Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
'''
import os
from pathlib import Path

def batch_rename_files(target_name, digits_count, source_ext, target_ext, name_range, directory='.'):
    """
    Переименовывает группу файлов в каталоге с заданными параметрами.
    
    :param target_name: Желаемое конечное имя файлов.
    :param digits_count: Количество цифр в порядковом номере.
    :param source_ext: Расширение исходного файла для переименования.
    :param target_ext: Расширение конечного файла.
    :param name_range: Диапазон сохраняемого оригинального имени.
    :param directory: Каталог, в котором находятся файлы для переименования.
    """
    # Получаем список файлов с заданным расширением
    files = Path(directory).glob(f'*.{source_ext}')
    
    # Переименовываем файлы
    for idx, file in enumerate(files, start=1):
        # Формируем новое имя файла
        original_part = file.stem[name_range[0]:name_range[1]]
        new_name = f"{original_part}{target_name}{str(idx).zfill(digits_count)}.{target_ext}"
        new_file_path = file.with_name(new_name)
        
        # Проверяем, что такого файла еще нет
        if not new_file_path.exists():
            # Переименовываем файл
            file.rename(new_file_path)
            print(f"Файл '{file.name}' переименован в '{new_name}'")
        else:
            print(f"Файл с именем '{new_name}' уже существует, переименование пропущено.")

# Пример использования функции
if __name__ == "__main__":
    batch_rename_files("newfile", 3, "txt", "txt", [0, 3], r"Укажите путь_к_вашей_директории")
