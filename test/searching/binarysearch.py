import unittest
import random
from src.searching.binary import binarysearch
from src.sorting.sample import nums as numeric_lists


class TestBinarySearch(unittest.TestCase):

    def test_binarysearch_found(self):
        """Test case where the target is found in the list."""
        nums = sorted(
            random.choice(numeric_lists)
        )  # Pick a random sorted list from numeric_lists
        target = random.choice(nums)  # Random target from the list
        result = binarysearch(nums, target=target, start=0, end=len(nums) - 1)
        self.assertGreater(result, -1, f"Target {target} should be found in the list.")

    def test_binarysearch_not_found(self):
        """Test case where the target is not found in the list."""
        nums = sorted(
            random.choice(numeric_lists)
        )  # Pick a random sorted list from numeric_lists
        target = max(nums) + 1  # Ensure the target is not in the list
        result = binarysearch(nums, target=target, start=0, end=len(nums) - 1)
        self.assertEqual(
            result, -1, f"Target {target} should not be found in the list."
        )

    def test_binarysearch_empty_list(self):
        """Test case with an empty list."""
        nums = []
        target = 5  # Arbitrary target
        result = binarysearch(nums, target=target, start=0, end=len(nums) - 1)
        self.assertEqual(
            result, -1, "Binary search should return -1 for an empty list."
        )

    def test_binarysearch_single_element_found(self):
        """Test case where the list has a single element, and the target is that element."""
        nums = [5]
        target = 5
        result = binarysearch(nums, target=target, start=0, end=len(nums) - 1)
        self.assertEqual(result, 0, f"Target {target} should be found at index 0.")

    def test_binarysearch_single_element_not_found(self):
        """Test case where the list has a single element, and the target is different."""
        nums = [5]
        target = 10
        result = binarysearch(nums, target=target, start=0, end=len(nums) - 1)
        self.assertEqual(
            result, -1, f"Target {target} should not be found in the list."
        )

    def test_binarysearch_large_list(self):
        """Test case with a large sorted list."""
        nums = sorted(
            random.sample(range(0, 100000), 100000)
        )  # Generate a large sorted list
        target = random.choice(nums)  # Random target in the list
        result = binarysearch(nums, target=target, start=0, end=len(nums) - 1)
        self.assertGreater(result, -1, f"Target {target} should be found in the list.")


if __name__ == "__main__":
    unittest.main()
