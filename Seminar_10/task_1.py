"""
Создайте класс окружность.
Класс должен принимать радиус окружности при создании экземпляра.
У класса должно быть два метода, возвращающие длину окружности и её площадь.
"""
from math import pi, sqrt


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def circum_ference(self):
        circum = 2 * pi * self.radius
        return circum

    def area(self):
        ar = pi * (self.radius ** 2)
        return ar

    @classmethod
    def radius_from_area(cls, area):
        return cls(sqrt(area / pi))


if __name__ == '__main__':
    circle_1 = Circle(10)
    print(circle_1.circum_ference())
    print(circle_1.area())
    c2 = Circle.radius_from_area(314)
    print(c2.radius)
