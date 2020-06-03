from typing import List, Dict
from collections import deque


def is_bipartite(adj_map: Dict[int, List[int]],
                 start: int) -> bool:

    q = deque([start])
    group = 0
    colours = {start: 1}

    while q:
        level_count = len(q)
        while level_count > 0:
            current = q.popleft()
            for next_node in adj_map[current]:
                if next_node in colours and colours[next_node] != group:
                    return False
                elif next_node not in colours:
                    colours.update({next_node: group})
                    q.append(next_node)

            level_count -= 1

        group = (group + 1) % 2

    return True


if __name__ == "__main__":

    adj_map = {0: [0, 1], 1: []}
    print(is_bipartite(adj_map, 0))
