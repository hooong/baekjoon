from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if not total % 2 == 0:
            return False

        target = total // 2
        dp = [False for _ in range(target + 1)]
        dp[0] = True

        for i in range(1, len(nums) + 1):
            for j in range(target, -1, -1):
                if j - nums[i-1] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i-1]]

        return dp[target]


def test():
    solution = Solution()

    assert solution.canPartition([1, 5, 11, 5]) is True
    assert solution.canPartition([1, 2, 3, 5]) is False
