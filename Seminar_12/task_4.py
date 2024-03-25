"""
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
Используйте декораторы свойств.
Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__.
"""


class Rectangle:
    __slots__ = ('_length', '_width')

    def __init__(self, length, width=None):
        self._length = length
        self._width = width
        if width is None:
            self._width = length

    def perimeter(self):
        return 2 * (self._width + self._length)

    def area_of_rectangle(self):
        return self._width * self._length

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @length.setter
    def length(self, length):
        if length > 0:
            self._length = length
        else:
            raise ValueError('Отрицательное число')

    @width.setter
    def width(self, width):
        if width > 0:
            self._width = width
        else:
            raise ValueError('Отрицательное число')


if __name__ == '__main__':
    rectangle = Rectangle(3, 5)
    print(rectangle.area_of_rectangle())