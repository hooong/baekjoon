from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []

        if not nums:
            return []

        start = nums[0]
        before = start
        for i in range(1, len(nums)):
            cur = nums[i]

            if before + 1 == cur:
                if i == len(nums) - 1:
                    answer.append(f'{start}->{cur}')
                else:
                    before = cur
                    continue
            else:
                if start == before:
                    answer.append(str(start))
                else:
                    answer.append(f'{start}->{before}')
                start = cur
                before = cur
        if start == nums[-1]:
            answer.append(str(nums[-1]))

        return answer


def test():
    solution = Solution()

    assert solution.summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert solution.summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
