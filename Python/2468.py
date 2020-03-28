# 2468번 안전 영역
from collections import deque
import sys

# bfs
def bfs(flood, x, y):
    q = deque()
    q.append([x,y])

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if flood[nx][ny] == 0:
                    flood[nx][ny] = 1
                    q.append([nx,ny])

# main
N = int(input())

map = []
max_h = 0
for _ in range(N):
    row = []
    for h in sys.stdin.readline().split():
        h = int(h)
        if h > max_h:
            max_h = h
        row.append(h)
    map.append(row)

safe = [1]      # 안전 영역의 개수 (아무곳도 잠기지 않은 경우 1 포함)
for f in range(1,max_h+1):
    flood = [[0 for _ in range(N)] for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if map[x][y] <= f:
                flood[x][y] = -1

    # 안전영역 개수 구하기
    count = 0
    for x in range(N):
        for y in range(N):
            if flood[x][y] == 0:
                flood[x][y] = 1
                bfs(flood, x, y)
                count += 1
    
    safe.append(count)

print(max(safe))
