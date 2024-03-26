"""
Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое
 или вещественное число.
Обрабатывайте не числовые данные как исключения.
"""


def check_input(text):
    while True:
        try:
            num = float(input(text))
        except ValueError as e:
            print(f'Ошибка типа данных: {e}')
        else:
            return int(num) if num.is_integer() else num


number = check_input('Введите целое или вещественное число: ')
print(f'{number} тип {type(number).__name__}')
