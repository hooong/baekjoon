from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        answer = []

        def dfs(target, cur):
            nonlocal answer

            if len(cur) == target:
                if low <= int(cur) <= high:
                    answer.append(int(cur))
                    return

            last_num = int(cur[-1])
            if last_num < 9:
                dfs(target, cur + str(last_num + 1))

        start_len = len(str(low))
        for i in range(start_len, 10):
            for j in range(1, 10):
                dfs(i, str(j))

        return answer


def test():
    solution = Solution()

    assert solution.sequentialDigits(100, 300) == [123, 234]
    assert solution.sequentialDigits(1000, 13000) == [1234,2345,3456,4567,5678,6789,12345]
    assert solution.sequentialDigits(58, 155) == [67,78,89,123]
