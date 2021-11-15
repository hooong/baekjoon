from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[] for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i].append(nums[i])
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)


def test():
    solution = Solution()

    assert solution.largestDivisibleSubset([1, 2, 3]) in ([1, 2], [1, 3])
    assert solution.largestDivisibleSubset([1, 2, 4, 8]) == [1, 2, 4, 8]
    assert solution.largestDivisibleSubset([4, 8, 10, 240]) == [4, 8, 240]
