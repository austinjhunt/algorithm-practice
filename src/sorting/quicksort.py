import logging


logger = logging.getLogger(__name__)


# Quick sort.
# Think: pivot.
# A pivot is one of the items in an array that meets 3 conditions after a sort:
# Correct position in final sorted array
# items to left are smaller
# items to right are bigger
# 1. Choose pivot (mid point item) and move it to end of array.
# 2. Pick low index = index of first item in array starting from left larger than pivot.
# 3. Pick high index = index of first item in array starting from right smaller than pivot.
# 4. Swap low & high.
# 5. Repeat from 2 until index of low is higher than index of high.
# 6. Swap low & pivot.
# 7. Recurse on each half of array.
# 8. Return fully sorted array by combining sorted halves.


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def partition(a: list, low: int = 0, high: int = 0):
    # Always pick first or last as pivot
    pivot = a[low]

    # leftwall indicates the right position of pivot SO FAR
    leftwall = low + 1
    for i in range(low + 1, high + 1):
        if a[i] < pivot:
            # a[i] is less than pivot so put in left partition
            logger.info(
                {
                    "action": "partition",
                    "pre_swap": a,
                    "swapping_indices": (i, leftwall),
                    "swapping_elems": (a[i], a[leftwall]),
                }
            )
            # swap the currently correct pivot with i
            swap(i, leftwall, a)

            # this leftwall position now more correct
            logger.info({"action": "partition", "post_swap": a})

            leftwall += 1
    # original pivot was at low; new correct pivot is indicated by current leftwall minus 1
    # because it was incremented a final time before a[i] became >= pivot
    swap(low, leftwall - 1, a)

    # return new correct pivot
    return leftwall - 1


def quicksort(a: list, low: int = 0, high: int = 0):
    logger.info({"action": "quicksort", "a": a, "low": low, "high": high})
    if low < high:
        pivot_index = partition(a, low, high)
        logger.info({"action": "quicksort", "pivot_index": pivot_index})
        quicksort(a, low, pivot_index - 1)
        quicksort(a, pivot_index + 1, high)
    return a


def test_quicksort(lists):
    logger.info({"action": "test_quicksort"})
    for n in lists:
        try:
            # create a copy of n since data is shared in sample.py
            n_copy = [el for el in n]
            logger.info({"action": "test_quicksort", "list": n_copy})
            n_sorted = sorted(n_copy)
            low, high = (0, len(n_copy) - 1)
            out = quicksort(n_copy, low, high)
            logger.info({"action": "test_quicksort", "list": n_copy, "output": out})
            assert out == n_sorted
            logger.info(
                {"action": "test_quicksort", "list": n_copy, "status": "success"}
            )
        except AssertionError:
            logger.error({"action": "test_quicksort", "list": n, "status": "fail"})
