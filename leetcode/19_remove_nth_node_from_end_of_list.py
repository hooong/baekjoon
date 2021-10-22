import copy
from typing import Optional

from leetcode.data_structures.list_node import ListNode, make_list_node, print_list_node


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_size = self.get_size_of_linked_list(copy.deepcopy(head))
        front_n = list_size - n

        hhead = ListNode(next=head)

        if front_n == 0:
            return head.next

        for i in range(front_n - 1):
            head = head.next

        if n == 1:
            head.next = None
        else:
            head.next = head.next.next

        return hhead.next

    def get_size_of_linked_list(self, head):
        cnt = 0
        while head:
            head = head.next
            cnt += 1
        return cnt


def test_case():
    solution = Solution()

    assert print_list_node(solution.removeNthFromEnd(make_list_node([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert print_list_node(solution.removeNthFromEnd(make_list_node([1]), 1)) == []
    assert print_list_node(solution.removeNthFromEnd(make_list_node([1, 2]), 1)) == [1]
