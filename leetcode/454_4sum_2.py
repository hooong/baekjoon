from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hash_1 = {}
        hash_2 = {}

        n = len(nums1)
        for i in range(n):
            for j in range(n):
                a = nums1[i] + nums2[j]
                b = nums3[i] + nums4[j]

                if a not in hash_1:
                    hash_1[a] = 0
                hash_1[a] += 1

                if b not in hash_2:
                    hash_2[b] = 0
                hash_2[b] += 1

        answer = 0
        for k in hash_1:
            if -k in hash_2:
                answer += hash_1[k] * hash_2[-k]

        return answer


def test():
    solution = Solution()

    assert solution.fourSumCount(nums1=[1, 2], nums2=[-2, -1], nums3=[-1, 2], nums4=[0, 2]) == 2
    assert solution.fourSumCount(nums1=[0], nums2=[0], nums3=[0], nums4=[0]) == 1
    assert solution.fourSumCount([-1, 1, 1, 1, -1],
                                 [0, -1, -1, 0, 1],
                                 [-1, -1, 1, -1, -1],
                                 [0, 1, 0, -1, -1]) == 132
