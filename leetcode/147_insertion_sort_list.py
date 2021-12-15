# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from leetcode.data_structures.list_node import ListNode


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        before = dummy
        cur = head
        post = None

        while cur:
            post = cur.next

            while before.next and before.next.val < cur.val:
                before = before.next

            cur.next = before.next
            before.next = cur

            before = dummy
            cur = post

        return dummy.next
