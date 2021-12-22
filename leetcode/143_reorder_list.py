# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from leetcode.data_structures.list_node import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Divide half
        fast, slow = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        mid = slow

        # Reverse second-half
        prev, cur = None, mid

        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        head_second = prev

        # reorder
        first, second = head, head_second

        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
