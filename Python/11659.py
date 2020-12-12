# 11659번 구간 합 구하기 4
from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

dp = [0] * (n+1)
dp[1] = arr[0]
for i in range(1, n+1):
    dp[i] = dp[i-1] + arr[i-1]

for _ in range(m):
    i, j = map(int, stdin.readline().split())
    print(dp[j] - dp[i-1])
