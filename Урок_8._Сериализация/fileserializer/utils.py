import os


def get_directory_size(path):
    """Возвращает размер директории с учетом всех файлов."""
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            total += get_directory_size(entry.path)
    return total
