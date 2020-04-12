"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is
the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
"""
from typing import Dict, Optional
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_height(node: TreeNode,
               memo: Dict[TreeNode, int]) -> int:

    if node is None:
        return 0
    elif node in memo:
        return memo[node]
    else:
        height = 1 + max(get_height(node.left, memo), get_height(node.right, memo))
        memo[node] = height
        return height


def get_max_path_length(node: Optional[TreeNode]) -> int:

    if node is None:
        return 0

    max_path_len = 0
    memo = {}
    node_queue = deque([node])

    while node_queue:

        current_node = node_queue.popleft()
        left_height = get_height(current_node.left, memo)
        right_height = get_height(current_node.right, memo)
        max_path_len = max(max_path_len, left_height + right_height)

        if 2 * left_height > max_path_len:
            node_queue.append(current_node.left)
        if 2 * right_height > max_path_len:
            node_queue.append(current_node.right)

    return max_path_len



class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return get_max_path_length(root)


def build_tree(arr: [int]) -> TreeNode:

    arr = deque(arr)
    head_node = TreeNode(arr.popleft())
    node_queue = deque([head_node])

    while arr:
        current_node = node_queue.popleft()
        val = arr.popleft()
        if val:
            current_node.left = TreeNode(val)
            node_queue.append(current_node.left)
        if arr:
            val = arr.popleft()
            if val:
                current_node.right = TreeNode(val)
                node_queue.append(current_node.right)

    return head_node


def print_tree(node: TreeNode) -> None:

    if not node:
        print("Empty tree")

    node_queue = deque([node])

    while node_queue:
        current = node_queue.popleft()
        print(current.val)

        if current.left:
            node_queue.append(current.left)
        if current.right:
            node_queue.append(current.right)


if __name__ == "__main__":

    arr = [1, 2, None, 3, 4, 5, 6, 7, 8]
    tree = build_tree(arr)
    print_tree(tree)
    max_path = get_max_path_length(tree)
    print(f"Max path length is {max_path}")
