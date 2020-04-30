"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree
along the parent-child connections. The path must contain at least one node and does not need to go through the root.
"""
from typing import Tuple, List
from collections import deque
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _get_max_path_to_root_and_in_tree(root: TreeNode) -> Tuple[int, int]:

    if root.left:
        max_path_to_left, max_path_in_left = _get_max_path_to_root_and_in_tree(root.left)
    else:
        max_path_to_left, max_path_in_left = 0, -math.inf

    if root.right:
        max_path_to_right, max_path_in_right = _get_max_path_to_root_and_in_tree(root.right)
    else:
        max_path_to_right, max_path_in_right = 0, -math.inf

    max_path_to_root = root.val + max(0, max_path_to_right, max_path_to_left)
    max_path_through_root = root.val + max(0, max_path_to_left) + max(0, max_path_to_right)
    max_path_in_tree = max(max_path_in_left, max_path_in_right, max_path_through_root)

    return max_path_to_root, max_path_in_tree


def get_max_path_sum(root: TreeNode) -> int:

    _, max_in_tree = _get_max_path_to_root_and_in_tree(root)
    return max_in_tree


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return get_max_path_sum(root)


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
