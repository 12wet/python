import unittest
from polys import *

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]      # W(x) = x
        self.p2 = [0, 0, 1]   # W(x) = x^2
        self.p3 = [-3, 0, 1]  # W(x) = -3 + x^2
        self.p4 = [3] 
        self.p5 = [0]
        self.p6 = [0, 0, 0]

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])
        self.assertEqual(add_poly(self.p1, self.p5), self.p1)
        self.assertEqual(add_poly(self.p1, self.p3), [-3, 1, 1])

    def test_sub_poly(self): 
        self.assertEqual(sub_poly(self.p1, self.p2), [0, 1, -1])
        self.assertEqual(sub_poly(self.p1, self.p5), self.p1)
        self.assertEqual(sub_poly(self.p1, self.p3), [3, 1, -1])

    def test_mul_poly(self): 
        self.assertEqual(mul_poly(self.p1, self.p2), [0, 0, 0, 1])
        self.assertEqual(mul_poly(self.p1, self.p5), [])
        self.assertEqual(mul_poly(self.p1, self.p3), [0, -3, 0, 1])

    def test_is_zero(self): 
        self.assertFalse(is_zero(self.p1))
        self.assertTrue(is_zero(self.p5))
        self.assertFalse(is_zero(self.p3))

    def test_eq_poly(self): 
        self.assertFalse(eq_poly(self.p1, self.p2))
        self.assertTrue(eq_poly(self.p5, self.p6))
        self.assertTrue(eq_poly(self.p3, self.p3))

    def test_eval_poly(self): 
        self.assertEqual(eval_poly(self.p1, 2), 2)
        self.assertEqual(eval_poly(self.p3, 3), 6)
        self.assertEqual(eval_poly(self.p5, 8), 0)

    def test_combine_poly(self): 
        self.assertEqual(combine_poly(self.p1, self.p2), self.p2)
        self.assertEqual(combine_poly(self.p4, self.p5), [0])

    def test_pow_poly(self): 
        self.assertEqual(pow_poly(self.p1, 2), [0, 0, 1])
        self.assertEqual(pow_poly(self.p3, 2), [9, 0, -6, 0, 1])
        self.assertEqual(pow_poly(self.p5, 8), [])

    def test_diff_poly(self): 
        self.assertEqual(diff_poly(self.p1), [1])
        self.assertEqual(diff_poly(self.p3), [0, 2])
        self.assertEqual(diff_poly(self.p5), [])

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy