"""Dijsktra's shortest path algorithm"""

from src.structures.graph import Graph
import heapq


def dijkstra(graph: Graph, start=None):
    """
    Finds the shortest path from the start node to all other nodes in a weighted graph.
    :param graph: Dictionary where keys are nodes and values are lists of (neighbor, weight) tuples.
    :param start: The starting node.
    :return: Dictionary of shortest distances from start node to each other node.
    """
    if start is None:
        start = graph.get_random_node()

    # use a min heap (parent always smaller than children)
    # to always process the node with smallest known distance

    # initialize min heap. item structure is (distance, node)
    minheap = [(0, start)]

    # initialize all distances to infinity
    distances = {node: float("inf") for node in graph}

    distances[start] = 0

    while minheap:
        # while the heap still has (distance, neighbor) items

        # get distance and node by popping from heap (pulls smallest item off heap)
        # heapq treats heaps as min heaps by default
        # tuples compared by first element so popping from a min heap
        # always returns tuple with smallest distance value, meaning
        # we prioritize the closest/most promising next node first
        current_distance, current_node = heapq.heappop(minheap)

        if current_distance > distances[current_node]:
            # not a shortest distance; ignore
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # add new minimum distance to this neighbor to the heap
                heapq.heappush(minheap, (distance, neighbor))

    return distances
