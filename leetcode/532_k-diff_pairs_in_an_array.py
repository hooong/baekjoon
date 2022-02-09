from collections import Counter
from typing import List


# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         if len(nums) == 1:
#             return 0
#
#         nums.sort()
#
#         answer = []
#         left = 0
#         right = 1
#         while left < right < len(nums):
#             diff = nums[right] - nums[left]
#             if diff == k:
#                 tmp = (nums[left], nums[right])
#                 if tmp not in answer:
#                     answer.append(tmp)
#                 right += 1
#             elif diff < k:
#                 right += 1
#             else:
#                 left += 1
#
#                 if left == right and right < len(nums):
#                     right += 1
#
#         return len(answer)


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hash_table = Counter(nums)

        cnt = 0
        for x in hash_table:
            if k > 0 and (x+k) in hash_table:
                cnt += 1
            elif k == 0 and hash_table[x] > 1:
                cnt += 1
        return cnt


def test():
    solution = Solution()

    assert solution.findPairs([1], 0) == 0
    assert solution.findPairs([3, 1, 4, 1, 5], 2) == 2
    assert solution.findPairs([1, 2, 3, 4, 5], 1) == 4
    assert solution.findPairs([1, 3, 1, 5, 4], 0) == 1
    assert solution.findPairs([1, 1, 1, 2, 2], 0) == 2
