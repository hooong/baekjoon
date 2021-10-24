from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        return self.check(candidates, target, [], 0)

    def check(self, candidates, target, cur, idx):
        answer = []

        for i in range(idx, len(candidates)):
            cur_sum = sum(cur) + candidates[i]
            if cur_sum == target:
                answer.append(cur + [candidates[i]])
                break
            elif cur_sum > target:
                break
            else:
                tmp = self.check(candidates, target, cur + [candidates[i]], i)
                answer.extend(tmp)

        return answer


def test_case():
    solution = Solution()

    assert solution.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert solution.combinationSum([2], 1) == []
    assert solution.combinationSum([1], 1) == [[1]]
    assert solution.combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert solution.combinationSum([1], 2) == [[1, 1]]
