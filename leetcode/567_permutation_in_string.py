from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target_dict = Counter(s1)

        cur_dict = {}
        left = 0
        right = left + len(s1)

        for i in range(right):
            ch = s2[i]
            if ch not in cur_dict:
                cur_dict[ch] = 0
            cur_dict[ch] += 1

        while right < len(s2):
            if cur_dict == target_dict:
                return True

            cur_dict[s2[left]] -= 1
            if cur_dict[s2[left]] == 0:
                del (cur_dict[s2[left]])
            left += 1

            if s2[right] not in cur_dict:
                cur_dict[s2[right]] = 0
            cur_dict[s2[right]] += 1
            right += 1

        return cur_dict == target_dict


def test():
    solution = Solution()

    assert solution.checkInclusion(s1="ab", s2="eidbaooo") is True
    assert solution.checkInclusion(s1="ab", s2="eidboaoo") is False
    assert solution.checkInclusion(s1='ab', s2='aaccaaccab') is True
    assert solution.checkInclusion(s1='ab', s2='a') is False
