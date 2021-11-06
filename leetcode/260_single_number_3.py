from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)

        answer = []
        for k, v in counter.items():
            if v == 1:
                answer.append(k)

            if len(answer) == 2:
                break

        return answer


def test_case():
    solution = Solution()

    assert solution.singleNumber([1, 2, 1, 3, 2, 5]) == [3, 5]
    assert solution.singleNumber([-1, 0]) == [-1, 0]
    assert solution.singleNumber([0, 1]) == [0, 1]
