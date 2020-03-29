# 10026번 적록색약
from collections import deque
import sys

# 영역 구분
def check(grid, visit, sep, x, y):
    q = deque()
    q.append([x,y])

    # 상하좌우 인접 가능
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visit[nx][ny] and grid[nx][ny] in sep:
                    visit[nx][ny] = True
                    q.append([nx,ny])

# main
n = int(input())

grid = []
for _ in range(n):
    grid.append(sys.stdin.readline())

# 각 방문여부를 저장
visit_blind = [[False for _ in range(n)] for _ in range(n)]
visit_normal = [[False for _ in range(n)] for _ in range(n)]

# 영역의 개수를 카운트
cnt_blind = 0
cnt_normal = 0

for i in range(n):
    for j in range(n):
        # 색약인 경우
        if not visit_blind[i][j]:
            visit_blind[i][j] = True
            cnt_blind += 1
            if grid[i][j] == 'B':
                check(grid, visit_blind, ['B'], i, j)
            else:   # 적록을 하나로 보기 위함
                check(grid, visit_blind, ['R', 'G'], i, j)

        # 색약이 아닌 경우
        if not visit_normal[i][j]:
            visit_normal[i][j] = True
            cnt_normal += 1
            check(grid, visit_normal, [grid[i][j]], i, j)

print(cnt_normal, cnt_blind)
