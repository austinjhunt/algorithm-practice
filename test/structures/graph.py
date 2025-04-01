import unittest
from src.structures.graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge(("A", "B"))
        self.graph.add_edge(("A", "C"), weight=3)
        self.graph.add_edge(("B", "D"))

    def test_add_node(self):
        self.graph.add_node("E")
        self.assertIn("E", self.graph.adjacency_list)
        self.assertEqual(self.graph.get_node_neighbors("E"), [])

    def test_add_edge(self):
        self.assertIn("B", self.graph.get_node_neighbors("A"))
        self.assertIn("A", self.graph.get_node_neighbors("B"))  # Undirected
        self.assertEqual(self.graph.adjacency_matrix[0][1], 1)  # A-B edge

    def test_add_directed_edge(self):
        self.graph.add_edge(("C", "E"), directed=True)
        self.assertIn("E", self.graph.get_node_neighbors("C"))
        self.assertNotIn("C", self.graph.get_node_neighbors("E"))  # Directed edge

    def test_get_random_node(self):
        self.assertIn(self.graph.get_random_node(), ["A", "B", "C", "D"])

    def test_graph_representation(self):
        repr_output = repr(self.graph)
        self.assertIn("A: [", repr_output)
        self.assertIn("B: [", repr_output)
        self.assertIn("C: [", repr_output)
        self.assertIn("D: [", repr_output)
