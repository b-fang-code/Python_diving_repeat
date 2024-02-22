"""
Функция получает на вход список чисел.
Отсортируйте список по убыванию суммы цифр
"""

data = list(map(int, input('Введите числа через пробел: ').split()))


def sort_list(num):
    sum_ = 0
    while num > 0:
        sum_ += num % 10
        num //= 10
    return sum_


print(sorted(data, key=sort_list, reverse=True))
