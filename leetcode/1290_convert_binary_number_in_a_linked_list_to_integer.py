# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from leetcode.data_structures.list_node import ListNode


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = ''

        while head:
            binary += str(head.val)
            head = head.next
        return int(binary, 2)
