from collections import deque
from typing import Dict, List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def _get_bottom_view(root: TreeNode,
                     position: int,
                     output: Dict[int, int]) -> None:

    if root.right:
        _get_bottom_view(root.right, position + 1, output)

    if root.left:
        _get_bottom_view(root.left, position - 1, output)

    if position not in output:
        output[position] = root.val


def get_bottom_view(root) -> List[int]:

    output_dict = dict()
    output = []

    _get_bottom_view(root, 0, output_dict)

    for key in sorted(list(output_dict)):
        output.append(output_dict[key])

    return output


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

    tree = create_tree_from_list([1, 2, 3, 4, 5, None, 6])
    v = get_bottom_view(tree)
    print(v)


