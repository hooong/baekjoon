from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        answer = 0

        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            answer = max(answer, prices[i] - min_price)

        return answer


def test():
    solution = Solution()

    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
    assert solution.maxProfit([1]) == 0
