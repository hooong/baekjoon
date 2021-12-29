class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        head = root

        if not head:
            return head

        q = [head]
        level = 0
        while q:
            for i in range(2 ** level):
                cur = q.pop(0)

                if i == (2 ** level) - 1:
                    cur.next = None
                else:
                    cur.next = q[0]

                if cur.left:
                    q.append(cur.left)
                    q.append(cur.right)
            level += 1

        return root
