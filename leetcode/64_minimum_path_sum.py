from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        len_row = len(grid)
        len_col = len(grid[0])

        dp = [[0 for _ in range(len_col)] for _ in range(len_row)]
        dp[0][0] = grid[0][0]

        for i in range(1, len_col):
            dp[0][i] = dp[0][i-1] + grid[0][i]

        for j in range(1, len_row):
            dp[j][0] = dp[j-1][0] + grid[j][0]

        for row in range(1, len_row):
            for col in range(1, len_col):
                dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + grid[row][col]

        return dp[len_row-1][len_col-1]


def test():
    solution = Solution()

    assert solution.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert solution.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12
