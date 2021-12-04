from typing import List


# class Solution:
#     def maxScore(self, cardPoints: List[int], k: int) -> int:
#         def dfs(left, right, cnt):
#             if cnt == k:
#                 return max(cardPoints[left], cardPoints[right])
#
#             return max(cardPoints[left] + dfs(left + 1, right, cnt + 1),
#                        cardPoints[right] + dfs(left, right - 1, cnt + 1))
#         return dfs(0, len(cardPoints) - 1, 1)
#

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = len(cardPoints) - k

        total = sum(cardPoints[right:])
        max_score = total
        for _ in range(k):
            total += cardPoints[left] - cardPoints[right]
            max_score = max(max_score, total)
            left += 1
            right += 1
        return max_score


def test():
    solution = Solution()

    assert solution.maxScore(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3) == 12
    assert solution.maxScore(cardPoints=[2, 2, 2], k=2) == 4
    assert solution.maxScore(cardPoints=[9, 7, 7, 9, 7, 7, 9], k=7) == 55
    assert solution.maxScore(cardPoints=[1, 1000, 1], k=1) == 1
    assert solution.maxScore(cardPoints=[1, 79, 80, 1, 1, 1, 200, 1], k=3) == 202
