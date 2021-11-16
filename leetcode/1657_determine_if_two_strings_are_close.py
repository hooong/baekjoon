from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        w1_counter = list(Counter(word1).values())
        w2_counter = list(Counter(word2).values())

        for i in w1_counter:
            if i in w2_counter:
                w2_counter.remove(i)

        if w2_counter:
            return False
        return True


def test():
    solution = Solution()

    assert solution.closeStrings('abc', 'bca') is True
    assert solution.closeStrings('a', 'aa') is False
    assert solution.closeStrings('cabbba', 'abbccc') is True
    assert solution.closeStrings('cabbba', 'aabbss') is False
