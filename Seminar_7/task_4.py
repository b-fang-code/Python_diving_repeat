"""
Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона.
"""
import os
import string
from random import choices, randint


def gen_files(ext, min_name_len=6, max_len_name=30, count=2):
    folder_name = 'Files'
    os.mkdir(folder_name)
    for i in range(count):
        file_name = ''.join(choices(string.ascii_lowercase, k=randint(min_name_len, max_len_name)))
        with open(f'{folder_name}/{file_name}.{ext}', 'wb') as f:
            f.write(os.urandom(randint(min_name_len, max_len_name)))


if __name__ == '__main__':
    gen_files('bin', min_name_len=6, max_len_name=30, count=2)