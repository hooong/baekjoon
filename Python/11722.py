# 11722번 가장 긴 감소하는 부분 수열
import sys

#main
n = int(input())
arr = [int(x) for x in sys.stdin.readline().split()]

dp = [1] * n

if n == 1:
    print(1)
else:
    for i in range(1,n):
        for j in range(i+1):
            if arr[i] < arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    print(max(dp))
