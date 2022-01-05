from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []

        def is_palindrome(target):
            return target == target[::-1]

        def dfs(start, cur):
            if start == len(s):
                answer.append(cur.copy())
                return

            for i in range(start, len(s)):
                target = s[start:i + 1]
                if is_palindrome(target):
                    cur.append(target)
                    dfs(i+1, cur)
                    cur.pop()

        dfs(0, [])
        return answer


def test():
    solution = Solution()

    assert solution.partition('aab') == [['a', 'a', 'b'], ['aa', 'b']]
    assert solution.partition('a') == [['a']]
