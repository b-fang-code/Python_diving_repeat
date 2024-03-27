"""
На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также вычисляющую периметр, площадь
 и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса.
"""
import unittest
from rectangle_for_task_5 import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(3, 5)
        self.rectangle_2 = Rectangle(4, 6)

    def test_perimeter(self):
        self.assertEqual(Rectangle(3, 5).perimeter(), self.rectangle.perimeter())

    def test_area(self):
        self.assertEqual(Rectangle(3, 5).area_of_rectangle(), self.rectangle.area_of_rectangle())

    def test_sum(self):
        self.assertEqual(Rectangle(3, 5).__add__(Rectangle(4, 6)),
                         self.rectangle.__add__(self.rectangle_2))

    def test_dev(self):
        self.assertEqual(Rectangle(3, 5).__sub__(Rectangle(4, 6)),
                         self.rectangle.__sub__(self.rectangle_2))

    def test_eq(self):
        self.assertEqual(Rectangle(3, 5).__eq__(Rectangle(4, 6)),
                         self.rectangle.__eq__(self.rectangle_2))


if __name__ == '__main__':
    unittest.main(verbosity=2)
