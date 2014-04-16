import unittest
from bstree import BSTree, Node

class SimpleInsert(unittest.TestCase):
    """Testing simpliest cases"""

    def setUp(self):
        self.tree = BSTree()

    def test_key_equals_value(self):
        self.tree.insert("object")
        self.assertIs(self.tree.head.key, self.tree.head.payload)

    def test_no_items(self):
        self.assertIsNone(self.tree.head)

    def test_one_item_no_value(self):
        self.tree.insert(10)
        self.assertEqual(self.tree.search(10), 10)

    def test_one_item_key_and_value(self):
        self.tree.insert("ten", 10)
        self.assertEqual("ten", 10)

class IteratorInsert(unittest.TestCase):
    """Testing cases with lists, multiple arguments, and tuples as arguments
    to the class """


class Delete(unittest.TestCase):
    """Testing deletion cases"""
    def setUp(self):
        list_set = [10, 5, 20, -4, -3, 12, -20]
        self.tree = BSTree(*list_set)


class Lists(unittest.TestCase):
    """ Tests for printing the tree as a list """
    def setUp(self):
        self.list_set = [10, 5, 20, -4, -3, 12, -20]
        self.tree = BSTree(*self.list_set)

    def test_print_in_order(self):
        self.list_set.sort()
        self.assertEqual(self.tree.print_in_order(), self.list_set)



if __name__ == '__main__':
    unittest.main()
