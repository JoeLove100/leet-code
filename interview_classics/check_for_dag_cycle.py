from typing import List, Dict


def no_cycles(adj_map: Dict[int, List[int]]) -> bool:
    """
    check if the given adj map does in fact define
    a DAG (ie has no cycles)
    """

    visited = set()

    for i in adj_map:
        if i in visited:
            continue

        current = i
        stack = []
        while True:
            while adj_map[current]:
                stack.append(current)
                current = adj_map[current].pop()
                visited.add(current)
                if current in stack:
                    return False

            if stack:
                current = stack.pop()
            else:
                break

    return True


if __name__ == "__main__":

    adj_map = {0: [1], 1: [2], 2: [3], 3: [], 4: [5], 5: [4]}
    print(no_cycles(adj_map))
