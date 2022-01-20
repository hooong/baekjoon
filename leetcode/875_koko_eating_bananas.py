from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k: int):
            count = 0

            for i in piles:
                count += (i // k) + (i % k != 0)

            if count <= h:
                return True
            return False

        start = 1
        end = max(piles)

        answer = float('inf')
        while start <= end:
            mid = (start + end) // 2

            if check(mid):
                end = mid - 1
                answer = min(answer, mid)
            else:
                start = mid + 1
        return answer


def test():
    solution = Solution()

    assert solution.minEatingSpeed([3,6,7,11], 8) == 4
    assert solution.minEatingSpeed([30,11,23,4,20], 5) == 30
    assert solution.minEatingSpeed([30,11,23,4,20], 6) == 23
