from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_right_view(root: TreeNode) -> List[int]:

    if not root:
        return []

    node_queue = deque([root])
    right_view = []

    while node_queue:
        count = len(node_queue)

        while count > 0:

            current_node = node_queue.popleft()
            count -= 1
            if count == 0:
                right_view.append(current_node.val)

            if current_node.left:
                node_queue.append(current_node.left)

            if current_node.right:
                node_queue.append(current_node.right)

    return right_view


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        return get_right_view(root)


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


if __name__ == "__main__":

    tree = create_tree_from_list([1, 2, 3, 4, 5, 6])
    rv = get_right_view(tree)
    print(rv)
