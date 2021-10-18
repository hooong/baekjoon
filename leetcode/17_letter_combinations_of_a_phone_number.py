from typing import List


class Solution:
    letter_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits: str) -> List[str]:
        answer = []

        if not digits:
            return answer

        answer.extend(self.dfs(list(digits), ''))
        return answer

    def dfs(self, digits: list, cur: str):
        if not digits:
            return [cur]

        tmp = []
        for ch in self.letter_map[digits[0]]:
            if len(digits) == 1:
                tmp.extend(self.dfs([], cur + ch))
            else:
                tmp.extend(self.dfs(digits[1:], cur + ch))

        return tmp


def test_case():
    solution = Solution()

    assert solution.letterCombinations('23') == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert solution.letterCombinations('') == []
    assert solution.letterCombinations('2') == ["a", "b", "c"]
