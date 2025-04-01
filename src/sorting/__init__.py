import logging


logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)


from .heapsort import test_heapsort
from .mergesort import test_mergesort
from .quicksort import test_quicksort
from .bubblesort import test_bubblesort
from .insertionsort import test_insertionsort
from .sample import nums, words
