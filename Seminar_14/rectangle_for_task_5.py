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
