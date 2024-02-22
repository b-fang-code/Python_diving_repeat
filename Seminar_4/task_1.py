"""
Напишите функцию, которая принимает строку текста.
Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""

text = input('Введите текст: ').replace(' ', '')
print(text)


def code_(str_: str):
    lst = []
    for i in str_:
        lst.append(ord(i))
    lst_2 = sorted(lst, reverse=True)
    return lst_2


print(code_(text))
