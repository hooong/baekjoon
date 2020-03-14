# 2206번 벽 부수고 이동하기
import sys
from collections import deque

# BFS
def bfs():
    q = deque()
    q.append([0,0,0])
    visit[0][0][0] = 1

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    while q:
        tmp = q.popleft()
        x = tmp[0]
        y = tmp[1]
        wall = tmp[2]

        if x == n-1 and y == m-1:
            return visit[wall][x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visit[wall][nx][ny] == 0:
                    # 벽이 부서지든 안부서지든 0이면 확인해야함.
                    if map[nx][ny] == '0':
                        visit[wall][nx][ny] = visit[wall][x][y] + 1
                        q.append([nx,ny,wall])
                    # 벽이 부서지지 않은 상황에서 벽을 마주한다면 벽을 부순 상황으로 전환
                    elif map[nx][ny] == '1' and wall == 0:
                        visit[1][nx][ny] = visit[wall][x][y] + 1
                        q.append([nx,ny,1])

# main
n, m = [int(x) for x in sys.stdin.readline().split()]

map = []
for _ in range(n):
    map.append(list(sys.stdin.readline()))

# 벽을 부순 경우, 부수지 않은 경우를 모두 확인해야함.
visit = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]

answer = bfs()
if answer == None:  # 끝까지 가지 못하면 return값이 없음.
    print(-1)
else:
    print(answer)
