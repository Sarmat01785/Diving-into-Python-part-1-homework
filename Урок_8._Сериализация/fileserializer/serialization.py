import json
import csv
import os
import pickle
from .utils import get_directory_size  # Импорт функции из utils.py

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
