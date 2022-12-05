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

    def test_intersection(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).intersection(Rectangle(1, 1, 2, 2)), Rectangle(1, 1, 2, 2))
        with self.assertRaises(ValueError):
            Rectangle(0, 0, 1, 1).intersection(Rectangle(10, 10, 13, 13))

    def test_cover(self):
        self.assertEqual(Rectangle(0, 0, 1, 1).cover(Rectangle(1, 1, 5, 6)), Rectangle(0, 0, 5, 6))

    def test_make4(self):
        self.assertEqual(Rectangle(4, 4, 16, 16).make4(),
                         (Rectangle(4, 10, 10, 16),
                          Rectangle(10, 10, 16, 16),
                          Rectangle(10, 4, 16, 10),
                          Rectangle(4, 4, 10, 10)))


if __name__ == '__main__':
    unittest.main()