"""
Given inorder and postorder traversal of a tree, construct the binary tree.
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recreate_tree(in_order: List[int],
                  post_order: List[int]) -> Optional[TreeNode]:

    if not in_order or not post_order:
        return None

    root = TreeNode(post_order.pop())
    current = root
    stack = []
    orders = {n: i for i, n in enumerate(in_order)}

    while post_order:
        next_val = post_order.pop()
        if orders[current.val] < orders[next_val]:
            current.right = TreeNode(next_val)
            stack.append(current)
            current = current.right
        else:
            while stack:
                if orders[stack[-1].val] < orders[next_val]:
                    break
                else:
                    current = stack.pop()

            current.left = TreeNode(next_val)
            current = current.left

    return root


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return recreate_tree(inorder, postorder)


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


def create_list_from_tree(root: Optional[TreeNode]) -> List[int]:

    if not root:
        return []

    output = []
    stack = [root]

    while stack:
        current = stack.pop()
        output.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return output
