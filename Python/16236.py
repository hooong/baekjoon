# 16236번 아기 상어
from collections import deque
import sys


def find_fish(cur_y, cur_x):
    visited = [[False] * n for _ in range(n)]
    move_que = deque()  # 물고기를 찾기 위한 움직임을 담는 큐
    move_que.append([0, cur_y, cur_x])
    visited[cur_y][cur_x] = True
    fish = []  # 잡어먹을 수 있는 물고기
    while move_que:
        cur_time, cur_y, cur_x = move_que.popleft()

        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    if sea[ny][nx] == 0 or sea[ny][nx] == size:
                        move_que.append([cur_time + 1, ny, nx])
                    elif sea[ny][nx] < size:
                        fish.append([cur_time + 1, ny, nx])
    if fish:
        fish.sort(key=lambda f: (f[0], f[1], f[2]))
        return fish[0]
    else:
        return -1


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(sys.stdin.readline())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 아기상어의 초기 위치 탐색
cur = []
for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            cur = [i, j]
            break
    if not cur == []:
        break

total_time = 0  # 아기 상어가 버티는 시간
eat_cnt = 0         # 물고기를 먹는 횟수
y = cur[0]
x = cur[1]
size = 2
while True:
    eat_fish = find_fish(y, x)
    if eat_fish == -1:
        break
    else:
        time, fish_y, fish_x = eat_fish

    total_time += time
    eat_cnt += 1

    if eat_cnt == size:
        eat_cnt = 0
        size += 1

    # 상어 실제 이동
    sea[fish_y][fish_x] = 9
    sea[y][x] = 0
    y = fish_y
    x = fish_x

print(total_time)
