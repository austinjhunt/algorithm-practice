import unittest
from src.structures.hashtable import HashTable


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable(size=8)
        self.ht.insert("apple", 100)
        self.ht.insert("banana", 200)
        self.ht.insert("cherry", 300)

    def test_insert_and_get(self):
        self.ht.insert("date", 400)
        self.assertEqual(self.ht.get("date"), 400)
        self.assertEqual(self.ht.get("apple"), 100)
        self.assertIsNone(self.ht.get("nonexistent"))

    def test_overwrite_value(self):
        self.ht.insert("banana", 250)
        self.assertEqual(self.ht.get("banana"), 250)

    def test_delete(self):
        self.ht.delete("cherry")
        self.assertIsNone(self.ht.get("cherry"))
        self.ht.delete("nonexistent")  # Should not cause errors

    def test_resize(self):
        for i in range(20):
            self.ht.insert(f"key{i}", i)
        self.assertGreater(self.ht.size, 8)  # Ensure resizing happened
