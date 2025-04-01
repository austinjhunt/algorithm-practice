**Questions:**

**Algorithms:**

1.  **What is the time complexity of Merge Sort in the worst-case scenario?**

    O(nlogn). logn comes from height of binary tree. n comes from iterative merging.

2.  **Explain the difference between Breadth-First Search (BFS) and Depth-First Search (DFS).**

    BFS leverages a queue. Add a node to queue initially, then while queue not empty, pop a node from it, add to visited set, and add all of its neighbors to the queue.

    DFS leverages recursion with args currentNode, targetNode, and visited nodes set. If you have not visited a node yet, add to a visited set, return true if target matches current, otherwise iterate over currentNode neighbors and recursively call DFS on each one. if any return true, return True. Return false at end of function to represent missing target.

3.  **Under what condition is Binary Search applicable, and what is its time complexity?**

    Binary search is only applicable when data is already sorted. Algorithm is recursively passing an array, a target, a start index, and end index, set a middle index to start + end // 2. Stop condition is start > end. If middle value matches target, return middle or true. if target less than middle, return recursive call on array,target,start,middle-1. If greater than middle, return recursive call on array, target, start+1, end. Since you are recursively splitting array in half, worst case is log of n. Best case is O(1) if target is the first middle element.

**Data Structures:**

4.  **Describe the key characteristics of a Hash Table and how it works.**

    Hash tables provide benefit of O(1) time complexity for searching. A hash table maps keys to indices in a table using a hash function (e.g., hash of key mod table size), with an ideal hash function working to minimize collisions and maximize randomness / distribution of keys across the table. To handle collisions you can leverage chaining. That is, if a hash function maps 2 separate key to same index in table, you can store a linked list, or a list of some sort, in that location so that both of those keys can share the space. Space complexity of Hash Table is O(K) where K is number of keys (rather, key-value pairs). As you add more keys, you have to increase the space it occupies linearly (at least) to meet that demand. Although, in my implementation, I add a \_resize() argument allowing you to increase that size by a multiple, like 1.5 times the current size.

5.  **Explain the difference between a Tree and a Graph data structure.**

    A graph is ultimately a set of vertices V={v1,v2,v3...} and Edges={(v1,v2), (v1,v3), (v2,v4)....}. A tree is a type of graph that is connected and has no cycles. In other words, for any 2 vertices in a tree graph, there is exactly one path (ordered list of edges) connecting them.

6.  **What are the primary operations performed on a Stack and a Queue, and how do they differ?**

    Stack is a LIFO (last in first out) data structure. Easiest way to remember this is a stack of plates. The last one you put on top is the first one (haha, ideally) that you remove. Adding to a stack is called "pushing", removing from a stack is called "popping". Stacks are a good way to represent recursion. When you make a recursive call in a function, you are pushing new data onto the recursion stack. When the recursive function returns, you are popping from the recursion stack and that popped value can then be used by the calling function.

    Queue is a FIFO (first in first out) data structure. Pretty simple. We refer to waiting lines as queues because whoever is currently first in line will be the next person to leave that line. Adding to a queue is called enqueuing and removing is dequeuing. We use queues to implement breadth first searches on graphs. First initialize a queue with just one start node in the graph, then while the queue is empty, pop the first one from the queue; if not already visited, add to a visited set, then enqueue all of the node's neighbors. This means we're traversing / visiting one level of the graph at a time (level K nodes meaning nodes that are K edges from the starting node).

7.  **What is a Heap, and what are its common applications?**

    A heap is a nearly complete binary tree used for heapsort and priorty queues. There are specifically two kinds of heaps: max heaps and min heaps. A max heap is a heap such that for any node in the heap, its value is less than or equal to the value its parents. This means the root is the maximum. Max heaps are used to implement heapsort algorithms. A min heap is a heap such that for any node in the heap, its value is greater than or equal to the value of its parent. The root is the minimum. Min heaps are used to implement priority queues.

    For the "nearly complete" constraint, this means all but the last level of the tree is full, and the last level is filled starting from the left.

    Some key notes:
    When representing a heap as an array, we can represent the following about a node at index i.

    - Left child index in array = 2 \* i
    - Right child index in array = 2 \* i + 1
    - Parent index in array = floor(i / 2)
      It's quite useful to use 1-based indexing on the array representation of a heap so these calculations are simpler.

**Concepts:**

8.  **What is Big O notation used for, and why is it important in algorithm analysis?**

    Big O notation is used to represent how an algorithm's space or time complexity grows in relation to its input data, and it's useful in determining whether a given algorithm is a good choice to solve a specific problem like sorting or searching. At its core, this means "as the size n of my input grows, how can I express the number of times my most basic operation, like a comparison, is run, relative to the size n of my input?" For instance, O(n^2) means an algorithm's complexity will grow quadratically relative to its input data as its input grows. Simple example of this is an algorithm with a nested loop like bubblesort. Minimizing time complexity is a common goal but it's not always the primary goal. Sometimes teams want to keep processes simple, readable, and maintainable even if it means sacrificing efficiency. It's useful to know characteristics of your input data since algorithm complexity can range depending on those characteristics. For instance, if you have a fully or nearly sorted list, running quicksort on that list results in the algorithm's worst time complexity of O(n^2), as opposed to its best O(nlogn). Or if insertion sort is used on a list that's initially fully in reverse order, the algorithm will run in O(n^2).

9.  **Explain the concept of Recursion and provide an example of a problem where it is commonly used.**

    With recursion, we have a function that is calling itself. To avoid stack overflow (calling itself infinitely), we need a base case, which is just a stop condition, and we need to make sure that we are always going to somehow reach that base case. This usually involves recursively taking input parameter values (arguments), updating them with new values, and passing those new values to a new function call until the base case / stop condition is satisfied. Each recursive call of a function is pushed to a stack, and is popped when it returns. The bottom of the stack represents the first invocation of the function.
