"""
Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноименных
 pickle файлов.
"""

import json
import pickle
from pathlib import Path


def from_json_to_pickle(directory):
    directory = Path(directory)

    if not directory.is_dir():
        print(f'{directory} не является директорией! ')
        return
    json_files = list(directory.glob('*.json'))

    if not json_files:
        print(f'В директории {directory} не найдено JSON-файлов')
        return

    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        pickle_file = json_file.with_suffix('.pickle')
        with open(pickle_file, 'wb') as f:
            pickle.dump(data, f)
        print(f'Содержимое файла {json_file.name} успешно сохранено в {pickle_file.name}')


if __name__ == '__main__':
    my_directory = './'
    from_json_to_pickle(my_directory)
