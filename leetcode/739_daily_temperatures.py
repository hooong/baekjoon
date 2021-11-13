from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        answer = [0] * len(temperatures)

        for cur_day, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                target_day = stack.pop()
                answer[target_day] = cur_day - target_day
            stack.append(cur_day)

        return answer


def test():
    solution = Solution()

    assert solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert solution.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert solution.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
