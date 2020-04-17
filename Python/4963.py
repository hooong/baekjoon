# 4963번 섬의 개수
import sys
from collections import deque

# bfs
def bfs(y,x):
    global board, visited

    q = deque()
    q.append([y,x])

    dy = [-1,-1,-1,0,0,0,1,1,1]
    dx = [-1,0,1,-1,0,1,-1,0,1]
    while q:
        y, x = q.popleft()

        for i in range(9):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < h and 0 <= nx < w:
                if not visited[ny][nx] and board[ny][nx]:
                    visited[ny][nx] = True
                    q.append([ny,nx])

# main
while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    board = []
    for _ in range(h):
        board.append([int(x) for x in sys.stdin.readline().split()])
    
    visited = [[False for _ in range(w)] for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and board[i][j] == 1:
                visited[i][j] = True
                bfs(i,j)
                cnt += 1

    print(cnt)
