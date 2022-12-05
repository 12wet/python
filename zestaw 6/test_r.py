# Kod testujący moduł.

import unittest
from rectangles import Rectangle
from points import Point


class TestRectangle(unittest.TestCase):

    def test_str(self):
        self.assertEqual(str(Rectangle(1, 3, 3, 5)), '[(1, 3), (3, 5)]')

    def test_repr(self):
        self.assertEqual(repr(Rectangle(1, 3, 3, 5)), 'Rectangle(1, 3, 3, 5)')

    def test_eg(self):
        self.assertEqual(Rectangle(1, 3, 3, 5), Rectangle(1, 3, 3, 5))

    def test_ne(self):
        self.assertNotEqual(Rectangle(1, 3, 3, 5), Rectangle(-1, 3, 3, 5))


    def test_center(self):
        self.assertEqual(Rectangle(2, 4, 6, 8).center(), Point(4, 6))

    def test_area(self):
        self.assertEqual(Rectangle(1, 3, 3, 5).area(), 4)

    def test_move(self):
        rect = Rectangle(0, 0, 0, 6)
        rect.move(-4, -6)
        self.assertEqual(rect, Rectangle(-4, -6, -4, 0))


if __name__ == '__main__':
    unittest.main()