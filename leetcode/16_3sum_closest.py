from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = sum(nums[:3])

        for i in range(len(nums) - 2):
            cur = nums[i]

            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_sum = cur + nums[left] + nums[right]

                if three_sum == target:
                    return target
                elif target - three_sum < 0:
                    right -= 1
                else:
                    left += 1

                if abs(target - answer) > abs(target - three_sum):
                    answer = three_sum

        return answer


def test_cases():
    solution = Solution()

    assert solution.threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert solution.threeSumClosest([0, 0, 0], 1) == 0
    assert solution.threeSumClosest([0, 2, 1, -3], 1) == 0
