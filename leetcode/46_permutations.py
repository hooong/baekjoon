import itertools
from typing import List


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         answer = []
#         for i in itertools.permutations(nums, len(nums)):
#             answer.append(list(i))
#
#         return answer


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def dfs(cur: list, visited):
            if len(cur) == len(nums):
                answer.append(cur)

            for i, num in enumerate(nums):
                if not visited[i]:
                    visited[i] = True
                    dfs(cur+[num], visited)
                    visited[i] = False

        visited = [False for _ in range(len(nums))]
        dfs([], visited)

        return answer


def test():
    solution = Solution()

    assert solution.permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert solution.permute([0, 1]) == [[0, 1], [1, 0]]
    assert solution.permute([1]) == [[1]]
