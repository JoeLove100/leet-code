"""
Invert a binary tree.
"""
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_binary_tree(root: TreeNode) -> TreeNode:

    if not root:
        return root

    traversal = deque([])
    q = deque([root])

    while q:
        current = q.popleft()
        traversal.append(current.val if current else None)
        if current is not None:
            q.append(current.left)
            q.append(current.right)

    new_root = TreeNode(traversal.popleft())
    q = deque([new_root])

    while traversal:

        current = q.popleft()

        if traversal[0] is None:
            traversal.popleft()
        else:
            current.right = TreeNode(traversal.popleft())
            q.append(current.right)

        if traversal:
            if traversal[0] is None:
                traversal.popleft()
            else:
                current.left = TreeNode(traversal.popleft())
                q.append(current.left)

    return new_root


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return invert_binary_tree(root)


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


def dfs(root: TreeNode) -> List[int]:

    q = deque([root])
    output = []

    while q:

        current = q.popleft()
        output.append(current.val if current else None)
        if current:
            q.append(current.left)
            q.append(current.right)

    while not output[-1]:
        output.pop()

    return output
