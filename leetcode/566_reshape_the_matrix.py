from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if r * c != m * n:
            return mat

        answer = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(m * n):
            answer[i // c][i % c] = mat[i // n][i % n]
        return answer


def test():
    solution = Solution()

    assert solution.matrixReshape([[1, 2], [3, 4]], 1, 4) == [[1, 2, 3, 4]]
    assert solution.matrixReshape([[1, 2], [3, 4]], 2, 4) == [[1, 2], [3, 4]]
