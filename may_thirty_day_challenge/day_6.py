"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.
"""

from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_tree_from_list(arr: List[int]) -> TreeNode:

    arr = arr[::-1]
    head = TreeNode(arr.pop())
    node_queue = deque([head])

    while arr:
        current = node_queue.popleft()
        left_val = arr.pop()
        if left_val:
            current.left = TreeNode(left_val)
            node_queue.append(current.left)

        if not arr:
            break
        else:
            right_val = arr.pop()
            if right_val:
                current.right = TreeNode(right_val)
                node_queue.append(current.right)

    return head


def are_cousins(root: TreeNode,
                x: int,
                y: int) -> bool:

    node_queue = deque([root])
    parents = dict()

    while node_queue:
        level_counter = len(node_queue)
        nodes_on_level = set()

        while level_counter > 0:
            current_node = node_queue.popleft()
            nodes_on_level.add(current_node.val)

            if current_node.left:
                node_queue.append(current_node.left)
                parents.update({current_node.left.val: current_node.val})

            if current_node.right:
                node_queue.append(current_node.right)
                parents.update({current_node.right.val: current_node.val})

            level_counter -= 1

        if x in nodes_on_level and y in nodes_on_level:
            return parents[x] != parents[y]
        elif x in nodes_on_level and y not in nodes_on_level:
            return False
        elif x not in nodes_on_level and y in nodes_on_level:
            return False

    raise ValueError("Neither node is in tree")


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        return are_cousins(root, x, y)
