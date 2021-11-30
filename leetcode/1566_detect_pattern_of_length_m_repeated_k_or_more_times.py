from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m):
            pattern = arr[i:i + m]

            if pattern * k == arr[i:i+(m*k)]:
                return True
        return False


def test():
    solution = Solution()

    assert solution.containsPattern(arr=[1, 2, 4, 4, 4, 4], m=1, k=3) is True
    assert solution.containsPattern(arr=[1, 2, 1, 2, 1, 1, 1, 3], m=2, k=2) is True
    assert solution.containsPattern(arr=[1, 2, 1, 2, 1, 3], m=2, k=3) is False
    assert solution.containsPattern(arr=[1, 2, 3, 1, 2], m=2, k=2) is False
    assert solution.containsPattern(arr=[2, 2, 2, 2], m=2, k=3) is False
