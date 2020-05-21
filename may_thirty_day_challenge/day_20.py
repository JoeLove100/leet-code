"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
"""
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_kth_smallest_element(root: TreeNode,
                             k: int):

    counter = 0
    stack = []
    current = root

    while True:

        while current is not None:
            stack.append(current)
            current = current.left

        if not stack:
            break
        else:
            counter += 1
            prev = stack.pop()

            if counter == k:
                return prev.val
            else:
                current = prev.right

    raise ValueError("Traversal terminated before kth element found")


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


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return get_kth_smallest_element(root, k)
