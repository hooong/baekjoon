class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.check(s) == self.check(t)

    def check(self, s):
        s = list(s)
        s_tmp = []
        while s:
            cur = s.pop(0)

            if cur == '#':
                if s_tmp:
                    try:
                        s_tmp.pop()
                    except:
                        pass
            else:
                s_tmp.append(cur)

        return s_tmp


def test():
    solution = Solution()

    assert solution.backspaceCompare(s="ab#c", t="ad#c") is True
    assert solution.backspaceCompare(s="ab##", t="c#d#") is True
    assert solution.backspaceCompare(s="a##c", t="#a#c") is True
    assert solution.backspaceCompare(s="a#c", t="b") is False
