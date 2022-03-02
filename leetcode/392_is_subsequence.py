class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        if i >= len(s):
            return True
        return False


def test():
    solution = Solution()

    assert solution.isSubsequence('abc', "ahbgdc") is True
    assert solution.isSubsequence(s = "axc", t = "ahbgdc") is False
