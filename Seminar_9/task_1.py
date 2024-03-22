"""
Создайте функцию-замыкание, которая принимает два целых числа:
от 1 до 100 для загадывания,
от 1 до 10 для количества попыток.
Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
"""


def numb(num, count):
    def wrapper():
        for i in range(1, count + 1):
            u_res = int(input('Проверим: '))
            if u_res == num:
                return 'ok'
            elif u_res > num:
                print('Число больше ')
            else:
                print('Число меньше')
        return 'no'

    return wrapper


result = numb(23, 6)
print(result())