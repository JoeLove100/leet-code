"""
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum
width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.
The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes
in the level, where the null nodes between the end-nodes are also counted into the length calculation.
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_width(root: Optional[TreeNode]) -> int:

    if not root:
        return 0

    q = deque([(root, 0)])
    max_width = 1

    while q:
        nodes_on_row = len(q)
        node_counter = 1
        while node_counter <= nodes_on_row:
            current, i = q.popleft()
            if node_counter == 1:
                start = i
            if node_counter == nodes_on_row:
                end = i

            if current.left:
                q.append((current.left, 2 * i))
            if current.right:
                q.append((current.right, 2 * i + 1))

            node_counter += 1

        max_width = max(max_width, end - start + 1)

    return max_width


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        return get_width(root)


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
