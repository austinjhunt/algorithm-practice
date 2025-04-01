import unittest
import random
from src.searching.dfs import dfs
from src.structures.graph import Graph


class TestDFS(unittest.TestCase):

    def setUp(self):
        # Mock the Graph class
        self.graph = Graph()
        self.graph.add_edge(("A", "B"))
        self.graph.add_edge(("A", "C"))
        self.graph.add_edge(("B", "C"))
        self.graph.add_edge(("B", "D"))

    def test_dfs_found(self):
        """Test case where the target is found in the graph."""
        result = dfs(self.graph, targetNode="D", currentNode="A")
        self.assertTrue(result)

    def test_dfs_not_found(self):
        """Test case where the target is not found in the graph."""
        result = dfs(self.graph, targetNode="E", currentNode="A")
        self.assertFalse(result)

    def test_dfs_empty_graph(self):
        """Test case where the graph is empty (no nodes)."""
        self.graph = Graph()
        result = dfs(self.graph, targetNode="A")
        self.assertFalse(result)

    def test_dfs_single_node_graph(self):
        """Test case where the graph has a single node and target is the same node."""
        self.graph = Graph()
        self.graph.add_node("A")
        result = dfs(self.graph, targetNode="A", currentNode="A")
        self.assertTrue(result)

    def test_dfs_connected_component(self):
        """Test case where we check the connected component for a random start node."""
        connected_component = set()
        start_node = "A"
        dfs(
            self.graph,
            targetNode="fake target to map out connected component",
            currentNode=start_node,
            visited=connected_component,
        )
        self.assertEqual(
            connected_component, {"A", "B", "C", "D"}
        )  # All reachable nodes should be visited

    def test_dfs_with_random_start(self):
        """Test case where the start node is chosen randomly."""
        start_node = "A"
        connected_component = set()
        # Simulating DFS to explore the connected component
        dfs(
            self.graph,
            targetNode="fake target to map out connected component",
            currentNode=start_node,
            visited=connected_component,
        )
        node_in_graph = random.choice(list(connected_component))
        result = dfs(self.graph, targetNode=node_in_graph, currentNode=start_node)
        self.assertTrue(
            result
        )  # It should be reachable since both are in the connected component


if __name__ == "__main__":
    unittest.main()
