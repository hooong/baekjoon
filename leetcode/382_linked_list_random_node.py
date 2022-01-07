# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import random
from typing import Optional

from leetcode.data_structures.list_node import ListNode


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = self.get_length_of_list(head)

    def getRandom(self) -> int:
        random_index = random.randrange(self.length)
        cur = self.head
        for i in range(random_index):
            cur = cur.next

        return cur.val

    def get_length_of_list(self, front):
        cnt = 0
        while front:
            cnt += 1
            front = front.next
        return cnt
