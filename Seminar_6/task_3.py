"""
Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными верными вариантами отгадок и количество попыток на угадывание.
Функция возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
"""


def quest(qst: str, answs: list, tr: int):
    print(qst)
    count = 1
    while tr > 0:
        tr -= 1
        my_answ_ = input('Ваш ответ: ')
        if my_answ_ in answs:
            return f'Вы угадали за {count} попыток'
        else:
            print(f'Неверно! Осталось попыток {tr}')
            count += 1
    return 0


if __name__ == '__main__':
    question = 'Зимой и летом одним цветом'
    answers = ['Ель', 'Елка', 'ель', 'елка']
    tries = 10
    print(quest(question, answers, tries))
