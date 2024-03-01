"""
Напишите функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
Полученные имена сохраните в файл
"""
from random import randint, sample
import string
from re import findall

start = 4
end = 7


def fill_in_file(file_name, lines_num):
    count = 0
    with open(file_name, 'w', encoding='utf-8') as f:
        while count < lines_num:
            name = ''.join(sample(string.ascii_lowercase, randint(start, end)))
            if len(findall('[aeiouyAEIOUY]', name)) > 0:
                f.write(f"{''.join(name).capitalize()}\n")
                count += 1


if __name__ == '__main__':
    fill_in_file('names.txt', 5)
