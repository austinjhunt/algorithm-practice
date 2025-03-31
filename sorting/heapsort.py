import logging

logger = logging.getLogger(__name__)

## Heap sort - O(nlogn)
## A heap is an ordered binary tree
## A max heap has restriction: parent nodes are greater than child nodes
## Utility funcs:
## build-max-heap: creates a max heap from unsorted array O(n)
## heapify: similar to build-max-heap but faster because we assume part of array is already sorted O(logn), but called n-1

# Algo: continuously do
# 1. Create max heap
# 2. Find and remove largest item from heap
# 3. Place item in sorted partition


# Begin by representing array as tree (unsorted binary tree)
def heapsort(a: list):
    build_max_heap(a)
    n = len(a)
    for i in range(n - 1, 0, -1):  # stops at 1
        a[i], a[0] = a[0], a[i]  # swap the root of heap with last element
        heapify(a, 0, i)  # heapify the root and the heap size is i
    return a


def swap(i, j, a):
    a[i], a[j] = a[j], a[i]


def build_max_heap(a: list):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):  # start at last parent index
        heapify(a, i, n)


def heapify(a: list, i: int, heap_size: int):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    largest = left if left < heap_size and a[left] > a[largest] else largest
    largest = right if right < heap_size and a[right] > a[largest] else largest

    if largest != i:
        swap(i, largest, a)
        heapify(a, largest, heap_size)


def test_heapsort(lists):
    logger.info({"action": "test_heapsort"})
    for n in lists:
        # create a copy of n since data is shared in sample.py
        try:
            n_copy = [el for el in n]
            logger.info({"action": "test_heapsort", "list": n_copy})
            n_sorted = sorted(n_copy)
            out = heapsort(n_copy)
            logger.info({"action": "test_heapsort", "list": n_copy, "output": out})
            assert n_sorted == out
            logger.info(
                {"action": "test_heapsort", "list": n_copy, "status": "success"}
            )
        except AssertionError:
            logger.error({"action": "test_heapsort", "list": n, "status": "fail"})
