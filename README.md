# Algorithm Practice

This repository contains implementations of some well-known leet-codey algorithms for searching and sorting data structures.

## Sorting

### Heap Sort

Heap Sort is a comparison-based sorting algorithm that leverages a binary heap data structure. It works by first transforming the input array into a max heap and then repeatedly extracting the maximum element from the heap to build the sorted array.

- **Time Complexity**: O(n log n) for both best, average, and worst cases.
- **Use Cases**: Suitable for large datasets when in-place sorting is required and heap data structures are already in use.

### Bubble Sort

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed.

- **Time Complexity**: O(n^2) in worst and average cases, O(n) in the best case (already sorted input).
- **Use Cases**: Useful for small datasets or when simplicity is preferred over efficiency.

### Insertion Sort

Insertion Sort builds the sorted array one element at a time, taking each element and inserting it into its correct position relative to the previously sorted elements.

- **Time Complexity**: O(n^2) in worst and average cases, O(n) in best case.
- **Use Cases**: Good for small or nearly sorted datasets due to its adaptability.

### Merge Sort

Merge Sort is a divide-and-conquer algorithm that splits the input array into halves, sorts each half recursively, and then merges the sorted halves.

- **Time Complexity**: O(n log n) for all cases.
- **Use Cases**: Efficient for large datasets, useful in external sorting where data cannot be loaded into memory at once.

### Quick Sort

Quick Sort is another divide-and-conquer algorithm that picks a pivot element, partitions the array around the pivot, and recursively sorts the partitions.

- **Time Complexity**: O(n log n) on average, O(n^2) in the worst case (when the smallest or largest element is always picked as pivot).
- **Use Cases**: Often the fastest sorting method for general-purpose use in practice due to its efficient in-memory performance.

## Searching

### Binary Search

Binary Search is an efficient algorithm for finding an element in a sorted array by repeatedly dividing the search interval in half.

- **Time Complexity**: O(log n) for all cases.
- **Use Cases**: Ideal for searching in large, sorted datasets where random access is possible.

### Depth-First Search (DFS)

DFS is a graph traversal algorithm that explores as far as possible along a branch before backtracking.

- **Time Complexity**: O(V + E), where V is the number of vertices and E is the number of edges.
- **Use Cases**: Used in pathfinding, cycle detection, and solving mazes.

### Breadth-First Search (BFS)

BFS explores a graph level by level, ensuring that all nodes at the current depth are visited before moving deeper.

- **Time Complexity**: O(V + E).
- **Use Cases**: Used in shortest path algorithms (like Dijkstra's), web crawling, and network broadcasting.
