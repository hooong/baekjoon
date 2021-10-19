from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []

        i = 0
        j = 0
        while i < len(nums1) or j < len(nums2):
            if i == len(nums1):
                nums.append(nums2[j])
                j += 1
            elif j == len(nums2):
                nums.append(nums1[i])
                i += 1
            else:
                if nums1[i] <= nums2[j]:
                    nums.append(nums1[i])
                    i += 1
                else:
                    nums.append(nums2[j])
                    j += 1

        mid = len(nums) // 2
        if len(nums) % 2 == 0:
            answer = (nums[mid] + nums[mid-1]) / 2
        else:
            answer = nums[mid]

        return answer


def test_case():
    solution = Solution()

    assert solution.findMedianSortedArrays([1, 3], [2]) == 2.00000
    assert solution.findMedianSortedArrays([1, 2], [3, 4]) == 2.50000
    assert solution.findMedianSortedArrays([0, 0], [0, 0]) == 0.00000
    assert solution.findMedianSortedArrays([], [1]) == 1.00000
    assert solution.findMedianSortedArrays([2], []) == 2.00000
