from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []

        if len(nums) < 3:
            return answer

        for i in range(len(nums) - 2):
            cur = nums[i]

            if i > 0 and cur == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                two_sum = nums[l] + nums[r]
                if two_sum == -cur:
                    tmp = [cur, nums[l], nums[r]]

                    if tmp not in answer:
                        answer.append(tmp)

                    l += 1
                    r -= 1
                elif two_sum > -cur:
                    r -= 1
                else:
                    l += 1

        return answer


def test_cases():
    solution = Solution()

    # case1
    assert solution.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]

    # case2
    assert solution.threeSum([]) == []

    # case3
    assert solution.threeSum([0]) == []

    # case4
    assert solution.threeSum([1, -1, -1, 0]) == [[-1, 0, 1]]
