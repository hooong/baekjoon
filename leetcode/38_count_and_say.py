class Solution:
    def countAndSay(self, n: int) -> str:
        answer = [0, '1']

        for i in range(2, n+1):
            before = answer[i-1]
            answer.append(self.count(list(before)))

        return answer[n]

    def count(self, s: list):
        if len(s) == 1:
            return f'1{s[0]}'

        before = s.pop(0)

        tmp = ''
        cnt = 1
        while s:
            cur = s.pop(0)
            if before == cur:
                cnt += 1
            else:
                tmp += f'{cnt}{before}'
                cnt = 1
            before = cur

        if cnt:
            tmp += f'{cnt}{before}'

        return tmp


def test_case():
    solution = Solution()

    assert solution.countAndSay(1) == '1'
    assert solution.countAndSay(4) == '1211'
    assert solution.countAndSay(5) == '111221'
