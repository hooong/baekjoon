class Solution:
    def numTrees(self, n: int) -> int:
        mem = [0] * (n + 1)
        mem[0] = 1
        mem[1] = 1

        return self.count(n, mem)

    def count(self, n, mem):
        if mem[n]:
            return mem[n]

        tmp = 0
        for i in range(n):
            left, right = len(range(0, i)), len(range(i+1, n))
            tmp += self.count(left, mem) * self.count(right, mem)

        mem[n] = tmp
        return tmp


def test_case():
    solution = Solution()

    assert solution.numTrees(3) == 5
    assert solution.numTrees(1) == 1
    assert solution.numTrees(4) == 14
