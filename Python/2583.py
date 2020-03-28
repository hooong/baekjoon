# 2583번 영역 구하기
from collections import deque
import sys

# bfs
def bfs(map, x, y, s):
    global width

    q = deque()
    q.append([x,y])

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    w = 1           # 영역의 넓이를 저장
    while q:
        pos = q.popleft()
        x = pos[0]
        y = pos[1]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if map[ny][nx] == 0:
                    map[ny][nx] = s
                    q.append([nx,ny])
                    w += 1
    
    width.append(w)

# main
# -1 : 경계, 0 : 빈공간, 1~n : 영역
m, n, k = [int(x) for x in sys.stdin.readline().split()]

# m - y축, n - x축
map = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    # x축이 m까지 y축이 n까지
    x1, y1, x2, y2 = [int(x) for x in sys.stdin.readline().split()]

    # map에 경계 설치
    for x in range(x1,x2):
        for y in range(m-y2,m-y1):
            map[y][x] = -1

width = []      # 모든 영역의 넓이를 담을 배열
site = 0        # 영역의 번호
for i in range(m):
    for j in range(n):
        if map[i][j] == 0:
            map[i][j] = site+1
            bfs(map,j,i,site+1)

width.sort()
# 출력
print(len(width))
for i in width:
    print(i, end=' ')
print()
