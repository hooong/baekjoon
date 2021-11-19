from operator import xor


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return format(xor(x, y), 'b').count('1')


def test():
    solution = Solution()

    assert solution.hammingDistance(1, 4) == 2
    assert solution.hammingDistance(3, 1) == 1
