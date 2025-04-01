import logging


logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)


from .dfs import test_dfs
from .bfs import test_bfs
from .binary import test_binarysearch
