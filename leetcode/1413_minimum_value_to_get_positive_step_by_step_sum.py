from itertools import accumulate
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        return -min(0, min(accumulate(nums))) + 1


def test():
    solution = Solution()

    assert solution.minStartValue([-3, 2, -3, 4, 2]) == 5
    assert solution.minStartValue([1, 2]) == 1
    assert solution.minStartValue([1, -2, -3]) == 5
    assert solution.minStartValue([2, 3, 5, -5, -1]) == 1
    assert solution.minStartValue([-5, -2, 4, 4, -2]) == 8
