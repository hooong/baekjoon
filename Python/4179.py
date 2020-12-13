# 4179번 불!
from collections import deque
import sys, heapq


def bfs():
    global board, start, fire

    visited = [[False] * c for _ in range(r)]
    move = list()
    heapq.heappush(move, [0, start[0], start[1]])
    visited[start[0]][start[1]] = True
    while move:
        f_size = len(fire)
        for _ in range(f_size):
            f_y, f_x = fire.popleft()

            for i in range(4):
                f_ny = f_y + dy[i]
                f_nx = f_x + dx[i]

                if 0 <= f_ny < r and 0 <= f_nx < c:
                    if board[f_ny][f_nx] == '.' or board[f_ny][f_nx] == 'J':
                        board[f_ny][f_nx] = 'F'
                        fire.append([f_ny, f_nx])

        m_size = len(move)
        for _ in range(m_size):
            cnt, cur_y, cur_x = heapq.heappop(move)

            for i in range(4):
                ny = cur_y + dy[i]
                nx = cur_x + dx[i]

                if 0 <= ny < r and 0 <= nx < c:
                    if not visited[ny][nx] and board[ny][nx] == '.':
                        visited[ny][nx] = True
                        heapq.heappush(move, [cnt+1, ny, nx])
                else:
                    return cnt + 1
    return 'IMPOSSIBLE'


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

r, c = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline()) for _ in range(r)]

start = []
fire = deque()
for i in range(r):
    for j in range(c):
        if board[i][j] == 'J':
            start = [i, j]
        if board[i][j] == 'F':
            fire.append([i, j])

print(bfs())
