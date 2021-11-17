from collections import deque


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1

        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        dp[1][1] = 1

        for i in range(1, n+1):
            for j in range(1, m+1):
                if i == 1 and j == 1:
                    continue

                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[n][m]


def test():
    solution = Solution()

    assert solution.uniquePaths(3, 7) == 28
    assert solution.uniquePaths(3, 2) == 3
    assert solution.uniquePaths(7, 3) == 28
    assert solution.uniquePaths(3, 3) == 6
    assert solution.uniquePaths(1, 1) == 1
    assert solution.uniquePaths(23, 12) == 193536720
