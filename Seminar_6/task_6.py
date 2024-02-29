"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в виде строки вида DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищенную функцию.
"""


def check_leap_year(year):
    return not year % 4 != 0 or year % 100 == 0 and year % 400 != 0


def check_date(date):
    day, month, year = map(int, date.split('.'))
    if not 0 < day < 32 or not 0 < month < 13 or not 0 < year < 10000:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    leap = check_leap_year(year)
    if leap and month == 2 and day > 29:
        return False
    if not leap and month == 2 and day > 28:
        return False
    return True


if __name__ == '__main__':
    input_date = input('Введите дату в виде строки вида DD.MM.YYYY: ')
    print(check_date(input_date))
