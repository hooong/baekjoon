# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from typing import List, Optional

from leetcode.data_structures.list_node import ListNode, make_list_node, print_list_node


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(None)
        cur = head

        q = []

        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(q, (node.val, idx, node))

        while q:
            min_node = heapq.heappop(q)
            idx, cur.next = min_node[1], min_node[2]
            cur = cur.next

            if cur.next:
                heapq.heappush(q, (cur.next.val, idx, cur.next))
        return head.next


def test_case():
    solution = Solution()

    assert print_list_node(
        solution.mergeKLists([make_list_node([1, 4, 5]), make_list_node([1, 3, 4]), make_list_node([2, 6])])) == [1, 1,
                                                                                                                  2, 3,
                                                                                                                  4, 4,
                                                                                                                  5, 6]
    assert print_list_node(solution.mergeKLists([])) == []
    assert print_list_node(solution.mergeKLists([make_list_node([])])) == []
