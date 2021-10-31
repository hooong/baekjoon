"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head:
            head, tail = self.link_child(head)
        return head

    def link_child(self, cur):
        head = cur

        while True:
            if cur.child:
                tmp = cur.next

                cur.next, tail = self.link_child(cur.child)
                cur.next.prev = cur

                tail.next = tmp
                if tmp:
                    tmp.prev = tail

                cur.child = None

            if cur.next:
                cur = cur.next
            else:
                break

        return head, cur
