"""
Given a complete binary tree, count the number of nodes.
"""
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_node_count(root: Optional[TreeNode]) -> int:

    if not root:
        return 0

    counter = 0
    q = deque([root])

    while q:
        current_node = q.popleft()
        counter += 1
        if current_node.left:
            q.append(current_node.left)
        if current_node.right:
            q.append(current_node.right)

    return counter


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
