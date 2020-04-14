# 9613번 GCD합
import sys

# gcd
def gcd(a,b):
    while True:
        if a == 0:
            return b

        tmp = a
        a = b % a
        b = tmp

# main
T = int(input())

for _ in range(T):
    nums = [int(x) for x in sys.stdin.readline().split()]
    n = nums.pop(0)     # 맨 앞의 n을 pop
    nums.sort()     # a가 b보다 큰 경우를 막음

    # 가능한 최대공약수들
    sumOfGcd = 0
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            sumOfGcd += gcd(nums[i],nums[j])

    print(sumOfGcd)
    