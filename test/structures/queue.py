import unittest
from src.structures.queue import Queue
from src.structures.node import QueueNode


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.add(QueueNode("first"))
        self.assertFalse(self.queue.is_empty())

    def test_add(self):
        node1 = QueueNode("first")
        node2 = QueueNode("second")
        self.queue.add(node1)
        self.queue.add(node2)
        self.assertEqual(self.queue.head, node1)
        self.assertEqual(self.queue.tail, node2)

    def test_pop(self):
        node1 = QueueNode("first")
        node2 = QueueNode("second")
        self.queue.add(node1)
        self.queue.add(node2)
        popped = self.queue.pop()
        self.assertEqual(popped, node1)
        self.assertEqual(self.queue.head, node2)
        self.assertFalse(self.queue.is_empty())
        self.queue.pop()
        self.assertTrue(self.queue.is_empty())
