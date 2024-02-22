"""
Функция получает на вход строку из двух чисел через пробел.
Сформируйте словарь, где ключом будет
символ из Unicode, а значением — его порядковый номер из диапазона, границами которого являются введенные числа.
Границы диапазона учитывать.
"""

start, end = sorted(map(int, input('Введите два числа через пробел: ').split()))


def create_char_dir(st, en):
    dict_ = {}
    for i in range(st, en):
        dict_[chr(i)] = i
    return dict_


print(create_char_dir(start, end))
