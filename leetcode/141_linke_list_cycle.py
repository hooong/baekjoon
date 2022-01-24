# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import Optional

from leetcode.data_structures.list_node import ListNode


# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         cur = head
#
#         while cur:
#             if cur.val == float('-inf'):
#                 return True
#
#             cur.val = float('-inf')
#             cur = cur.next
#         return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
