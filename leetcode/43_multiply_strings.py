class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        answer = ['0'] * (len(num1) + len(num2))

        re_num1 = num1[::-1]
        re_num2 = num2[::-1]

        carry = 0
        for i, n2 in enumerate(re_num2):
            carry = 0
            for j, n1 in enumerate(re_num1):
                tmp_1 = int(n1) * int(n2)
                num = tmp_1 % 10

                tmp_2 = num + carry + int(answer[i+j])
                answer[i+j] = str(tmp_2 % 10)
                carry = (tmp_1 // 10) + (tmp_2 // 10)

                if j == len(re_num1) - 1:
                    answer[i+j+1] = str(int(answer[i+j+1]) + carry)

        if answer[-1] == '0':
            answer = answer[:-1]

        return ''.join(answer[::-1])


def test_case():
    solution = Solution()

    assert solution.multiply('2', '3') == '6'
    assert solution.multiply('123', '456') == '56088'
    assert solution.multiply('9', '99') == '891'
    assert solution.multiply('999', '999') == '998001'
