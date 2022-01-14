from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        memo = [[[None] * n for _ in range(n)] for _ in range(n)]

        def dfs(r1, c1, c2):
            r2 = r1 + c1 - c2

            if r1 == n or r2 == n or c1 == n or c2 == n \
                    or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            elif r1 == c1 == n - 1:
                return grid[r1][c1]
            elif memo[r1][c1][c2]:
                return memo[r1][c1][c2]
            else:
                tmp = grid[r1][c1]
                if c1 != c2:
                    tmp += grid[r2][c2]

                tmp += max(dfs(r1, c1 + 1, c2), dfs(r1, c1 + 1, c2 + 1), dfs(r1 + 1, c1, c2),
                           dfs(r1 + 1, c1, c2 + 1))

            memo[r1][c1][c2] = tmp
            return tmp

        return max(0, dfs(0, 0, 0))


def test():
    solution = Solution()

    assert solution.cherryPickup(grid=[[0, 1, -1], [1, 0, -1], [1, 1, 1]]) == 5
    assert solution.cherryPickup(grid=[[1, 1, -1], [1, -1, 1], [-1, 1, 1]]) == 0
