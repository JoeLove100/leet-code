class MinStack:

    def __init__(self):
        self._min_stack = []
        self._stack = []

    def push(self, x: int) -> None:
        if not self._min_stack or self._min_stack[-1] >= x:
            self._min_stack.append(x)
        self._stack.append(x)

    def pop(self) -> None:
        val = self._stack.pop()
        if self._min_stack and self._min_stack[-1] == val:
            self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]


if __name__ == "__main__":

    min_stack = MinStack()
    min_stack.push(0)
    min_stack.push(1)
    min_stack.push(0)
    print(min_stack.getMin())
    min_stack.pop()
    print(min_stack.getMin())
