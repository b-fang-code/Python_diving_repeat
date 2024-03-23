"""
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании экземпляра.
У класса должно быть два метода, возвращающие периметр и площадь.
Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
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


if __name__ == '__main__':
    rectangle_1 = Rectangle(2, 3)
    print(rectangle_1.perimeter())
    print(rectangle_1.area_of_rectangle())

    rectangle_2 = Rectangle(2)
    print(rectangle_2.perimeter())
    print(rectangle_2.area_of_rectangle())
