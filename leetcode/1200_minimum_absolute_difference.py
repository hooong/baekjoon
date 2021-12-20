from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        min_dis = arr[-1] - arr[0]
        for i in range(len(arr) - 1):
            min_dis = min(min_dis, (arr[i+1] - arr[i]))

        answer = []
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] == min_dis:
                answer.append([arr[i], arr[i+1]])

        return answer


def test():
    solution = Solution()

    assert solution.minimumAbsDifference([4, 2, 1, 3]) == [[1, 2], [2, 3], [3, 4]]
    assert solution.minimumAbsDifference([1, 3, 6, 10, 15]) == [[1, 3]]
    assert solution.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]) == [[-14, -10], [19, 23], [23, 27]]
