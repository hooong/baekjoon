from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        sum_front, sum_back = 0, sum(nums)
        result = []

        for i, num in enumerate(nums):
            sum_back -= num
            result.append(sum_back - (len(nums) - 1 - i) * num + i * num - sum_front)
            sum_front += num

        return result


def test():
    solution = Solution()

    assert solution.getSumAbsoluteDifferences([2, 3, 5]) == [4, 3, 5]
    assert solution.getSumAbsoluteDifferences([1, 4, 6, 8, 10]) == [24, 15, 13, 15, 21]
