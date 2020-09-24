# 뱀
from collections import deque

n = int(input())

board = [[0] * n for _ in range(n)]

k = int(input())
for _ in range(k):
    y, x = map(int, input().split())
    board[y-1][x-1] = 1

l = int(input())
moves = dict()
for _ in range(l):
    t, d = input().split()
    moves[int(t)] = d

snake = deque()
snake.append([0,0])
y = x = 0

time = 0
d = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while True:
    time += 1
    y = y + dy[d]
    x = x + dx[d]

    if 0 <= y < n and 0 <= x < n and not [y,x] in snake:
        snake.append([y,x])
        if board[y][x] == 1:
            board[y][x] = 0
        else:
            snake.popleft()
        
        if time in moves.keys():
            turn = moves[time]
            if turn == 'L':
                d = (d+3)%4
            else:
                d = (d+1)%4
    else:
        break

print(time)
