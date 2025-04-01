import unittest
from src.sorting.insertionsort import insertion_sort
from src.sample import nums, words


class TestInsertionSort(unittest.TestCase):

    def test_insertionsort(self):
        for n in nums:
            with self.subTest(list=n):
                n_copy = n.copy()
                n_sorted = sorted(n_copy)
                result = insertion_sort(n_copy)
                self.assertEqual(result, n_sorted)

    def test_insertionsort_strings(self):
        for n in words:
            with self.subTest(list=n):
                n_copy = n.copy()
                n_sorted = sorted(n_copy)
                result = insertion_sort(n_copy)
                self.assertEqual(result, n_sorted)


if __name__ == "__main__":
    unittest.main()
