from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []

        for i in range(n+1):
            binary = format(i, 'b')
            answer.append(binary.count('1'))

        return answer


def test():
    solution = Solution()

    assert solution.countBits(2) == [0, 1, 1]
    assert solution.countBits(5) == [0, 1, 1, 2, 1, 2]
