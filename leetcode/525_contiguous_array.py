from collections import Counter
from copy import deepcopy
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        answer = 0

        cnt = 0
        hash_map = {0: -1}
        for i, num in enumerate(nums):
            if num == 0:
                cnt -= 1
            else:
                cnt += 1

            if cnt not in hash_map:
                hash_map[cnt] = i
            else:
                answer = max(answer, i - hash_map[cnt])

        return answer


def test():
    solution = Solution()

    assert solution.findMaxLength([0, 1]) == 2
    assert solution.findMaxLength([0, 1, 0]) == 2
    assert solution.findMaxLength([0, 0, 0, 1, 1]) == 4
    assert solution.findMaxLength([0, 1, 1, 0, 1, 1, 1, 0]) == 4
