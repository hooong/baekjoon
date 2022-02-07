from collections import Counter


# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         hash_map = Counter(s)
#
#         for ch in t:
#             if ch in hash_map:
#                 hash_map[ch] -= 1
#                 if not hash_map[ch]:
#                     del(hash_map[ch])
#             else:
#                 return ch


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        answer = 0
        for ch in s:
            answer ^= ord(ch)
        for ch in t:
            answer ^= ord(ch)
        return chr(answer)


def test():
    solution = Solution()

    assert solution.findTheDifference('abcd', 'abcde') == 'e'
    assert solution.findTheDifference('', 'y') == 'y'
