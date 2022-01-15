from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        tmp = {}

        for i, num in enumerate(arr):
            if num in tmp.keys():
                tmp[num].append(i)
            else:
                tmp[num] = [i]

        q = [[0, 0]]
        visited = [False for _ in range(len(arr))]
        visited[0] = True
        while q:
            cur_node, cnt = q.pop(0)

            if cur_node == len(arr) - 1:
                return cnt

            for next_node in tmp[arr[cur_node]]:
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append([next_node, cnt + 1])

            tmp[arr[cur_node]] = []

            for i in [cur_node - 1, cur_node + 1]:
                if 0 <= i < len(arr) and not visited[i]:
                    visited[i] = True
                    q.append([i, cnt + 1])
        return -1


def test():
    solution = Solution()

    assert solution.minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]) == 3
    assert solution.minJumps([7]) == 0
    assert solution.minJumps([7, 6, 9, 6, 9, 6, 9, 7]) == 1
