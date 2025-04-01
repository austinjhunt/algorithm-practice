import unittest
from src.sorting.heapsort_custom import heapsort
from src.sorting.heapsort_heapq import heapsort_maxheap_heapq, heapsort_minheap_heapq
from src.sample import nums, words


class TestHeapSort(unittest.TestCase):

    def test_heapsort(self):
        for n in nums:
            with self.subTest(list=n):
                n_copy = n.copy()
                n_sorted = sorted(n_copy)
                result = heapsort(n_copy)
                self.assertEqual(result, n_sorted)

    def test_heapsort_strings(self):
        for n in words:
            with self.subTest(list=n):
                n_copy = n.copy()
                n_sorted = sorted(n_copy)
                result = heapsort(n_copy)
                self.assertEqual(result, n_sorted)

    def test_heapsort_maxheap_heapq(self):
        for n in nums:
            with self.subTest(list=n):
                n_copy = n.copy()
                n_sorted = sorted(n_copy)
                result = heapsort_maxheap_heapq(n_copy)
                self.assertEqual(result, n_sorted)

    def test_heapsort_minheap_heapq(self):
        for n in nums:
            with self.subTest(list=n):
                n_copy = n.copy()
                n_sorted = sorted(n_copy)
                result = heapsort_minheap_heapq(n_copy)
                self.assertEqual(result, n_sorted)

    def test_heapsort_minheap_heapq(self):
        for n in words:
            with self.subTest(list=n):
                n_copy = n.copy()
                n_sorted = sorted(n_copy)
                result = heapsort_minheap_heapq(n_copy)
                self.assertEqual(result, n_sorted)


if __name__ == "__main__":
    unittest.main()
