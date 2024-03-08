"""
Прочитайте созданный в прошлом задании csv файл без использования 'csv.DictReader'.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции.
"""

import hashlib
import json
from pathlib import Path


def from_csv_to_json(csv_file_, json_file_):
    if not Path(csv_file_).exists():
        print(f'Файл {csv_file_} не найден ')
        return
    data = []
    with open(csv_file_, 'r', encoding='utf-8') as csvfile:
        lines = csvfile.readlines()

        for line in lines[1:]:  # Пропускаем заголовок
            access_level, user_id, name = line.strip().split(',')
            user_id = user_id.zfill(10)  # Дополняем id до 10 цифр незначащими нулями
            name = name.capitalize()  # Делаем первую букву имени прописной
            hash_value = hashlib.sha256((f'{name}{user_id}'.encode())).hexdigest()
            data.append({
                'access_level': access_level,
                'user_id': user_id,
                'name': name,
                'hash': hash_value
            })
    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=2)
    print(f'Данные успешно сохранены в файле {json_file_}')


if __name__ == '__main__':
    csv_file = 'task_3.csv'
    json_file = 'task_4.json'
    from_csv_to_json(csv_file, json_file)
