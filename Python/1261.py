# 1261번 알고스팟
from collections import deque
import sys

# main
m, n = map(int, input().split())

board = []
for _ in range(n):
    board.append(sys.stdin.readline())

# bfs
q = deque()
q.append([0,0,0])

# 방문여부
visited = [[float('inf') for _ in range(m)] for _ in range(n)]
visited[0][0] = 0

# 상하좌우
dy = [-1,0,1,0]
dx = [0,-1,0,1]

while q:
    y, x, cnt = q.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m:
            if visited[ny][nx] > cnt:
                visited[ny][nx] = cnt
                if board[ny][nx] == '1':
                    q.append([ny,nx,cnt+1])    
                else:                    
                    q.append([ny,nx,cnt])

print(visited[n-1][m-1])