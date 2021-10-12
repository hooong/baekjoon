from typing import List


class Solution:
    answer = None

    def generateParenthesis(self, n: int) -> List[str]:
        self.answer = []

        self.chaining_parenthesis(n, 0, 0, '')

        return self.answer

    def chaining_parenthesis(self, n, open, close, tmp):
        if open == n and close == n:
            self.answer.append(tmp)
            return
        elif open == n and close != n:
            self.chaining_parenthesis(n, open, close + 1, tmp + ')')
        elif open > close:
            self.chaining_parenthesis(n, open + 1, close, tmp + '(')
            self.chaining_parenthesis(n, open, close + 1, tmp + ')')
        elif open == close:
            self.chaining_parenthesis(n, open + 1, close, tmp + '(')


def test_case_1():
    solution = Solution()

    answer = solution.generateParenthesis(3)
    assert answer == ["((()))", "(()())", "(())()", "()(())", "()()()"]

    answer = solution.generateParenthesis(1)
    assert answer == ['()']
