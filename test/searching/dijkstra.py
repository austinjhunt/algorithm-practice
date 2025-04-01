from src.searching.dijsktra import dijkstra
import unittest


# Unit Tests
class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.graph = {
            "A": [("B", 1), ("C", 4)],
            "B": [("A", 1), ("C", 2), ("D", 5)],
            "C": [("A", 4), ("B", 2), ("D", 1)],
            "D": [("B", 5), ("C", 1)],
        }

    def test_dijkstra(self):
        self.assertEqual(dijkstra(self.graph, "A"), {"A": 0, "B": 1, "C": 3, "D": 4})
        self.assertEqual(dijkstra(self.graph, "B"), {"A": 1, "B": 0, "C": 2, "D": 3})
        self.assertEqual(dijkstra(self.graph, "C"), {"A": 3, "B": 2, "C": 0, "D": 1})
        self.assertEqual(dijkstra(self.graph, "D"), {"A": 4, "B": 3, "C": 1, "D": 0})

    def test_single_node_graph(self):
        self.assertEqual(dijkstra({"A": []}, "A"), {"A": 0})

    def test_disconnected_graph(self):
        disconnected_graph = {
            "A": [("B", 2)],
            "B": [("A", 2)],
            "C": [],  # 'C' is disconnected
        }
        self.assertEqual(
            dijkstra(disconnected_graph, "A"), {"A": 0, "B": 2, "C": float("inf")}
        )


if __name__ == "__main__":
    unittest.main()
