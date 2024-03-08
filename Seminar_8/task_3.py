"""
Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
"""

import json
import csv
from pathlib import Path


def convert_to_csv():
    if Path('task_2.json').exists():
        with open('task_2.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    else:
        print('Файл task_2.json не найден!')
        return

    with open('task_3.csv', 'w', newline='', encoding='utf-8') as csv_file:
        field_names = ['access_level', 'user_id', 'name']
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()

        for access_level, users in data.items():
            for user_id, name in users.items():
                writer.writerow({
                    'access_level': access_level,
                    'user_id': user_id,
                    'name': name,
                })
    print('Данные успешно сохранены в файл task_3.csv')


if __name__ == '__main__':
    convert_to_csv()
