"""
Функция принимает на вход три списка одинаковой длины:
имена str,
ставка int,
премия str с указанием процентов вида «10.25%».
Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии.
"""

names = ['John', 'Mike', 'Evan']
bet = [11, 12, 13]
award = ['11.22%', '12.2%', '10.25%']


def calc_(names_, bet_, award_):
    dict_ = {n: s / 100 * float(b[:-1]) for n, s, b in zip(names_, bet_, award_)}
    return dict_


print(calc_(names, bet, award))
