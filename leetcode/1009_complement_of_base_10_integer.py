class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return (2**len(str(format(n, 'b')))) - 1 - n


def test():
    solution = Solution()

    assert solution.bitwiseComplement(5) == 2
    assert solution.bitwiseComplement(7) == 0
    assert solution.bitwiseComplement(10) == 5
