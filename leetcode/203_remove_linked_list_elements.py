# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from leetcode.data_structures.list_node import ListNode, make_list_node, print_list_node


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        hhead = ListNode(next=head)

        before = hhead
        cur = before.next
        while cur:
            if cur.val == val:
                before.next = cur.next
            else:
                before = cur
            cur = cur.next

        return hhead.next


def test():
    solution = Solution()

    assert print_list_node(solution.removeElements(make_list_node([1, 2, 6, 3, 4, 5, 6]), 6)) == [1, 2, 3, 4, 5]
    assert print_list_node(solution.removeElements(make_list_node([]), 1)) == []
    assert print_list_node(solution.removeElements(make_list_node([7, 7, 7, 7]), 7)) == []
