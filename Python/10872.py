# 팩토리얼 재귀
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)

n = int(input())

print(factorial(n))
