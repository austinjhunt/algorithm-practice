import logging


logger = logging.getLogger(__name__)


def swap(index1, index2, array):
    array[index1], array[index2] = array[index2], array[index1]
    return array


# Bubble sort. Bubble one item at a time up to its correct position.
def bubble_sort(a):
    logger.info({"bubble_sort": a})
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):  # correct inner loop
            if a[j] > a[j + 1]:
                swap(j, j + 1, a)
    return a


def test_bubblesort(lists):
    logger.info({"action": "test_bubblesort"})
    for n in lists:
        # create a copy of n since data is shared in sample.py
        try:
            n_copy = [el for el in n]
            logger.info({"action": "test_bubblesort", "list": n_copy})
            n_sorted = sorted(n_copy)
            out = bubble_sort(n_copy)
            logger.info({"action": "test_bubblesort", "list": n_copy, "output": out})
            assert n_sorted == out
            logger.info(
                {"action": "test_bubblesort", "list": n_copy, "status": "success"}
            )
        except AssertionError:
            logger.error({"action": "test_bubblesort", "list": n, "status": "fail"})
