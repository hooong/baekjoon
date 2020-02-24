# 11049번 행렬 곱셈 순서
import sys

# main
n = int(sys.stdin.readline())

marr = [[0,0]]
for _ in range(n):
    tmp = [int(x) for x in sys.stdin.readline().split()]
    marr.append(tmp)

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]


print(dp[1][n])
