"""
Given inorder and postorder traversal of a tree, construct the binary tree.

You may assume that duplicates do not exist in the tree.
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_tree(in_order: List[int],
             post_order: List[int]) -> Optional[TreeNode]:

    if not post_order:
        return None

    orders = {n: i for i, n in enumerate(in_order)}

    head = TreeNode(post_order.pop())

    def add_node(root: TreeNode, val: int):

        if orders[val] < orders[root.val]:
            if root.left:
                add_node(root.left, val)
            else:
                root.left = TreeNode(val)
        else:
            if root.right:
                add_node(root.right, val)
            else:
                root.right = TreeNode(val)

    while post_order:
        add_node(head, post_order.pop())

    return head


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return get_tree(inorder, postorder)
