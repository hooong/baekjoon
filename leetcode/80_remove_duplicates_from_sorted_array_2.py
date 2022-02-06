from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        total_cnt = len(nums)

        before_num = nums[0]
        cur_cnt = 1
        for i in range(1, len(nums)):
            if before_num == nums[i]:
                cur_cnt += 1
                if cur_cnt > 2:
                    total_cnt -= 1
                    nums[i] = 10**5
            else:
                before_num = nums[i]
                cur_cnt = 1

        nums.sort()
        return total_cnt

