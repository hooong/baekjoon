# 11055번 가장 큰 증가 부분 수열
import sys

# main
n = int(input())
arr = [int(x) for x in sys.stdin.readline().split()]

dp = [0] * n

dp[0] = arr[0]
for i in range(1,n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j], dp[j] + arr[i])
        else:
            dp[j]
print(max(dp))