from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []

        if len(nums) < 4:
            return answer

        nums.sort()

        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                cur_sum = nums[i] + nums[j]

                l = j + 1
                r = len(nums) - 1
                while l < r:
                    tmp = nums[l] + nums[r]

                    if cur_sum + tmp == target:
                        if not [nums[i], nums[j], nums[l], nums[r]] in answer:
                            answer.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                    elif cur_sum + tmp > target:
                        r -= 1
                    else:
                        l += 1

        return answer


def test_case():
    solution = Solution()

    assert solution.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert solution.fourSum(nums=[2, 2, 2, 2, 2], target=8) == [[2, 2, 2, 2]]
