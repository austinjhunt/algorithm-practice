import heapq


def heapsort_minheap_heapq(iterable):
    """
    Sorts an iterable using HeapSort with heapq which treats heap as min heap by default.
    :param iterable: A list of elements to be sorted.
    :return: A sorted list in ascending order.
    """
    heap = []

    # Push all elements onto the heap
    for value in iterable:
        heapq.heappush(heap, value)

    # Extract elements in sorted order
    return [heapq.heappop(heap) for _ in range(len(heap))]


def heapsort_maxheap_heapq(iterable):
    """
    Implements HeapSort by first building a max heap and then extracting the max iteratively.
    :param iterable: A list of elements to be sorted.
    :return: A sorted list in ascending order.
    """
    n = len(iterable)

    # THIS WILL NOT WORK FOR STRINGS!!!

    # Convert list to a max heap (negate values to use min-heap as max-heap)
    max_heap = [-val for val in iterable]
    heapq.heapify(max_heap)

    # Extract elements and restore max-heap property
    sorted_list = []
    for i in range(n):
        sorted_list.insert(0, -heapq.heappop(max_heap))

    return sorted_list


# Example usage
if __name__ == "__main__":
    numbers = [5, 3, 8, 1, 2, 7]
    sorted_numbers = heapsort_minheap_heapq(numbers)
    print("Sorted List:", sorted_numbers)

    numbers = [5, 3, 8, 1, 2, 7]
    sorted_numbers = heapsort_maxheap_heapq(numbers)
    print("Sorted List:", sorted_numbers)
