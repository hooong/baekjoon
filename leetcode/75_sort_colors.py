import heapq
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums

        q = []
        while nums:
            cur = nums.pop()
            heapq.heappush(q, cur)

        while q:
            cur = heapq.heappop(q)
            nums.append(cur)

        return nums


def test_case():
    solution = Solution()

    assert solution.sortColors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]
    assert solution.sortColors([2, 0, 1]) == [0, 1, 2]
    assert solution.sortColors([0]) == [0]
    assert solution.sortColors([1]) == [1]
