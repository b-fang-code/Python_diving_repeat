"""
Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
Верните дату в текущем году, соответствующую этому тексту. Логируйте ошибки, если текст не соответствует формату.
Логируйте объект именованного кортежа с атрибутами, соответствующими дате, если дата существует
"""

import datetime
import logging
import re
from collections import namedtuple

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Именованный кортеж для хранения даты
Date = namedtuple('Date', ['year', 'month', 'day'])


def parse_date(text):
    # Регулярное выражение для извлечения информации о дате
    pattern = r'(\d+)-([а-я]+)\s+([а-я]+)'

    # Поиск совпадений в тексте
    match = re.match(pattern, text, re.IGNORECASE)
    if match:
        try:
            # Извлечение информации о дне, месяце и порядковом номере
            day_number = int(match.group(1))
            month_name = match.group(2)
            weekday_name = match.group(3)

            # Получение текущей даты
            today = datetime.date.today()

            # Нахождение дня недели и месяца в тексте
            weekdays = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
            months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
                      'ноября', 'декабря']
            month_index = months.index(month_name) + 1
            weekday_index = weekdays.index(weekday_name)

            # Вычисление даты на этот год
            date = datetime.date(today.year, month_index, 1)
            while date.weekday() != weekday_index:
                date += datetime.timedelta(days=1)

            # Добавление порядкового номера дня
            date += datetime.timedelta(weeks=day_number - 1)

            # Логирование объекта даты
            date_obj = Date(date.year, date.month, date.day)
            logger.info(f"Объект даты: {date_obj}")

            return date
        except ValueError:
            logger.error("Ошибка при разборе текста")
            return None
    else:
        logger.error("Текст не соответствует формату")
        return None


# Пример использования
date_text = "1-й четверг ноября"
parsed_date = parse_date(date_text)
if parsed_date:
    print(f"Дата: {parsed_date}")
else:
    print("Ошибка при разборе текста")


