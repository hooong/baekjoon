from typing import List


# class Solution:
#     def maxDistToClosest(self, seats: List[int]) -> int:
#         N = len(seats)
#         left = [N for _ in range(N)]
#         right = [N for _ in range(N)]
#
#         for i in range(0, N):
#             if seats[i] == 1:
#                 left[i] = 0
#             else:
#                 if 0 < i:
#                     left[i] = left[i-1] + 1
#
#         for i in range(N-1, -1, -1):
#             if seats[i] == 1:
#                 right[i] = 0
#             else:
#                 if i < N-1:
#                     right[i] = right[i+1] + 1
#
#         answer = 0
#         for i in range(N):
#             answer = max(answer, min(left[i], right[i]))
#
#         return answer

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        N = len(seats)
        prev = -1
        future = 0
        answer = 0

        for i in range(N):
            if seats[i] == 1:
                prev = i
            else:
                while future < N and seats[future] == 0 or future < i:
                    future += 1

                left = i - prev if not prev == -1 else N
                right = future - i if not future == N else N
                answer = max(answer, min(left, right))
        return answer


def test():
    solution = Solution()

    assert solution.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]) == 2
    assert solution.maxDistToClosest([1, 0, 0, 0]) == 3
    assert solution.maxDistToClosest([0, 1]) == 1
