"""
Binary search implementation
"""

import random
import logging
from src.sorting.sample import nums as numeric_lists

logger = logging.getLogger(__name__)


def binarysearch(array, target, start, end):
    """return the index of the queried element if present in sorted input array, else -1"""
    logger.info(
        {
            "action": "binarysearch",
            "array": array,
            "target": target,
            "start": start,
            "end": end,
        }
    )
    if start > end:
        return -1
    middle = (start + end) // 2
    if target == array[middle]:
        logger.info({"status": "found target", "target": target, "index": middle})
        return middle
    if target < array[middle]:
        return binarysearch(array, target, start, middle - 1)
    if target > array[middle]:
        return binarysearch(array, target, middle + 1, end)


def test_binarysearch():
    for nums in numeric_lists:
        nums = sorted(nums)
        item_in_nums = random.choice(nums)

        # get item not in nums by incrementing from item_in_nums until not in array
        item_not_in_nums = item_in_nums
        while item_not_in_nums in nums:
            item_not_in_nums += 1

        logger.info({"msg": "checking positive search"})
        assert binarysearch(nums, target=item_in_nums, start=0, end=len(nums) - 1) > -1

        logger.info({"msg": "checking negative search"})
        assert (
            binarysearch(nums, target=item_not_in_nums, start=0, end=len(nums) - 1)
            == -1
        )


if __name__ == "__main__":
    test_binarysearch()
