from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        max_val = max(arr)

        is_up = True
        for i in range(1, len(arr)):
            if i == len(arr) - 1:
                if is_up:
                    return False

            if is_up:
                if arr[i-1] >= arr[i]:
                    return False
            else:
                if arr[i-1] <= arr[i]:
                    return False

            if max_val == arr[i]:
                is_up = False

        return True


def test():
    solution = Solution()

    assert solution.validMountainArray([2,1]) is False
    assert solution.validMountainArray([3,5,5]) is False
    assert solution.validMountainArray([0,3,2,1]) is True
    assert solution.validMountainArray([1,1,1,1]) is False
    assert solution.validMountainArray([0, 1,3,2,4]) is False
    assert solution.validMountainArray([2]) is False
    assert solution.validMountainArray([0,1,2,3,4]) is False
