"""
Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
Например, отлавливаем ошибку деления на ноль.
"""

import logging
import os

if not os.path.exists('./logfiles'):
    os.mkdir('./logfiles')

logging.basicConfig(filename='./logfiles/log.log',
                    level=logging.ERROR,
                    encoding='utf-8',
                    filemode='a',
                    )

loger = logging.getLogger(__name__)


def divide_by_zero(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        logging.error('Нельзя делить на 0!')
        return float('inf') if x > 0 else float('-inf')


print(divide_by_zero(5, 0))
