class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        count = 0

        while n >= i:
            count += 1

            n -= i
            i += 1

        return count


def test_case():
    solution = Solution()

    assert solution.arrangeCoins(5) == 2
    assert solution.arrangeCoins(8) == 3
    assert solution.arrangeCoins(10) == 4
    assert solution.arrangeCoins(7) == 3
