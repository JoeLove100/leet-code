"""
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply
available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

-> Fill any of the jugs completely with water.
-> Empty any of the jugs.
-> Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
"""
from typing import Tuple, List
from collections import deque


def _get_next_states(current_state: Tuple[int, int],
                     x: int,
                     y: int) -> List[Tuple[int, int]]:

    next_states = []

    # pour out one jug
    next_states.extend([(0, current_state[1]), (current_state[0], 0)])

    # pour left into right
    spare_capacity_right = y - current_state[1]
    next_states.append((max(0, current_state[0] - spare_capacity_right),
                        min(y, current_state[1] + current_state[0])))

    # pour right into left
    spare_capacity_left = x - current_state[0]
    next_states.append((min(x, current_state[0] + current_state[1]),
                       max(0, current_state[0] - spare_capacity_left)))

    # fill up one jug
    next_states.extend([(x, current_state[1]), (current_state[0], y)])

    return next_states


def can_measure_water(x: int,
                      y: int,
                      z: int) -> bool:

    visited = {(0, 0)}
    states = deque([(0, 0)])

    while states:
        current_state = states.popleft()
        if z in current_state or z == sum(current_state):
            return True

        possible_next_states = _get_next_states(current_state, x, y)
        for next_state in possible_next_states:
            if next_state not in visited:
                visited.add(next_state)
                states.append(next_state)

    return False


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        return can_measure_water(x, y, z)


if __name__ == "__main__":

    print(can_measure_water(1, 10, 5))
