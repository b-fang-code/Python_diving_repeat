"""
Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные, верните истину,
 а если хотя бы одна убыточная — ложь.
"""


def is_profit(dict_):
    return all(sum(v) >= 0 for v in dict_.values())


my_dict = {
    'Azimuth': [100, -200, 500, -300, 400],
    'Boutique': [600, -500, 300, -100, 200],
    'Voyage': [400, -300, 600, -200, -400],
}

print(is_profit(my_dict))
