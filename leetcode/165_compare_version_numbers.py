class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')

        while version1 and version2:
            v1 = int(version1.pop(0))
            v2 = int(version2.pop(0))

            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        while version1:
            tmp = int(version1.pop(0))
            if tmp > 0:
                return 1
        while version2:
            tmp = int(version2.pop(0))
            if tmp > 0:
                return -1

        return 0


def test():
    solution = Solution()

    assert solution.compareVersion('1.01', '1.001') == 0
    assert solution.compareVersion('1.0', '1.0.0') == 0
    assert solution.compareVersion('0.1', '1.1') == -1
    assert solution.compareVersion('0.0.1', '0.0.1') == 0
    assert solution.compareVersion('0.001.1', '0.1.1') == 0
    assert solution.compareVersion('1.0', '1.0.1') == -1
    assert solution.compareVersion('1.0.1', '1') == 1
