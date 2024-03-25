"""
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.
"""


class Range:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    @staticmethod
    def validate(value):
        if value <= 0:
            raise ValueError('Ошибка')


class Rectangle:
    length = Range()
    width = Range()

    def __init__(self, length, width=None):
        self.length = length
        self.width = width
        if width is None:
            self.width = length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def area_of_rectangle(self):
        return self.width * self.length


if __name__ == '__main__':
    r = Rectangle(1, 10)
    print(r.perimeter())
