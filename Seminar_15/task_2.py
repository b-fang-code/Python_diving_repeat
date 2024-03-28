"""
На семинаре про декораторы был создан логирующий декоратор. Он сохранял аргументы функции и результат её работы в файл.
Напишите аналогичный декоратор, но внутри используйте модуль logging.
"""
import logging
from time import asctime
import os

if not os.path.exists('./logfiles'):
    os.mkdir('./logfiles')

logging.basicConfig(filename='./logfiles/log2.log',
                    level=logging.INFO,
                    encoding='utf-8',
                    filemode='a',
                    format='{levelname:<5}, asctime.now(), time:{asctime}, {msg}',
                    style='{')


def loggering(func):
    def wrapper(a, b, c):
        res = func(a, b, c)
        logging.info(f'Функция {func.__name__} была вызвана с аргументами {a, b, c} и результат выполнения {res}')
        return res

    return wrapper


@loggering
def discriminant(a, b, c):
    d = b ** 2 - 4 * a * c
    match d:
        case d if d < 0:
            result = None
        case d if d == 0:
            x1 = -b / (2 * a)
            result = x1
        case _:
            x1 = (-b + (d ** 0.5)) / (2 * a)
            x2 = (-b - (d ** 0.5)) / (2 * a)
            result = (x1, x2)
    return result


discriminant(5, 2, 1)
