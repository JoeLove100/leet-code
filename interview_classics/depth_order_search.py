"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
"""
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_level_order(root: TreeNode) -> List[List[int]]:

    if not root:
        return []

    levels = []
    node_queue = deque([(root, 0)])

    while node_queue:

        current_node, current_level = node_queue.popleft()

        if len(levels) <= current_level:
            levels.append([])
        levels[current_level].append(current_node.val)

        if current_node.left:
            node_queue.append((current_node.left, current_level + 1))

        if current_node.right:
            node_queue.append((current_node.right, current_level + 1))

    return levels


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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return get_level_order(root)


if __name__ == "__main__":

    tree = create_tree_from_list([0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8])
    dos = get_level_order(tree)

    for lst in dos:
        print(lst)
