from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        answer = 0

        for account in accounts:
            answer = max(answer, sum(account))

        return answer


def test():
    solution = Solution()

    assert solution.maximumWealth([[1, 2, 3], [3, 2, 1]]) == 6
    assert solution.maximumWealth([[1, 5], [7, 3], [3, 5]]) == 10
    assert solution.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17
