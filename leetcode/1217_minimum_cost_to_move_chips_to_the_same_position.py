from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd_cnt = 0
        even_cnt = 0

        for i in position:
            if i % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1

        return min(odd_cnt, even_cnt)


def test():
    solution = Solution()

    assert solution.minCostToMoveChips([1,2,3]) == 1
    assert solution.minCostToMoveChips([2,2,2,3,3]) == 2
    assert solution.minCostToMoveChips([1,1000000000]) == 1
