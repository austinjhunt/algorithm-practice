from sorting.heapsort import test_heapsort
from sorting.mergesort import test_mergesort
from sorting.quicksort import test_quicksort
from sorting.bubblesort import test_bubblesort
from sorting.insertionsort import test_insertionsort
from sorting.sample import nums, words

test_lists = nums + words
test_quicksort(test_lists)
test_mergesort(test_lists)
test_bubblesort(test_lists)
test_insertionsort(test_lists)
test_heapsort(test_lists)
