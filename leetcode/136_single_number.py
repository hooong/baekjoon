from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        exceed_single = []
        single_candidates = []

        for num in nums:
            if num in single_candidates:
                exceed_single.append(num)
                single_candidates.remove(num)

            if num in exceed_single:
                continue
            else:
                single_candidates.append(num)

        return single_candidates[0]


def test_case():
    solution = Solution()

    assert solution.singleNumber([2, 2, 1]) == 1
    assert solution.singleNumber([4, 1, 2, 1, 2]) == 4
    assert solution.singleNumber([1]) == 1
