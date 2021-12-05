class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return

        min_value = self.getMin()
        if val < min_value:
            min_value = val
        self.stack.append((val, min_value))

    def pop(self) -> None:
        self.stack.pop()
        return

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


def test():
    min_stack = MinStack()

    assert min_stack.push(-2) is None
    assert min_stack.push(0) is None
    assert min_stack.push(-3) is None
    assert min_stack.getMin() == -3
    assert min_stack.pop() is None
    assert min_stack.top() == 0
    assert min_stack.getMin() == -2
