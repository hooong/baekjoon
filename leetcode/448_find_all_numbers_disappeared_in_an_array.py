from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            i = abs(num) - 1
            nums[i] = -(abs(nums[i]))

        return [i + 1 for i, num in enumerate(nums) if num > 0]


def test():
    solution = Solution()

    assert solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert solution.findDisappearedNumbers([1, 1]) == [2]
