import unittest
from singlelist import *
from node import *


class TestSingleList(unittest.TestCase):
    def test_insert_head(self):
        lista = SingleList()
        lista.insert_head(Node(12))
        lista.insert_head(Node(46))
        lista.insert_head(Node(90))

        self.assertEqual(lista.head.value, 90)
        self.assertEqual(lista.head.nextNode.value, 46)
        self.assertEqual(lista.head.nextNode.nextNode.value, 12)
        self.assertEqual(lista.tail.value, 12)
        self.assertEqual(lista.tail.nextNode, None)
        self.assertEqual(lista.length, 3)

    def test_insert_tail(self):
        lista = SingleList()
        lista.insert_tail(Node(12))
        lista.insert_tail(Node(46))
        lista.insert_tail(Node(90))

        self.assertEqual(lista.head.value, 12)
        self.assertEqual(lista.head.nextNode.value, 46)
        self.assertEqual(lista.head.nextNode.nextNode.value, 90)
        self.assertEqual(lista.tail.value, 90)
        self.assertEqual(lista.tail.nextNode, None)
        self.assertEqual(lista.length, 3)

    def test_remove_head(self):
        lista = SingleList()
        lista.insert_head(Node(12))
        lista.insert_head(Node(46))
        lista.insert_head(Node(90))

        self.assertEqual(lista.remove_head().value, 90)
        self.assertEqual(lista.length, 2)
        self.assertEqual(lista.remove_head().value, 46)
        self.assertEqual(lista.length, 1)
        self.assertEqual(lista.remove_head().value, 12)
        self.assertEqual(lista.head, None)
        self.assertEqual(lista.tail, None)
        self.assertEqual(lista.length, 0)
        with self.assertRaises(ValueError):
            lista.remove_head()

    def test_remove_tail(self):
        lista = SingleList()
        lista.insert_head(Node(12))
        lista.insert_head(Node(46))
        lista.insert_head(Node(90))

        self.assertEqual(lista.remove_tail().value, 12)
        self.assertEqual(lista.length, 2)
        self.assertEqual(lista.remove_tail().value, 46)
        self.assertEqual(lista.length, 1)
        self.assertEqual(lista.remove_tail().value, 90)
        self.assertEqual(lista.head, None)
        self.assertEqual(lista.tail, None)
        self.assertEqual(lista.length, 0)
        with self.assertRaises(ValueError):
            lista.remove_tail()

    def test_join(self):
        lista12 = SingleList()
        lista12.insert_head(Node(12))
        lista12.insert_head(Node(46))
        lista12.insert_head(Node(90))

        lista46 = SingleList()
        lista46.insert_head(Node(9))
        lista46.insert_head(Node(123))
        lista46.insert_head(Node(1))

        lista12.join(lista46)

        self.assertEqual(lista12.head.value, 90)
        self.assertEqual(lista12.head.nextNode.value, 46)
        self.assertEqual(lista12.head.nextNode.nextNode.value, 12)
        self.assertEqual(lista12.tail.value, 9)
        self.assertEqual(lista12.tail.nextNode, None)
        self.assertEqual(lista12.length, 6)
        self.assertEqual(lista46.head, None)
        self.assertEqual(lista46.tail, None)
        self.assertEqual(lista46.length, 0)