# drills
def mergesort(array):
    # need to recursively split into halves then merge the two halfs back together
    def _merge(a, b):
        # merge arrays into sorted output
        merged = []
        while len(a) > 0 and len(b) > 0:
            if a[0] <= b[0]:
                merged.append(a.pop(0))
            else:
                merged.append(b.pop(0))
        # either a or b empty
        while len(a) > 0:
            merged.append(a.pop(0))
        while len(b) > 0:
            merged.append(b.pop(0))
        return merged

    if len(array) == 1:
        return array
    # 2 or more. split
    a, b = array[: len(array) // 2], array[len(array) // 2 :]
    a, b = mergesort(a), mergesort(b)
    return _merge(a, b)


def bfs(graph, target):
    from collections import deque

    visited = set()
    start = graph.getRandomNode()
    q = deque([start])
    while q:
        node = q.popleft()
        if node not in visited:
            visited.add(node)
            if node == target:
                return "found"
            q.extend(node.get_neighbors())
    return "not found"


def dfs(graph, current, target, visited):
    if current is None:
        current = graph.getRandomNode()
    if visited == None:
        visited = set()

    if current not in visited:
        visited.add(current)
        if current == target:
            return "found"
        for neighbor in current.get_neighbors():
            if dfs(graph, neighbor, target, visited) == "found":
                return "found"
    return "not found"


def binarysearch(array, target, start, end):
    if start > end:
        return "not found"

    middle = (start + end) // 2
    if array[middle] == target:
        return "found"
    # short circuit, avoid right call if possible
    left = binarysearch(array, target, start, middle - 1)
    if left == "found":
        return "found"
    right = binarysearch(array, target, middle + 1, end)
    if right == "found":
        return "found"
    return "not found"


def heapsort(array):
    # build max heap
    # find and remove largest item from that heap (root)
    # place that item in sorted position (end of array)
    out = []

    def buildmaxheapfromarray(a: list): 
        # remember: good to use 1 based indexing 
        # node left child = 2 * node index
        # node right child = 2 * node index + 1
        # parent = node index // 2