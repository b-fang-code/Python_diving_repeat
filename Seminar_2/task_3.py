'''
✔ Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.
'''

from math import pi
import decimal



while True:
    diameter = int(input('Введите диаметр окружности: '))
    if 0 < diameter <= 1000:
        print(f'Площадь круга: {decimal.Decimal(pi * ((diameter / 2) ** 2))} \nДлина окружности:'
              f'{decimal.Decimal(2 * pi * (diameter / 2))}')
        break
    else:
        print('Число превышает 1000')
        continue
