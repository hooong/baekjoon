import copy
from typing import List


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()
        self.sum_candidate(candidates, [], 0, target, answer)
        return answer

    def sum_candidate(self, candidates, cur, idx, target, answer):
        if target < 0:
            return

        if target == 0:
            answer.append(cur)
            return

        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue

            if candidates[i] > target:
                break

            self.sum_candidate(candidates, cur + [candidates[i]], i + 1, target - candidates[i], answer)


def test_case():
    solution = Solution()

    assert solution.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8) == [[1, 1, 6], [1, 2, 5], [1, 7],
                                                                                     [2, 6]]
    assert solution.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5) == [[1, 2, 2], [5]]
