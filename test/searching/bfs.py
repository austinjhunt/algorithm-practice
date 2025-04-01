import unittest
from unittest.mock import MagicMock
from src.searching.bfs import bfs, get_connected_component_vertices_bfs
from src.structures.graph import Graph


class TestBFS(unittest.TestCase):

    def setUp(self):
        # Mock the Graph class
        self.graph = MagicMock(spec=Graph)

        # Mock methods of the graph
        self.graph.get_random_node.return_value = "A"
        self.graph.get_node_neighbors.return_value = ["B", "C"]

        # Mock a scenario where we have a simple connected graph for BFS
        self.graph.get_node_neighbors = MagicMock(
            side_effect=lambda node: {
                "A": ["B", "C"],
                "B": ["A", "D"],
                "C": ["A"],
                "D": ["B"],
            }.get(node, [])
        )

    def test_bfs_found(self):
        # Test case where target node is found in the graph
        result = bfs(self.graph, targetNode="D", startNode="A")
        self.assertTrue(result)

    def test_bfs_not_found(self):
        # Test case where target node is not found in the graph
        result = bfs(self.graph, targetNode="E", startNode="A")
        self.assertFalse(result)

    def test_bfs_with_random_start(self):
        # Test case using a random start node from the graph's mocked get_random_node method
        self.graph.get_random_node.return_value = "A"
        result = bfs(self.graph, targetNode="D")
        self.assertTrue(result)

    def test_get_connected_component_vertices_bfs(self):
        # Test connected component vertices using BFS
        result = get_connected_component_vertices_bfs(self.graph, start_node="A")
        expected_result = {
            "A",
            "B",
            "C",
            "D",
        }  # This assumes our graph is connected as per the mock
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
