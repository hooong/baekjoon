from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        answer = 1
        cur_pos = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > cur_pos:
                cur_pos = points[i][1]
                answer += 1
        return answer


def test():
    solution = Solution()

    assert solution.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert solution.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert solution.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
