from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0] * len(prices)

        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            profit[i] = profit[i-1] + diff if diff > 0 else profit[i - 1]

        return profit[-1]


def test():
    solution = Solution()

    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert solution.maxProfit([1, 2, 3, 4, 5]) == 4
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
