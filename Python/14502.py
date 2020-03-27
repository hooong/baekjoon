# 14502번 연구소
from collections import deque
import sys, copy

# 바이러스 전파 bfs
def virus(n, m, map):
    global safe

    b_map = copy.deepcopy(map)
    visit  = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    
    for i in range(n):
        for j in range(m):
            if b_map[i][j] == 2:
                visit[i][j] = True
                q.append([i,j])

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    while q:
        tmp = q.popleft()
        x = tmp[0]
        y = tmp[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visit[nx][ny] and b_map[nx][ny] == 0:
                    visit[nx][ny] = True
                    b_map[nx][ny] = 2
                    q.append([nx,ny])
    
    s_count = 0
    for tmp in b_map:
        s_count += tmp.count(0)
    
    safe.append(s_count)

# 벽 세우기 dfs
def wall(n, m, w_map, w_count):
    if w_count == 3:
        virus(n,m,w_map)
        return 

    for i in range(n):
        for j in range(m):
            if w_map[i][j] == 0:
                w_map[i][j] = 1
                wall(n,m,w_map,w_count+1)
                w_map[i][j] = 0

# main
n, m = [int(x) for x in sys.stdin.readline().split()]

map = []
for _ in range(n):
    map.append([int(x) for x in sys.stdin.readline().split()])

safe = []

wall(n,m,map,0)

print(max(safe))