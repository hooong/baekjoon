class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False

        binary_n = format(n, 'b')

        if binary_n.count('1') == 1:
            return True
        return False


def test():
    solution = Solution()

    assert solution.isPowerOfTwo(1) is True
    assert solution.isPowerOfTwo(16) is True
    assert solution.isPowerOfTwo(3) is False
