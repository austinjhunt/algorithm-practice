"""
Breadth-first search (BFS) implementation
"""

import random
import logging
from collections import deque
from src.structures.graph import Graph, build_sample_graph

logger = logging.getLogger(__name__)


def get_connected_component_vertices_bfs(graph: Graph, start_node: any) -> list:
    """Use breadth first traversal to build a list of
    vertices in the start_node's connected component"""
    q = deque([start_node])
    visited = set()
    while q:
        node = q.popleft()
        if node not in visited:
            visited.add(node)
            q.extend(graph.get_node_neighbors(node))
    return visited


def bfs(graph: Graph, targetNode, startNode=None):
    """
    Breadth-first search for a target node on a graph whose core representation is an adjacency list
    using collections.dequeue
    """
    startNode = graph.get_random_node() if not startNode else startNode
    visited = set()
    q = deque([startNode])
    while q:
        node = q.popleft()
        logger.info(
            {
                "action": "bfs",
                "comparing": {"currentNode": node, "targetNode": targetNode},
            }
        )
        if node == targetNode:
            logger.info(
                {"action": "bfs", "status": "found", "visitCount": len(visited)}
            )
            return True
        if node not in visited:
            logger.info(
                {
                    "action": "bfs_customqueue",
                    "visiting": node,
                    "msg": "visiting node and enqueuing all neighbors",
                }
            )
            visited.add(node)
            q.extend(graph.get_node_neighbors(node))
    return False


def test_bfs():
    logger.info({"action": "test_bfs"})
    graph = build_sample_graph(edges=4, vertices=5)
    logger.info(f"GRAPH:\n{graph}")
    # test a positive and a negative case
    # node_in_graph = graph.get_random_node()
    # node_not_in_graph = str(uuid.uuid4())
    # Fun fact: these assertions MAY fail when sample graph
    # created consists of multiple disconnected components.
    # if you pick a random start node in one connected component A that is
    # disconnected from another connected component B where B contains the targetNode, targetNode
    # will not be found / is not reachable.
    # assert bfs(graph, targetNode=node_in_graph)
    # assert not bfs(graph, targetNode=node_not_in_graph)
    # Workaround with sample graph.
    # Choose a target from the pool of nodes reachable from the random start node
    # Found by visiting / traversing first with DFS. Not practical, but good to illustrate.
    # Pick two nodes from the same connected component
    start_node = graph.get_random_node()
    connected_component = get_connected_component_vertices_bfs(graph, start_node)
    if connected_component:
        node_in_graph = random.choice(list(connected_component))
        logger.info({"start_node": start_node, "node_in_graph": node_in_graph})
        assert bfs(graph, targetNode=node_in_graph)  # Now guaranteed to be reachable


if __name__ == "__main__":
    test_bfs()
