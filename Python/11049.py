# 11049번 행렬 곱셈 순서
import sys

# main
n = int(sys.stdin.readline())

dim = [[0,0]]
for _ in range(n):
    tmp = [int(x) for x in sys.stdin.readline().split()]
    dim.append(tmp)

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for dia in range(n):
    for i in range(1, (n - dia) + 1):
        j = i + dia

        if i == j:
            continue
        
        dp[i][j] = 987654321
        for k in range(i,j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + (dim[i][0] * dim[k][1] * dim[j][1]))

print(dp[1][n])
