# 11055번 가장 큰 증가 부분 수열
import sys

# main
n = int(input())
arr = [int(x) for x in sys.stdin.readline().split()]

dp = [0] * n

dp[0] = arr[0]
if n == 1:
    print(dp[0])
else:
    for i in range(1,n):
        dp[i] = arr[i]
        for j in range(i+1):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + arr[i])
    print(max(dp))