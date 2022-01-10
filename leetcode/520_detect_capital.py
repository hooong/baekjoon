import re


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if re.match('^[A-Z]*$', word):
            return True

        if re.match('^[A-Z]?[a-z]*$', word):
            return True

        return False


def test():
    solution = Solution()

    assert solution.detectCapitalUse('USA') is True
    assert solution.detectCapitalUse('FlaG') is False
    assert solution.detectCapitalUse('Flag') is True
    assert solution.detectCapitalUse('leetcode') is True
