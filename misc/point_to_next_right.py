"""
Given a binary tree, populate each "next" pointer to point to its next right node. If there is no
next right node, the "next" pointer should be set to NULL.

Initially, all "next" pointers are set to NULL.
"""

from collections import deque
from typing import List


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def point_next_to_right(root: Node) -> Node:

    if not root:
        return root

    q = deque([root])

    while q:

        level_count = len(q)

        while True:
            current_node = q.popleft()
            level_count -= 1

            if current_node.left:
                q.append(current_node.left)

            if current_node.right:
                q.append(current_node.right)

            if level_count > 0:
                current_node.next = q[0]
            else:
                break

    return root


class Solution:
    def connect(self, root: Node) -> Node:
        return point_next_to_right(root)


def create_tree_from_list(arr: List[int]) -> Node:

    arr = arr[::-1]
    head = Node(arr.pop())
    node_queue = deque([head])

    while arr:
        current = node_queue.popleft()
        left_val = arr.pop()
        if left_val:
            current.left = Node(left_val)
            node_queue.append(current.left)

        if not arr:
            break
        else:
            right_val = arr.pop()
            if right_val:
                current.right = Node(right_val)
                node_queue.append(current.right)

    return head


if __name__ == "__main__":

    tree = create_tree_from_list([1, 2, 3, 4, None, 5, None])
    tree = point_next_to_right(tree)
    print("done")
