# 19952번 인성 문제 있어?
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

t = int(input())

for _ in range(t):
    h, w, o, f, xs, ys, xe, ye = map(int, input().split())
    board = [[0] * w for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    visited[xs-1][ys-1] = True

    for _ in range(o):
        x, y, l = map(int, input().split())
        board[x-1][y-1] = l

    is_success = False
    dq = deque()
    dq.append([xs-1, ys-1, f])

    while dq:
        cur_x, cur_y, cur_f = dq.popleft()
        
        if cur_x == xe - 1 and cur_y == ye - 1:
            is_success = True
            break

        if cur_f == 0:
            continue
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                if (board[nx][ny] - board[cur_x][cur_y]) <= cur_f:
                    visited[nx][ny] = True
                    dq.append([nx, ny, cur_f-1])

    if is_success:
        print("잘했어!!")
    else:
        print("인성 문제있어??")

