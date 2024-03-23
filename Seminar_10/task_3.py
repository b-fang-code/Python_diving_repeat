"""
Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п.
 на ваш выбор.
Cвойство возраст должно быть недоступно для прямого обращения, но возможность получить текущий возраст должна
 присутствовать.
"""


class Person:

    def __init__(self, last_name, first_name, surname, age):
        self.__age = age
        self.surname = surname
        self.last_name = last_name
        self.first_name = first_name

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.surname


if __name__ == '__main__':
    p1 = Person('Васильев', 'Павел', 'Андреевич', 36)
    print(p1.full_name())
    p1.birthday()
    print(p1._Person__age)
