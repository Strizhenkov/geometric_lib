import unittest

import circle
import rectangle
import square
import triangle


class TestShapes(unittest.TestCase):
    def testAreaCircle1(self):
        self.assertAlmostEqual(3.14, circle.area(1), delta=0.01)

    def testAreaCircle2(self):
        self.assertAlmostEqual(44.17, circle.area(3.75), delta=0.01)

    def testAreaCircle3(self):
        self.assertAlmostEqual(12.56, circle.area(-2), delta=0.01)

    def testAreaCircle4(self):
        with self.assertRaises(Exception):
            circle.area('abc')

    def testPerimeterCircle1(self):
        self.assertAlmostEqual(12.56, circle.perimeter(2), delta=0.01)

    def testPerimeterCircle2(self):
        self.assertAlmostEqual(47.12, circle.perimeter(7.5), delta=0.01)

    def testPerimeterCircle3(self):
        self.assertAlmostEqual(-6.28, circle.perimeter(-1), delta=0.01)

    def testPerimeterCircle4(self):
        with self.assertRaises(Exception):
            circle.perimeter(True)

    def testAreaRectangle1(self):
        self.assertEqual(10, rectangle.area(2, 5))

    def testAreaRectangle2(self):
        self.assertAlmostEqual(3.85, rectangle.area(1.1, 3.5), delta=0.01)

    def testAreaRectangle3(self):
        self.assertEqual(2, rectangle.area(-1, -2))

    def testAreaRectangle4(self):
        with self.assertRaises(Exception):
            rectangle.area(True, True)

    def testPerimeterRectangle1(self):
        with self.assertRaises(Exception):
            rectangle.perimeter('Abcd', 1)

    def testPerimeterRectangle2(self):
        self.assertEqual(6, rectangle.perimeter(1, 2))

    def testPerimeterRectangle3(self):
        self.assertEqual(-2, rectangle.perimeter(0, -1))

    def testPerimeterRectangle4(self):
        with self.assertRaises(Exception):
            rectangle.perimeter(-True, -False)

    def testAreaSquare1(self):
        self.assertEqual(1.234567654321, square.area(1.111111))

    def testAreaSquare2(self):
        self.assertEqual(25, square.area(5))

    def testAreaSquare3(self):
        self.assertEqual(9025000000, square.area(95000))

    def testAreaSquare4(self):
        with self.assertRaises(Exception):
            square.area('x')

    def testPerimeterSquare1(self):
        with self.assertRaises(Exception):
            square.perimeter('*')

    def testPerimeterSquare2(self):
        self.assertEqual(492, square.perimeter(123))

    def testPerimeterSquare3(self):
        self.assertEqual(2, square.perimeter(0.5))

    def testPerimeterSquare4(self):
        self.assertEqual(4, square.perimeter(1))

    def testAreaTriangle1(self):
        self.assertEqual(10, triangle.area(4, 5))

    def testAreaTriangle2(self):
        self.assertEqual(36, triangle.area(9, 8))

    def testAreaTriangle3(self):
        self.assertEqual(1.26, triangle.area(1.2, 2.1))

    def testAreaTriangle4(self):
        with self.assertRaises(Exception):
            triangle.area(False, 47)

    def testPerimeterTriangle1(self):
        self.assertEqual(6, triangle.perimeter(1, 2, 3))

    def testPerimeterTriangle2(self):
        self.assertEqual(2.4, triangle.perimeter(0.9, 0.5, 1))

    def testPerimeterTriangle3(self):
        with self.assertRaises(Exception):
            triangle.perimeter(True, False, False)

    def testPerimeterTriangle4(self):
        with self.assertRaises(Exception):
            triangle.perimeter(90, 1, 1)