# 1915번 가장 큰 정사각형
import sys

# main
n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(sys.stdin.readline())

# 최대 한 변의 길이를 저장
width = [[1 for _ in range(m)] for _ in range(n)]

dx = [-1,0,-1]
dy = [0,-1,-1]
max_width = 1
for y in range(2,n):
    for x in range(2,m):
        isSquare = True

        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if board[ny][nx] != '1':
                isSquare = False
        
        if isSquare:
            width[y][x] = width[y-1][x-1] + 1

        max_width = max(max_width, width[y][x] ** 2)

print(max_width)
