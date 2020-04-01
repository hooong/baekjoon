# 1890번 점프
import sys

# 경로의 수 계산
def solve():
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(n):
            for k in range(i):
                if i - k == board[k][j]:
                    dp[i][j] += dp[k][j]
            for k in range(j):
                if j - k == board[i][k]:
                    dp[i][j] += dp[i][k]
    return dp[n-1][n-1]

# main
n = int(input())

board = []
for _ in range(n):
    board.append([int(x) for x in sys.stdin.readline().split()])

print(solve())

