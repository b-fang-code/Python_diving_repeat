"""
Продолжаем развивать задачу 2.
Возьмите словарь, который вы получили.
Сохраните его итератор.
Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
"""

str_ = input('Введите строку: ')
my_dict = {i: ord(i) for i in set(str_)}
my_iter = iter(my_dict.items())
for _ in range(5):
    print(next(my_iter))

