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
    build_max_heap(a)  # array is now a max heap satisfying heap constraints
    n = len(a)

    # starting from last element,
    for i in range(n - 1, 0, -1):  #
        # swap the root of heap with last element. in other words,
        # move max to current position
        a[i], a[0] = a[0], a[i]
        # ignore newly placed max and reheapify what is left
        # this will move max of remaining to position 0
        heapify(a, 0, i)
    return a


def swap(i, j, a):
    a[i], a[j] = a[j], a[i]


def build_max_heap(a: list):
    """build a max heap from an input array."""
    n = len(a)
    # we know parent index of node with index i is i // 2 with 1 based indexing
    # last parent has to be n // 2 - 1, and we go all the way to first item index 0
    for i in range(n // 2 - 1, -1, -1):  # start at last parent index
        heapify(a, i, n)


def heapify(a: list, i: int, heap_size: int):
    # translate from 1-based indexing to 0 based index
    left = 2 * i + 1  # left = 2i with 1-based
    right = 2 * i + 2  # right = 2i+1 with 1-based
    largestIndex = i  # parent is i // 2 with 1-based.
    largestIndex = (
        left if left < heap_size and a[left] > a[largestIndex] else largestIndex
    )
    largestIndex = (
        right if right < heap_size and a[right] > a[largestIndex] else largestIndex
    )

    if largestIndex != i:
        swap(i, largestIndex, a)
        heapify(a, largestIndex, heap_size)


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
