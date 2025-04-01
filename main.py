from src.searching import test_dfs, test_bfs, test_binarysearch
import argparse
import unittest
import os
import sys


def run_tests(test_directory: str):
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=test_directory, pattern="*.py")
    runner = unittest.TextTestRunner()
    runner.run(suite)


parser = argparse.ArgumentParser()
parser.add_argument(
    "--sorting", action="store_true", default=False, help="test sorting algorithms"
)
parser.add_argument(
    "--searching", action="store_true", default=False, help="test search algorithms"
)
parser.add_argument(
    "--structures", action="store_true", default=False, help="test data structures"
)
args = parser.parse_args()
if args.sorting:
    run_tests(os.path.join(os.path.dirname(__file__), "test", "sorting"))
if args.searching:
    run_tests(os.path.join(os.path.dirname(__file__), "test", "searching"))
if args.structures:
    run_tests(os.path.join(os.path.dirname(__file__), "test", "structures"))
