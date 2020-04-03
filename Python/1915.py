# 1915번 가장 큰 정사각형
import sys

# main
n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(sys.stdin.readline())

# 최대 한 변의 길이를 저장하는 배열
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
maxSide = 0
for y in range(n):
    for x in range(m):
        if board[y][x] == '1':
            # 대각선 위, 위, 왼쪽 중 최솟값에 + 1 저장.
            dp[y+1][x+1] = min(dp[y][x], min(dp[y+1][x], dp[y][x+1])) + 1
            maxSide = max(maxSide, dp[y+1][x+1])

print(maxSide ** 2)