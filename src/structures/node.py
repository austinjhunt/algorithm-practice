"""Node representations"""

import uuid


class Node:
    def __init__(self, value):
        self.value = value
        self.id = uuid.uuid4()

    def getID(self):
        return str(self.id)

    def equals(self, node):
        return self.value == node.value

    def __str__(self):
        return f"Node({self.value})"

    def __repr__(self):
        return f"Node({self.value})"


class GraphNode(Node):
    def __init__(self, value):
        super().__init__(value)


class QueueNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.next = None

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next

    def get_value(self):
        return self.value

    def __str__(self):
        print(f"<Node value={self.value}>")

    def __repr__(self):
        print(f"<Node value={self.value}>")
