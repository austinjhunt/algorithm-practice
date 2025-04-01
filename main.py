from src.sorting import (
    test_bubblesort,
    test_heapsort,
    test_insertionsort,
    test_mergesort,
    test_quicksort,
    nums,
    words,
)

from src.searching import test_dfs, test_bfs, test_binarysearch

import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--sorting", action="store_true", default=False, help="test sorting algorithms"
)
parser.add_argument(
    "--searching", action="store_true", default=False, help="test search algorithms"
)
args = parser.parse_args()

if args.sorting:

    test_lists = nums + words
    test_quicksort(test_lists)
    test_mergesort(test_lists)
    test_bubblesort(test_lists)
    test_insertionsort(test_lists)
    test_heapsort(test_lists)

if args.searching:
    test_dfs()
    test_bfs()
    test_binarysearch()
