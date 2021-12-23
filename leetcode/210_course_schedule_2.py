from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prerequisite_map = [[] for _ in range(numCourses)]

        in_degree = [0 for _ in range(numCourses)]
        for prerequisite in prerequisites:
            first, second = prerequisite[1], prerequisite[0]
            prerequisite_map[first].append(second)
            in_degree[second] += 1

        q = []
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)

        answer = []
        while q:
            cur = q.pop(0)

            answer.append(cur)
            for pre in prerequisite_map[cur]:
                in_degree[pre] -= 1
                if in_degree[pre] == 0:
                    q.append(pre)

        if not len(answer) == numCourses:
            return []
        return answer


def test():
    solution = Solution()

    assert solution.findOrder(2, [[1, 0]]) == [0, 1]
