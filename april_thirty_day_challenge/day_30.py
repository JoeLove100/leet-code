"""
Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given
string is a valid sequence in such binary tree.

We get the given string from the concatenation of an array of integers arr and the concatenation of all values
of the nodes along a path results in a sequence in the given binary tree.
"""
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid(root: Optional[TreeNode],
             arr: List[int]) -> bool:

    if root is None:
        return False

    if not arr:
        return True

    node_queue = deque([root])
    arr = deque(arr)

    while node_queue and arr:

        count = len(node_queue)
        val = arr.popleft()
        matching_entry = False
        valid_leaf = False

        while count > 0:
            current = node_queue.popleft()
            count -= 1

            if current.val == val:
                matching_entry = True
                if current.left:
                    node_queue.append(current.left)

                if current.right:
                    node_queue.append(current.right)

                if not current.left and not current.right:
                    valid_leaf = True

        if not matching_entry:
            return False

    return valid_leaf and not arr


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        return is_valid(root, arr)


def create_tree_from_list(arr: List[int]) -> TreeNode:

    arr = arr[::-1]
    head = TreeNode(arr.pop())
    node_queue = deque([head])

    while node_queue and arr:
        current = node_queue.popleft()
        left_val = arr.pop()
        if left_val is not None:
            current.left = TreeNode(left_val)
            node_queue.append(current.left)

        if not arr:
            break
        else:
            right_val = arr.pop()
            if right_val is not None:
                current.right = TreeNode(right_val)
                node_queue.append(current.right)

    return head
