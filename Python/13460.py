# 13460번 구슬 탈출 2
from collections import deque
import sys, copy

# 기울이기
def tilt(board, dir, r, b):

# bfs (board를 저장)
def bfs(board, ball_r, ball_b):
    q = deque()
    q.append([ball_r, ball_b])

    d = ['up', 'down', 'left', 'right']
    count = 0
    while q:
        if count > 10:
            return -1

        l = len(q)
        for _ in range(l):
            tmp = q.popleft()
            cur_board = copy.deepcopy(tmp[0])
            r = tmp[1]
            b = tmp[2]

            for i in range(4):
                tilt(cur_board, d[i], r, b)

        
        count += 1

    

# main
n, m = [int(x) for x in sys.stdin.readline().split()]   # 세로 : n, 가로 : m

board = []
for i in range(n):
    row = sys.stdin.readline()
    board.append(row)
    for j in range(m):
        if row[j] == 'R':
            ball_r = [i,j]
        elif row[j] == 'B':
            ball_b = [i,j]
        elif row[j] == 'O':
            hall = [i,j]



