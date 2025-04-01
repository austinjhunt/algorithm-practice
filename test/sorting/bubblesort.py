import unittest
from src.sorting.bubblesort import bubble_sort
from src.sorting.sample import nums, words


class TestBubbleSort(unittest.TestCase):

    def test_bubblesort(self):
        for n in nums:
            with self.subTest(list=n):
                n_copy = n.copy()
                n_sorted = sorted(n_copy)
                result = bubble_sort(n_copy)
                self.assertEqual(result, n_sorted)

    def test_bubblesort_strings(self):
        for n in words:
            with self.subTest(list=n):
                n_copy = n.copy()
                n_sorted = sorted(n_copy)
                result = bubble_sort(n_copy)
                self.assertEqual(result, n_sorted)


if __name__ == "__main__":
    unittest.main()
