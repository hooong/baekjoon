class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        def dp(d, target):
            if d == 0:
                return 0 if target > 0 else 1
            if (d, target) in memo:
                return memo[(d, target)]

            tmp = 0
            for i in range(max(0, target-f), target):
                tmp += dp(d-1, i)
            memo[(d, target)] = tmp
            return tmp
        return dp(d, target) % (10**9 + 7)


def test():
    solution = Solution()

    assert solution.numRollsToTarget(1, 6, 3) == 1
    assert solution.numRollsToTarget(2, 6, 7) == 6
    assert solution.numRollsToTarget(2, 5, 10) == 1
    assert solution.numRollsToTarget(1, 2, 3) == 0
    assert solution.numRollsToTarget(30, 30, 500) == 222616187
