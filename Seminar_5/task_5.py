"""
Напишите программу, которая выводит
на экран числа от 1 до 100.
При этом вместо чисел, кратных трем,
программа должна выводить слово «Fizz»
Вместо чисел, кратных пяти — слово «Buzz».
Если число кратно и 3, и 5, то программа
должна выводить слово «FizzBuzz».
*Превратите решение в генераторное выражение, лучше многострочное (почему?)
"""

print(*('FizzBuzz' if num % 15 == 0 else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else num for num in
        range(1, 100)))


def gen():
    for i in range(1, 100):
        if i % 15 == 0:
            yield 'FizzBuzz'
        elif i % 5 == 0:
            yield 'Buzz'
        elif i % 3 == 0:
            yield 'Fizz'
        else:
            yield i


print(*(gen()))
