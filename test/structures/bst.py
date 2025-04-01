from src.structures.bst import BinarySearchTree
import unittest


class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        for key in [50, 30, 70, 20, 40, 60, 80]:
            self.bst.insert(key)

    def test_insert_search(self):
        self.assertIsNotNone(self.bst.search(50))
        self.assertIsNotNone(self.bst.search(30))
        self.assertIsNone(self.bst.search(100))

    def test_delete(self):
        self.bst.delete(50)
        self.assertIsNone(self.bst.search(50))

    def test_inorder_traversal(self):
        self.assertEqual(self.bst.inorder(), [20, 30, 40, 50, 60, 70, 80])
