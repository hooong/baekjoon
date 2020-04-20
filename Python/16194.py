# 16194번 카드 구매하기 2
import sys

# main
n = int(input())
p = [int(x) for x in sys.stdin.readline().split()]

dp = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    dp[i][0] = 0
    for j in range(1,n+1):
        if j >= i:
            dp[i][j] = min(dp[i-1][j], dp[i][j-i] + p[i-1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][n])
