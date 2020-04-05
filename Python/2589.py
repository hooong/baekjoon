# 2589번 보물섬
from collections import deque
import sys

# bfs
def bfs(x, y):
    global h, w, board, maxLen

    visited = [[-1 for _ in range(w)] for _ in range(h)]
    visited[y][x] = 0

    q = deque()
    q.append([x,y])

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    while q:
        x, y = q.popleft()
        maxLen = max(maxLen, visited[y][x])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < w and 0 <= ny < h:
                if visited[ny][nx] == -1 and board[ny][nx] == 'L':
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([nx,ny])

# main
h, w = [int(x) for x in sys.stdin.readline().split()]

board = []
lands = []
for y in range(h):
    row = sys.stdin.readline()
    board.append(row)
    for x in range(w):
        if row[x] == 'L':
            lands.append([x,y])
    
maxLen = 0
for land in lands:
    bfs(land[0], land[1])

print(maxLen)
