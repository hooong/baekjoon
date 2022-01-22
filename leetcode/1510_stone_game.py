from math import sqrt


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n + 1)]
        dp[1] = True

        for i in range(1, n + 1):
            max_sqrt = int(sqrt(i))

            for j in range(1, max_sqrt + 1):
                tmp = i - j ** 2
                dp[i] = dp[i] or (not dp[tmp])

                if dp[i]:
                    break

        return dp[n]


def test():
    solution = Solution()

    assert solution.winnerSquareGame(1) is True
    assert solution.winnerSquareGame(2) is False
    assert solution.winnerSquareGame(4) is True
    assert solution.winnerSquareGame(8) is True
    assert solution.winnerSquareGame(9) is True
    assert solution.winnerSquareGame(15) is False
