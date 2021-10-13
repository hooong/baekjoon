from typing import Optional

from leetcode.data_structures.list_node import make_list_node, print_list_node, ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        return self.loop(head)

    def loop(self, cur):
        if not cur or not cur.next:
            return cur

        tmp = cur.next
        cur.next = self.loop(tmp.next)
        tmp.next = cur

        return tmp


def test_case():
    solution = Solution()

    head = make_list_node([1, 2, 3, 4])
    assert print_list_node(solution.swapPairs(head)) == [2, 1, 4, 3]

    head = make_list_node([])
    assert print_list_node(solution.swapPairs(head)) == []

    head = make_list_node([1])
    assert print_list_node(solution.swapPairs(head)) == [1]
