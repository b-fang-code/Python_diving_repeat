'''
Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число.
Откажитесь от магических чисел
В коде должны быть один input и один print
'''

MIN_D = 0
MAX_D = 1000
ONE_DIGIT = 10
TWO_DIGIT = 100

result = 0
number_type = ''

while True:
    n = int(input('Введите число от 1 до 999: '))
    if MIN_D < n < MAX_D:
        if n // ONE_DIGIT == 0:
            number_type = 'Цифра'
            result = n ** 2
        elif n // TWO_DIGIT == 0:
            number_type = 'Двузначное число'
            result = n // ONE_DIGIT * n % ONE_DIGIT
        else:
            number_type = 'Трехзначное число'
            result = n % ONE_DIGIT * TWO_DIGIT + n // ONE_DIGIT % ONE_DIGIT * ONE_DIGIT + n // TWO_DIGIT
        break

print(number_type, result)
