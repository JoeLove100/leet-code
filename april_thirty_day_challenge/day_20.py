"""
Return the root node of a binary search tree that matches the given preorder traversal.
"""
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree_recursive(arr: List[int]) -> Optional[TreeNode]:

    if not arr:
        return None

    current = TreeNode(arr[0])

    current.left = build_tree([n for n in arr[1:] if n < arr[0]])
    current.right = build_tree([n for n in arr[1:] if n > arr[0]])

    return current


def build_tree(arr: List[int]) -> Optional[TreeNode]:

    if not arr:
        return None

    head = TreeNode(arr[0])
    stack = [head]

    for n in arr[1:]:

        prev = stack.pop()
        current = TreeNode(n)

        if current.val < prev.val:
            prev.left = current
            stack.append(prev)
        else:
            while stack and current.val > stack[-1].val:
                prev = stack.pop()
            prev.right = current

        stack.append(current)

    return head


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return build_tree(preorder)


def get_in_order(root: TreeNode) -> List[int]:

    if not root:
        return []

    node_queue = deque([root])
    output = []

    while node_queue:

        current = node_queue.popleft()

        if not current:
            output.append(None)
        else:
            output.append(current.val)
            if current.left or current.right:
                node_queue.append(current.left)
                node_queue.append(current.right)

    return output


def get_tree_in_order(arr: List[int]) -> List[int]:

    tree = build_tree_recursive(arr)
    as_list = get_in_order(tree)
    return as_list
