from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        # people[n] = [n이 믿는 사람의 수, n을 믿는 사람의 수]
        people = [0 for _ in range(n)]
        for t in trust:
            a = t[0] - 1
            b = t[1] - 1

            people[a] -= 1
            people[b] += 1

        for i, person in enumerate(people):
            if person == n - 1:
                return i + 1
        return -1


def test():
    solution = Solution()

    assert solution.findJudge(2, [[1, 2]]) == 2
    assert solution.findJudge(3, [[1, 3], [2, 3]]) == 3
    assert solution.findJudge(3, [[1, 3], [2, 3], [3, 1]]) == -1
