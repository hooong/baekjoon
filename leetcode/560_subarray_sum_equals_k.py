from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_table = {0: 1}

        cur_sum = 0
        cnt = 0
        for num in nums:
            cur_sum += num

            tmp = cur_sum - k
            if tmp in hash_table:
                cnt += hash_table[tmp]

            if cur_sum in hash_table:
                hash_table[cur_sum] += 1
            else:
                hash_table[cur_sum] = 1

        return cnt


def test():
    solution = Solution()

    assert solution.subarraySum([1, 1, 1], 2) == 2
    assert solution.subarraySum([1, 2, 3], 3) == 2
