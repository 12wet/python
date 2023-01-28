import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack(size = 20)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1234)
        self.assertFalse(self.stack.is_empty())

    def test_is_full(self):
        self.assertFalse(self.stack.is_full())
        for i in range(20):
            self.stack.push(i)
        self.assertTrue(self.stack.is_full())

    def test_push(self):
        self.stack.push(10)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.pop(), 10)

    def test_pop(self):
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertTrue(self.stack.is_empty())

    def test_push_exception(self):
        for i in range(20):
            self.stack.push(i)
        with self.assertRaises(ValueError):
            self.stack.push(11)

    def test_pop_exception(self):
        with self.assertRaises(ValueError):
            self.stack.pop()