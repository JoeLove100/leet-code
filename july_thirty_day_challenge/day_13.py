"""
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def are_same(root_1: Optional[TreeNode],
             root_2: Optional[TreeNode]) -> bool:

    if not root_1 and not root_2:
        # both trees are null so equal
        return True

    if not root_1 or not root_2:
        # only one tree null so not equal
        return False

    q_1 = deque([(root_1, 0)])
    q_2 = deque([(root_2, 0)])

    while q_1 and q_2:
        if len(q_1) != len(q_2):
            # different row lengths - must not be equal
            return False

        nodes_on_row = len(q_1)
        while nodes_on_row > 0:
            node_1, pos_1 = q_1.popleft()
            node_2, pos_2 = q_2.popleft()

            if pos_1 != pos_2:
                # next nodes in different positions - not equal
                return False

            if node_1.val != node_2.val:
                # same position but different value - not equal
                return False

            if node_1.left:
                q_1.append((node_1.left, 2 * pos_1))
            if node_1.right:
                q_1.append((node_1.right, 2 * pos_1 + 1))

            if node_2.left:
                q_2.append((node_2.left, 2 * pos_2))
            if node_2.right:
                q_2.append((node_2.right, 2 * pos_2 + 1))

            nodes_on_row -= 1

    return not q_1 and not q_2  # only equal if both have used up all nodes


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return are_same(p, q)


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
