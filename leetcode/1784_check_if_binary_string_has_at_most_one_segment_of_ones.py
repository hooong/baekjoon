class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        tmp = s.split('0')
        count = len(tmp) - tmp.count('')

        if count == 1:
            return True
        return False


def test():
    solution = Solution()

    assert solution.checkOnesSegment('1001') is False
    assert solution.checkOnesSegment('110') is True
