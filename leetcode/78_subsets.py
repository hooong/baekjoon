from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]

        def dfs(level, cur):
            nonlocal answer

            if level == len(nums):
                return

            answer.append(cur + [nums[level]])
            dfs(level + 1, cur + [nums[level]])
            dfs(level + 1, cur)

        dfs(0, [])
        return answer
