from typing import Optional

from leetcode.data_structures.list_node import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        length = 0
        while cur:
            length += 1
            cur = cur.next

        mid = length // 2

        for _ in range(mid):
            head = head.next

        return head
