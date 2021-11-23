class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k + 1
        self.queue = [0] * (k + 1)
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.front = (self.front + 1) % self.size
        self.queue[self.front] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.rear = (self.rear + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        index = (self.rear + 1) % self.size
        return self.queue[index]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        tmp = (self.front + 1) % self.size
        return tmp == self.rear


def test():
    obj = MyCircularQueue(3)
    assert obj.enQueue(1) is True
    assert obj.enQueue(2) is True
    assert obj.enQueue(3) is True
    assert obj.enQueue(4) is False
    assert obj.Rear() == 3
    assert obj.isFull() is True
    assert obj.deQueue() is True
    assert obj.enQueue(4) is True
    assert obj.Rear() == 4
