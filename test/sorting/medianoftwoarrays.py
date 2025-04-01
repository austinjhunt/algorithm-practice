import unittest
from src.sorting.medianoftwoarrays import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums1 = [1, 3]
        nums2 = [2]
        expected = 2.0
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

    def test_example2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        expected = 2.5
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

    def test_empty_nums1(self):
        nums1 = []
        nums2 = [1, 2, 3]
        expected = 2.0
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

    def test_empty_nums2(self):
        nums1 = [1, 2, 3]
        nums2 = []
        expected = 2.0
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

    def test_both_empty(self):
        nums1 = []
        nums2 = []
        expected = None
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

    def test_same_elements(self):
        nums1 = [1, 1, 1]
        nums2 = [1, 1, 1]
        expected = 1.0
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

    def test_different_lengths(self):
        nums1 = [1, 5, 9]
        nums2 = [2, 3, 4, 6, 7]
        expected = 4.5
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

    def test_negative_numbers(self):
        nums1 = [-5, -3, -1]
        nums2 = [-10, -2, 0, 2]
        expected = -2.0
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

    def test_large_numbers(self):
        nums1 = [100000]
        nums2 = [100001]
        expected = 100000.5
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)


if __name__ == "__main__":
    unittest.main()
