# Kod testujący moduł.

import unittest


from points import Point

class TestPoint(unittest.TestCase): 

    def test_str(self):
         self.assertEqual(str(Point(7, 4)), "(7, 4)")

    def test_repr(self):
         self.assertEqual(repr(Point(0, 5)), "Point(0, 5)")

    def test_eq(self):
        self.assertEqual(Point(3, 3), Point(3, 3))

    def test_ne(self):
        self.assertNotEqual(Point(-1, -1), Point(-1, 1))

    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(1, 7), Point(2, 9))

    def test_sub(self):
        self.assertEqual(Point(1, 2) - Point(1, 7), Point(0, -5))

    def test_mul(self):
        self.assertEqual(Point(2, 1) * Point(2, 2), 6)

    def test_cross(self):
        self.assertEqual(Point(2, 1).cross(Point(2, 2)), 2)

    def test_length(self):
        self.assertEqual(Point(4, 3).length(), 5)

    def test_hash(self):
        self.assertEqual(hash(Point(0, 0)), -8458139203682520985)


if __name__ == '__main__':
    unittest.main()