from random import randint


def func_(min_, max_, count_):
    rnd = randint(min_, max_)
    print(f'Угадайте число от 0 до 100 за {count_} попыток: ')
    for i in range(1, count_ + 1):
        my_num = int(input(f'Попытка {i}\n Введите число от {min_} до {max_}: '))
        if my_num < rnd:
            print('Больше!')
        elif my_num > rnd:
            print('Меньше!')
        else:
            print(f'Верно! заданное число {rnd} ')
            return True
    print(f'Попытки закончились. Было загадано число {rnd}')
    return False


# if __name__ == '__main__':
#     MIN, MAX, COUNT = 0, 100, 15
#     print(func_(MIN, MAX, COUNT))
