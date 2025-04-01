"""
Graph structure implementation
"""

import random
import logging

logger = logging.getLogger(__name__)


class Graph:
    def __init__(self):
        self.adjacency_list = {}  # best for sparse graphs
        # Adjacency matrix requires an ordered nodes list as well
        self.nodes = []
        self.adjacency_matrix = []

    def get_node_neighbors(self, node):
        return self.adjacency_list.get(node, [])

    def get_random_node(self):
        return (
            random.choice(list(self.adjacency_list.keys()))
            if self.adjacency_list
            else None
        )

    def list_nodes(self):
        return self.nodes

    def add_node(self, node):
        """Add a node to a graph"""
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
            # Now update adjacency matrix as well for demo purposes
            self.nodes.append(node)
            size = len(self.nodes)
            for row in self.adjacency_matrix:
                # new column for node
                row.append(0)
            # new row for node
            self.adjacency_matrix.append([0] * size)

    def add_edge(self, edge: tuple, weight=None, directed=False):
        """Add an edge to a graph (tuple of 2 nodes represents edge between those nodes )"""
        node1, node2 = edge
        self.add_node(node1)
        self.add_node(node2)
        self.adjacency_list[node1].append(node2)
        if not directed:
            self.adjacency_list[node2].append(node1)
        idx1, idx2 = self.nodes.index(node1), self.nodes.index(node2)
        self.adjacency_matrix[idx1][idx2] = weight if weight else 1
        if not directed:
            self.adjacency_matrix[idx2][idx1] = (
                weight if weight else 1
            )  # symmetric for undirected graph

    def __repr__(self):
        out = ""
        for node, neighbors in self.adjacency_list.items():
            out += f"\t{node}: {neighbors}\n"
        return out


def build_sample_graph(edges: int = 30, vertices: int = 40):
    graph = Graph()
    logger.info({"action": "build_sample_graph", "edges": edges, "vertices": vertices})
    v = set()
    for i in range(vertices):
        v.add(random.randint(0, 1000))
    vlist = list(v)
    for _ in range(edges):
        node1, node2 = random.sample(vlist, 2)  # Picks two distinct nodes
        graph.add_edge((node1, node2))
    return graph


if __name__ == "__main__":
    graph = build_sample_graph()
