from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        class TrieNode:
            def __init__(self):
                self.zero = None
                self.one = None
                self.val = None

        root = TrieNode()
        for num in nums:
            cur = root
            for i in range(31, -1, -1):
                mask = 1 << i
                mask_num = num & mask

                if mask_num == 0:
                    if not cur.zero:
                        cur.zero = TrieNode()
                    cur = cur.zero
                else:
                    if not cur.one:
                        cur.one = TrieNode()
                    cur = cur.one
            cur.val = num

        answer = 0
        for num in nums:
            cur = root
            for i in range(31, -1, -1):
                mask = 1 << i
                mask_num = num & mask

                if mask_num == 0:
                    if cur.one:
                        cur = cur.one
                    else:
                        cur = cur.zero
                else:
                    if cur.zero:
                        cur = cur.zero
                    else:
                        cur = cur.one

            answer = max(answer, num ^ cur.val)

        return answer
