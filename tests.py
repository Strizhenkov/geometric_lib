import math
import unittest

import circle
import rectangle
import square
import triangle


class TestShapes(unittest.TestCase):
    def test_circle(self):
        self.assertEqual(25 * math.pi, circle.area(5))
        self.assertEqual(4 * math.pi, circle.perimeter(2))

    def test_rectangle(self):
        self.assertEqual(2, rectangle.area(1, 2))
        self.assertEqual(10, rectangle.perimeter(2, 3))

    def test_square(self):
        self.assertEqual(9, square.area(3))
        self.assertEqual(4, square.perimeter(1))

    def test_triangle(self):
        self.assertEqual(5, triangle.area(2, 5))
        self.assertEqual(6, triangle.perimeter(1, 2, 3))
