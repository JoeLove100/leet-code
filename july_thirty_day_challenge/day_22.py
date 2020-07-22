"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then
right to left for the next level and alternate between).
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_zig_zag(root: Optional[TreeNode]) -> List[List[int]]:

    if not root:
        return []

    output = []
    q = deque([root])
    fwd_traverse = True

    while q:
        nodes_on_level = deque([])
        level_count = len(q)

        while level_count > 0:
            current = q.popleft()
            if fwd_traverse:
                nodes_on_level.append(current.val)
            else:
                nodes_on_level.appendleft(current.val)

            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)

            level_count -= 1

        output.append(list(nodes_on_level))
        fwd_traverse = not fwd_traverse

    return output


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        return get_zig_zag(root)


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
