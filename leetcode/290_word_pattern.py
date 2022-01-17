class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')

        if not len(s) == len(pattern):
            return False

        tmp = {}
        for i in range(len(pattern)):
            x = pattern[i]
            if x in tmp:
                if not tmp[x] == s[i]:
                    return False
            else:
                tmp[x] = s[i]

        if len(tmp) == len(set(tmp.values())):
            return True
        return False


def test():
    solution = Solution()

    assert solution.wordPattern(pattern="abba", s="dog cat cat dog") is True
    assert solution.wordPattern(pattern="abba", s="dog cat cat fish") is False
    assert solution.wordPattern(pattern="aaaa", s="dog cat cat dog") is False
    assert solution.wordPattern(pattern="abba", s="dog dog dog dog") is False
    assert solution.wordPattern(pattern='aaa', s='aa aa aa aa') is False

