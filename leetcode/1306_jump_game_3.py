from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visit = [False for _ in range(len(arr))]

        def dfs(cur):
            visit[cur] = True

            if arr[cur] == 0:
                return True

            b = cur - arr[cur]
            f = cur + arr[cur]

            b_result = False
            f_result = False
            if 0 <= b < len(arr) and not visit[b]:
                b_result = dfs(b)

            if 0 <= f < len(arr) and not visit[f]:
                f_result = dfs(f)

            return b_result or f_result

        return dfs(start)


def test():
    solution = Solution()

    assert solution.canReach([4, 2, 3, 0, 3, 1, 2], 5) is True
    assert solution.canReach([4, 2, 3, 0, 3, 1, 2], 0) is True
    assert solution.canReach([3, 0, 2, 1, 2], 2) is False
