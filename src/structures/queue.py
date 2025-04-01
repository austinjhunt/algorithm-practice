from src.structures.node import QueueNode


class Queue:

    def __init__(self, firstNode: QueueNode = None):
        self.head = firstNode
        self.tail = firstNode

    def is_empty(self):
        return self.head is None

    def add(self, node: QueueNode):
        if self.is_empty():
            # One node. Node is both head and tail of queue.
            self.head = node
            self.tail = node
        else:
            # Point current tail at new one.
            current_tail = self.tail
            current_tail.set_next(node)
            # New node becomes tail.
            self.tail = node

    def pop(self):
        if self.is_empty():
            return None
        current_head = self.head

        # Update head of queue to next in line
        self.head = self.head.get_next()

        current_head.set_next(None)  # not attached anymore
        return current_head
