class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 5

        dp1 = 1
        dp2 = 2
        dp3 = 5

        for i in range(4, n+1):
            dp4 = (2 * dp3 + dp1) % (10 ** 9 + 7)
            dp1 = dp2
            dp2 = dp3
            dp3 = dp4

        return dp3


def test():
    solution = Solution()

    assert solution.numTilings(3) == 5
    assert solution.numTilings(1) == 1
    assert solution.numTilings(4) == 11
    assert solution.numTilings(5) == 24
