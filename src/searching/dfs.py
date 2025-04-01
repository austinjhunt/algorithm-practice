"""
Depth-first search (DFS) implementation
"""

import random
import logging
from src.structures.graph import Graph, build_sample_graph

logger = logging.getLogger(__name__)


def dfs(graph: Graph, targetNode, currentNode=None, visited: set = None):
    """
    Depth-first search for a target node on a graph whose core representation is an adjacency list

    Byproduct result: visited set becomes a set of vertices in the starting node's connected component
    """
    if visited is None:
        visited = set()
    currentNode = graph.get_random_node() if currentNode is None else currentNode
    if currentNode not in visited:  # have not visited this node yet
        if currentNode == targetNode:
            logger.info(
                {
                    "action": "dfs",
                    "status": "found targetNode",
                    "visited": visited,
                    "visitedCount": len(visited),
                }
            )
            return True
        visited.add(currentNode)
        for node in graph.get_node_neighbors(currentNode):
            if dfs(graph, targetNode, currentNode=node, visited=visited):
                return True
    return False


def test_dfs():
    logger.info({"action": "test_dfs"})
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
    # assert dfs(graph, targetNode=node_in_graph)
    # assert not dfs(graph, targetNode=node_not_in_graph)
    # Workaround with sample graph.
    # Choose a target from the pool of nodes reachable from the random start node
    # Found by visiting / traversing first with DFS. Not practical, but good to illustrate.
    # Pick two nodes from the same connected component
    start_node = graph.get_random_node()
    connected_component = set()
    assert not dfs(
        graph,
        currentNode=start_node,
        targetNode="fake target to map out connected component",
        visited=connected_component,
    )  # Get all reachable nodes
    if connected_component:
        node_in_graph = random.choice(list(connected_component))
        logger.info({"start_node": start_node, "node_in_graph": node_in_graph})
        assert dfs(
            graph, currentNode=start_node, targetNode=node_in_graph
        )  # Now guaranteed to be reachable


if __name__ == "__main__":
    test_dfs()
