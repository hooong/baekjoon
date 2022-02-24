# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from leetcode.data_structures.list_node import ListNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def _sortList(size, head):
            if size == 1:
                head.next = None
                return head

            mid = size // 2
            mid_node = head
            for _ in range(mid):
                mid_node = mid_node.next

            left = _sortList(mid, head)
            right = _sortList(size - mid, mid_node)

            tmp = ListNode()
            cur = tmp
            while left or right:
                if left and not right:
                    cur.next = left
                    left = left.next
                elif right and not left:
                    cur.next = right
                    right = right.next
                else:
                    if left.val < right.val:
                        cur.next = left
                        left = left.next
                    else:
                        cur.next = right
                        right = right.next
                cur = cur.next

            return tmp.next

        list_len = 0

        cur = head
        while cur:
            list_len += 1
            cur = cur.next

        if not list_len:
            return None
        return _sortList(list_len, head)
