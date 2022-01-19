class ListNode:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self._cache:
            node = self._cache[key]
            self.remove_node(node)
            self.insert_front(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            node = self._cache[key]
            self.remove_node(node)
            self.insert_front(node)
            node.val = value
        else:
            if len(self._cache) >= self._capacity:
                node_to_remove = self.remove_tail()
                self._cache.pop(node_to_remove.key)
            new_node = ListNode(key, value)
            self._cache[key] = new_node
            self.insert_front(new_node)
        return

    def remove_tail(self):
        last_node = self.tail.prev
        self.tail.prev = last_node.prev
        last_node.prev.next = self.tail
        return last_node

    def insert_front(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def remove_node(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev


def test():
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    cache = LRUCache(2)

    assert cache.get(2) == -1
    cache.put(2, 6)
    assert cache.get(1) == -1
    cache.put(1, 5)
    cache.put(1, 2)
    assert cache.get(1) == 2
    assert cache.get(2) == 6

    cache = LRUCache(2)

    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)
    assert cache.get(1) == -1
    assert cache.get(2) == 3
