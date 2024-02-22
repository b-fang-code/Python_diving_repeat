"""
Функция получает на вход список чисел и два индекса.
Вернуть сумму чисел между переданными индексами.
Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
Для простоты будем использовать только положительную индексацию
"""

lst = [12, 35, 25, 14, 86, 10, 8, 5]
ind_1, ind_2 = 3, 6


def index_plus(lst_, a, b):
    if a > b:
        a, b = b, a
    sum_num = sum(lst_[a:b + 1])
    return sum_num


print(index_plus(lst, ind_1, ind_2))
