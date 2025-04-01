import unittest
from src.sorting.quicksort import quicksort
from src.sample import nums, words


class TestSortingAlgorithms(unittest.TestCase):

    def test_quick_sort(self):
        for n in nums:
            with self.subTest(list=n):
                n_copy = n.copy()
                n_sorted = sorted(n_copy)
                low, high = 0, len(n_copy) - 1
                result = quicksort(n_copy, low, high)
                self.assertEqual(result, n_sorted)

    def test_quick_sort_strings(self):
        for n in words:
            with self.subTest(list=n):
                n_copy = n.copy()
                n_sorted = sorted(n_copy)
                low, high = 0, len(n_copy) - 1
                result = quicksort(n_copy, low, high)
                self.assertEqual(result, n_sorted)


if __name__ == "__main__":
    unittest.main()
