# 11404번 플로이드
from sys import stdin, maxsize
INF = maxsize

n = int(stdin.readline())
m = int(stdin.readline())

board = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    board[i][i] = 0

for _ in range(m):
    i, j, c = map(int, stdin.readline().split())

    board[i][j] = min(board[i][j], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if board[i][j] == INF:
            print(0, end=' ')
        else:
            print(board[i][j], end=' ')
    print()
