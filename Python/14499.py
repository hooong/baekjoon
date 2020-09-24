# ]14499번 주사위 굴리기

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))
dice = [[0 for _ in range(3)] for _ in range(4)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
while command:
    d = command.pop(0)

    nx = x + dx[d-1]
    ny = y + dy[d-1]
    if not (0 <= ny < m) or not (0 <= nx < n):
        continue

    x = nx
    y = ny
    if d == 1:
        tmp = dice[3][1]
        dice[3][1] = dice[1][2]
        dice[1][2] = dice[1][1]
        dice[1][1] = dice[1][0]
        dice[1][0] = tmp

    elif d == 2:
        tmp = dice[3][1]
        dice[3][1] = dice[1][0]
        dice[1][0] = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = tmp

    elif d == 3:
        tmp = dice[3][1]
        dice[3][1] = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = tmp

    elif d == 4:
        tmp = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = tmp

    if board[x][y] == 0:
        board[x][y] = dice[3][1]
    else:
        dice[3][1] = board[x][y]
        board[x][y] = 0
    
    print(dice[1][1])
    