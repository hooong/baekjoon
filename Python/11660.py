# 11660번 구간 합 구하기 5

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
board.insert(0, [0] * n)

for i in range(1, n+1):
    for j in range(n):
        if j == 0:
            board[i][j] += board[i-1][n-1]
        else:
            board[i][j] += board[i][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    ans = board
