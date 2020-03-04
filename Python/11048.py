# 11048번 이동하기
import sys

# main
n, m = [int(x) for x in sys.stdin.readline().split()]

map = []
for _ in range(n):
    map.append([int(x) for x in sys.stdin.readline().split()])

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for r in range(1, n+1):
    for c in range(1, m+1):
        dp[r][c] = map[r-1][c-1] + max(dp[r-1][c-1], max(dp[r-1][c], dp[r][c-1]))

print(dp[n][m])
