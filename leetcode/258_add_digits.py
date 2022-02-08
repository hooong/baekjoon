# class Solution:
#     def addDigits(self, num: int) -> int:
#         while num // 10 > 0:
#             tmp = 0
#             for i in str(num):
#                 tmp += int(i)
#             num = tmp
#         return num


class Solution:
    def addDigits(self, num: int) -> int:
        answer = 0

        if num == 0:
            answer = 0
        elif num % 9 == 0:
            answer = 9
        else:
            answer = num % 9

        return answer


def test():
    solution = Solution()

    assert solution.addDigits(38) == 2
    assert solution.addDigits(0) == 0
