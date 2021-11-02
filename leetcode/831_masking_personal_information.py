class Solution:
    def maskPII(self, s: str) -> str:
        answer = ''

        if '@' in s:
            # email
            answer = self.masking_email(s)
        else:
            # phone number
            answer = self.masking_number(s)

        return answer

    def masking_email(self, s):
        s = s.lower()
        name, domain = s.split('@')
        name = f'{name[0]}*****{name[-1]}'

        return f'{name}@{domain}'

    def masking_number(self, s):
        sep_ch = '+-() '

        for ch in sep_ch:
            s = s.replace(ch, '')

        local_number = s[-4:]
        if len(s) == 10:
            return f'***-***-{local_number}'
        elif len(s) == 11:
            return f"+*-***-***-{local_number}"
        elif len(s) == 12:
            return f"+**-***-***-{local_number}"
        elif len(s) == 13:
            return f"+***-***-***-{local_number}"


def test_case():
    solution = Solution()

    assert solution.maskPII("LeetCode@LeetCode.com") == "l*****e@leetcode.com"
    assert solution.maskPII("AB@qq.com") == "a*****b@qq.com"
    assert solution.maskPII("1(234)567-890") == "***-***-7890"
    assert solution.maskPII("86-(10)12345678") == "+**-***-***-5678"
