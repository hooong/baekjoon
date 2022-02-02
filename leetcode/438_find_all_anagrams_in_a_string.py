from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []

        if len(s) < len(p):
            return []

        check_hash = {}
        cnt = 0
        for ch in p:
            cnt += 1
            if ch not in check_hash:
                check_hash[ch] = 0
            check_hash[ch] += 1

        left = 0
        right = 0
        tmp_hash = {}
        while right < len(p):
            ch = s[right]
            if ch not in tmp_hash:
                tmp_hash[ch] = 0
            tmp_hash[ch] += 1
            right += 1

        if check_hash == tmp_hash:
            answer.append(left)

        while left < len(s) - len(p):
            left_ch = s[left]

            tmp_hash[left_ch] -= 1
            if tmp_hash[left_ch] == 0:
                tmp_hash.pop(left_ch)
            left += 1

            right_ch = s[right]
            if right_ch not in tmp_hash:
                tmp_hash[right_ch] = 0
            tmp_hash[right_ch] += 1
            right += 1

            if check_hash == tmp_hash:
                answer.append(left)

        return answer


def test():
    solution = Solution()

    assert solution.findAnagrams('cbaebabacd', 'abc') == [0, 6]
    assert solution.findAnagrams('abab', 'ab') == [0, 1, 2]
    assert solution.findAnagrams('aaa', 'aaaaa') == []
