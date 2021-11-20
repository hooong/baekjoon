import re


class Solution:
    def countValidWords(self, sentence: str) -> int:
        tokens = sentence.split(' ')

        count = 0
        for token in tokens:
            if not token:
                continue

            if not re.match(r'[a-z]?([a-z]+-?[a-z]+)?[!,.]?$', token):
                continue

            print(token)
            count += 1

        return count


def test():
    solution = Solution()

    assert solution.countValidWords("a") == 1
    assert solution.countValidWords("cat and  dog") == 3
    assert solution.countValidWords("!this  1-s b8d!") == 0
    assert solution.countValidWords("alice and  bob are playing stone-game10") == 5
    assert solution.countValidWords("he bought 2 pencils, 3 erasers, and 1  pencil-sharpener.") == 6
    assert solution.countValidWords("a-b-c") == 0
    assert solution.countValidWords('!') == 1
    assert solution.countValidWords(". ! 7hk  al6 l! aon49esj35la k3 7u2tkh  7i9y5  !jyylhppd et v- h!ogsouv 5") == 4
