"""
Binary search tree implementation
"""

import logging
from src.structures.node import BSTNode

logger = logging.getLogger(__name__)


class BinarySearchTree:
    def __init__(self, root: BSTNode = None):
        self.root = root

    def insert(self, value):
        logger.info({"action": "BinarySearchTree.insert", "value": value})
        self.root = self._insert(self.root, value)

    def _insert(self, node: BSTNode, value):
        """Insert a value into BST"""
        if node is None:
            return BSTNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        return node

    def _search(self, node: BSTNode, target):
        """Search for a value in BST"""
        if node is None or node.value == target:
            return node
        if target < node.value:
            return self._search(node.left, target)
        else:
            return self._search(node.right, target)

    def search(self, target):
        logger.info({"action": "BinarySearchTree.search", "target": target})
        return self._search(self.root, target)

    def delete(self, target):

        logger.info({"action": "BinarySearchTree.delete", "target": target})
        self._delete(self.root, target)

    def _delete(self, node: BSTNode, target):
        """delete a value from a BST if present"""
        if node is None:
            return None

        if target < node.value:
            node.left = self._delete(node.left, target)

        elif target > node.value:
            node.right = self._delete(node.right, target)

        elif target == node.value:
            if node.left is None:
                return node.right  # removes current node
            elif node.right is None:
                return node.left  # removes current node
            else:
                # node has 2 children.
                # find smallest node in the right subtree. move that to current node's position
                min_node_in_right_subtree = self._get_min_value_node(node.right)
                node.value = min_node_in_right_subtree.value
                # delete from its original position
                node.right = self._delete(node.right, min_node_in_right_subtree.value)

    def _get_min_value_node(self, node: BSTNode):
        # always left child , parent, right child in order
        # so min node is leftmost node in tree
        min_node = node
        while min_node.left is not None:
            min_node = min_node.left
        return min_node

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node: BSTNode) -> list:
        """return elements of BST tree in order as a list"""
        if node is None:
            return []
        return self._inorder(node.left) + [node.value] + self._inorder(node.right)
