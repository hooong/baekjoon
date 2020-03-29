# 7562번 나이트의 이동
from collections import deque
import sys

# bfs
def check(board, x, y):
    q = deque()
    q.append([x,y])

    # 나이트가 이동할 수 있는 8가지의 경우
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]
    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if board[ny][nx] == -1:
                    # 방문하지 않은 곳이면 바로 이전의 움직임 +1을 저장
                    board[ny][nx] = board[y][x] + 1
                    q.append([nx,ny])

# main
T = int(input())

for _ in range(T):
    n = int(input())

    # 방문하지 않은 곳 : -1
    board = [[-1 for _ in range(n)] for _ in range(n)]
    cur_x, cur_y = [int(x) for x in sys.stdin.readline().split()]
    target_x, target_y = [int(x) for x in sys.stdin.readline().split()]

    board[cur_y][cur_x] = 0

    # bfs 실행
    check(board, cur_x, cur_y)
    print(board[target_y][target_x])
