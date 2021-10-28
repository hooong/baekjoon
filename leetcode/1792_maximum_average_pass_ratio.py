from typing import List

import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        q = []
        for c in classes:
            change = self.calc_change(c[0], c[1])
            heapq.heappush(q, [-change, c[0], c[1]])

        for _ in range(extraStudents):
            cur = heapq.heappop(q)

            change = self.calc_change(cur[1] + 1, cur[2] + 1)
            heapq.heappush(q, [-change, cur[1] + 1, cur[2] + 1])

        tmp = 0
        while q:
            change, p, t = heapq.heappop(q)

            tmp += p / t

        answer = tmp / len(classes)
        return round(answer, 5)

    def calc_change(self, p, t):
        cur = p / t
        extra = (p + 1) / (t + 1)

        return extra - cur


def test_case():
    solution = Solution()

    assert solution.maxAverageRatio(classes=[[1, 2], [3, 5], [2, 2]], extraStudents=2) == 0.78333
    assert solution.maxAverageRatio(classes=[[2, 4], [3, 9], [4, 5], [2, 10]], extraStudents=4) == 0.53485
