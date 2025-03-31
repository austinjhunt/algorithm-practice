import logging

logger = logging.getLogger(__name__)


# Merge sort: Divide and conquer. Split array into equal halves until each one is 1 item, merge each pair back together in order.
# O(nlogn) worst case.
# While loop requires visiting n items.
# Logn comes from maximum height of binary tree we're creating with recursion.
def merge(arr1, arr2):
    # Merge two sorted arrays together
    out = []
    while len(arr1) > 0 and len(arr2) > 0:  # both have elems
        if arr1[0] < arr2[0]:
            out.append(arr1.pop(0))
        else:
            out.append(arr2.pop(0))
    # now either arr1 or arr2 is empty
    while len(arr1) > 0:
        out.append(arr1.pop(0))
    while len(arr2) > 0:
        out.append(arr2.pop(0))
    return out


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    half1, half2 = arr[: len(arr) // 2], arr[len(arr) // 2 :]
    half1 = merge_sort(half1)
    half2 = merge_sort(half2)
    return merge(half1, half2)


def test_mergesort(lists):
    logger.info({"action": "test_mergesort"})
    for n in lists:
        # create a copy of n since data is shared in sample.py
        try:
            n_copy = [el for el in n]
            logger.info({"action": "test_mergesort", "list": n_copy})
            n_sorted = sorted(n_copy)
            out = merge_sort(n_copy)
            logger.info({"action": "test_mergesort", "list": n_copy, "output": out})
            assert n_sorted == out
            logger.info(
                {"action": "test_mergesort", "list": n_copy, "status": "success"}
            )
        except AssertionError:
            logger.error({"action": "test_mergesort", "list": n, "status": "fail"})
