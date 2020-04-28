"""
Given a binary tree, return the in-order traversal of its nodes' values.

the recursive solution is trivial, could you do it iteratively?
# """
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


def get_in_order_traversal(head: TreeNode) -> List[int]:

    node_stack = [head]
    traversal = []

    while node_stack:
        current = node_stack[-1]
        if current.left:
            node_stack.append(current.left)
            current.left = None
            continue

        node_stack.pop()
        traversal.append(current.val)

        if current.right:
            node_stack.append(current.right)

    return traversal


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return get_in_order_traversal(root)

if __name__ == "__main__":

    tree = create_tree_from_list([1, 2, None, 3, None, 4])
    in_order = get_in_order_traversal(tree)

    for n in in_order:
        print(n, end=" ")



