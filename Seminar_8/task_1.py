"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""

import json


def get_json_file():
    with (
        open('union.txt', 'r', encoding='utf-8') as f1,
        open('union.json', 'w', encoding='utf-8') as f2,
    ):
        my_dict = {}
        for line in f1:
            name, value = line.strip().split('|')
            my_dict[name.title()] = value
        json.dump(my_dict, f2, indent=2)


if __name__ == '__main__':
    get_json_file()
