"""
Обрабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр прямоугольника.
Складываем и вычитаем периметры, а не длину и ширину.
При вычитании не допускайте отрицательных значений.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
"""


class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width
        if width is None:
            self.width = length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def area_of_rectangle(self):
        return self.width * self.length

    def __add__(self, other):
        return f'Сумма периметров: {self.perimeter() + other.perimeter()}'

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            return f'Разность периметров: {other.perimeter() - self.perimeter()}'
        return f'Разность периметров: {self.perimeter() - other.perimeter()}'

    def __eq__(self, other):
        if self.area_of_rectangle() != other.area_of_rectangle():
            return 'Площади НЕ равны'
        return 'Площади равны'

    def __ge__(self, other):
        if self.area_of_rectangle() < other.area_of_rectangle():
            return 'Первый меньше второго'
        return 'Первый больше второго'


if __name__ == '__main__':
    rectangle_1 = Rectangle(2, 3)
    print(rectangle_1.perimeter())

    rectangle_2 = Rectangle(2, 6)
    print(rectangle_2.perimeter())

    rectangle_3 = rectangle_1.__add__(rectangle_2)
    print(rectangle_3)

    rectangle_4 = rectangle_1.__sub__(rectangle_2)
    print(rectangle_4)

    print(Rectangle.__eq__(rectangle_1, rectangle_2))
    print(Rectangle.__ge__(rectangle_1, rectangle_2))
