'''
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
'''

sum_ = 0
count_add = 0
count_out = 0
while True:
    if sum_ > 5000_000:
        sum_ -= sum_ * 0.1
        print('С Вас сняли налог на богатство!')
    action = input("Введите тип действия: ")
    if action == 'q':
        print(sum_)
        print('Выход из банкомата')
        break
    elif action == 'a':
        sum_add = int(input('Введите сумму пополнения: '))
        if sum_add % 50 == 0:
            sum_ += sum_add
            count_add += 1
            if count_add % 3 == 0:
                sum_ *= 1.03
        else:
            print('Сумма не кратна 50!')
    elif action == 'o':
        sum_out = int(input('Введите сумму снятия: '))
        commission = sum_ * 0.015
        if commission < 30:
            commission = 30
        elif commission > 600:
            commission = 600

        if sum_out + commission > sum_:
            print('Недостаточно средств!')
        else:
            if sum_out % 50 == 0:
                sum_ -= sum_out + commission
                count_out += 1
                if count_out % 3 == 0:
                    sum_ *= 1.03
            else:
                print('Сумма не кратна 50!')
    print(f'Баланс: {sum_}')


