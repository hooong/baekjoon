from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        answer = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            s = max(firstList[i][0], secondList[j][0])
            e = min(firstList[i][1], secondList[j][1])

            if s <= e:
                answer.append([s, e])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return answer


def test():
    solution = Solution()

    assert solution.intervalIntersection(firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
                                         secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]) == [[1, 2], [5, 5], [8, 10],
                                                                                               [15, 23], [24, 24],
                                                                                               [25, 25]]
    assert solution.intervalIntersection(firstList=[[1, 3], [5, 9]], secondList=[]) == []
    assert solution.intervalIntersection(firstList=[], secondList=[[4, 8], [10, 12]]) == []
    assert solution.intervalIntersection(firstList=[[1, 7]], secondList=[[3, 10]]) == [[3, 7]]
