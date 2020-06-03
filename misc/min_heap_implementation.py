import math


class MinHeap:

    def __init__(self,
                 max_size: int) -> None:

        self._heap = []
        self._max_size = max_size

    @property
    def size(self):
        return len(self._heap)

    def __getitem__(self,
                    item: int) -> int:
        return self._heap[item]

    def __setitem__(self,
                    key: int,
                    value: int) -> None:
        self._heap[key] = value

    def _parent(self,
                i: int) -> int:
        return math.ceil(i / 2) - 1

    def _left_child(self,
                    i: int) -> int:
        if i == 0:
            return 1
        else:
            return 2 * i + 1

    def _right_child(self,
                     i: int) -> int:
        if i == 0:
            return 2
        else:
            return 2 * 1 + 2

    def _sift_down(self,
                   i: int) -> None:

        while i < self.size:

            min_index = i
            if self._left_child(i) < self.size and self[min_index] > self[self._left_child(i)]:
                min_index = self._left_child(i)

            if self._right_child(i) < self.size and self[min_index] > self[self._right_child(i)]:
                min_index = self._right_child(i)

            if min_index == i:
                break
            else:
                self[i], self[min_index] = self[min_index], self[i]
                i = min_index

    def _sift_up(self,
                i: int) -> None:

        while i > 0:
            parent_index = self._parent(i)
            if self[parent_index] < self[i]:
                break
            else:
                self[i], self[parent_index] = self[parent_index], self[i]
                i = parent_index

    def insert(self,
               n: int) -> None:

        if self.size == self._max_size:
            raise ValueError()

        self._heap.append(n)
        self._sift_up(self.size - 1)

    def pop(self) -> int:

        if self.size == 0:
            raise ValueError()

        self[0], self[self.size - 1] = self[self.size - 1], self[0]
        min_val = self._heap.pop()
        self._sift_down(0)
        return min_val


