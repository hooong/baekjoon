from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0: empty, 1: fresh, 2: rotten
        rows = len(grid)
        cols = len(grid[0])

        rotten = []

        # append fresh position
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))

        minuets = 0
        while self.count(grid, rotten):
            minuets += 1

        if not self.check_fresh(grid):
            return -1

        return minuets

    def count(self, grid, rotten):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        is_change = False
        for _ in range(len(rotten)):
            cur_y, cur_x = rotten.pop(0)

            for i in range(4):
                x = cur_x + dx[i]
                y = cur_y + dy[i]

                if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
                    if grid[y][x] == 1:
                        grid[y][x] = 2
                        rotten.append((y, x))
                        is_change = True

        return is_change

    def check_fresh(self, grid):
        for row in grid:
            for col in row:
                if col == 1:
                    return False
        return True


def test_case():
    solution = Solution()

    assert solution.orangesRotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert solution.orangesRotting(grid=[[0, 2]]) == 0
