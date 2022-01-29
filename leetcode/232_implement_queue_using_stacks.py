class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyQueue:

    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.size = 0

    def push(self, x: int) -> None:
        new_node = Node(x)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def pop(self) -> int:
        pop_node = self.head.next
        if self.tail == pop_node:
            self.tail = self.head
        self.head.next = pop_node.next
        self.size -= 1
        return pop_node.val

    def peek(self) -> int:
        return self.head.next.val

    def empty(self) -> bool:
        return self.size == 0


def test():
    queue = MyQueue()

    queue.push(1)
    queue.push(2)
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert queue.empty() is False

