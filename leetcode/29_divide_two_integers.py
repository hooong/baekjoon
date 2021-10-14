class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = dividend / divisor

        answer = int(str(quotient).split('.')[0])

        if answer < -1 * (2 ** 31):
            answer = -1 * (2 ** 31)
        elif answer > (2 ** 31) - 1:
            answer = (2 ** 31) - 1

        return answer

def test_case():
    solution = Solution()

    assert solution.divide(10, 3) == 3

    assert solution.divide(7, -3) == -2

    assert solution.divide(0, 1) == 0

    assert solution.divide(1, 1) == 1

    assert solution.divide(-2147483648, -1) == 2147483647
