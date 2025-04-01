import logging

logger = logging.getLogger(__name__)

## Insertion sort
## Start at left, go to right.
## Examine each item, compare to item to its left.
## Insert item into correct position in array.
## Mark array elements traversed so far as fully sorted.


def insertion_sort_old(a: list):
    sorted_a = []
    for i in range(len(a)):
        insert(a[i], sorted_a)
    return sorted_a


def insert(v, a):
    logger.info({"action": "insert", "v": v, "a": a})
    if len(a) == 0:
        a.append(v)
    else:
        i = len(a) - 1
        while i >= 0 and v < a[i]:
            i -= 1
        a.insert(i + 1, v)
    logger.info(
        {
            "action": "insert",
            "insert_result": a,
            "v": v,
        }
    )


def insertion_sort(a: list):
    for i in range(len(a)):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            # swap
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
    return a


def test_insertionsort(lists):
    logger.info({"action": "test_insertionsort"})
    for n in lists:
        # create a copy of n since data is shared in sample.py
        try:
            n_copy = [el for el in n]
            logger.info({"action": "test_insertionsort", "list": n_copy})
            n_sorted = sorted(n_copy)
            out = insertion_sort(n_copy)
            logger.info({"action": "test_insertionsort", "list": n_copy, "output": out})
            assert n_sorted == out
            logger.info(
                {"action": "test_insertionsort", "list": n_copy, "status": "success"}
            )
        except AssertionError:
            logger.error({"action": "test_insertionsort", "list": n, "status": "fail"})
