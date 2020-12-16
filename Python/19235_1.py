# 19235번 모노미노도미노
import sys


def print_green():
    for i in green[::-1]:
        print(*i)


def print_blue():
    for i in blue[::-1]:
        print(*(i[::-1]))


def down_block_green(t, x):
    global green

    if t in [1, 3]:
        i = 4
        while i > 0 and green[i-1][x] == 0:
            i -= 1
        green[i][x] = 1
        if t == 3:
            green[i+1][x] = 1
    elif t == 2:
        i = 4
        while i > 0 and green[i-1][x] == 0 and green[i-1][x+1] == 0:
            i -= 1
        green[i][x] = green[i][x+1] = 2


def down_block_blue(t, x):
    global blue

    if t in [1, 2]:
        i = 4
        while i > 0 and blue[i-1][x] == 0:
            i -= 1
        blue[i][x] = 1
        if t == 2:
            blue[i+1][x] = 1
    elif t == 3:
        i = 4
        while i > 0 and blue[i-1][x] == 0 and blue[i-1][x+1] == 0:
            i -= 1
        blue[i][x] = blue[i][x+1] = 2


def find_bang(board):
    global score

    is_exist = False
    for i in range(4):
        if board[i].count(0) == 0:
            score += 1
            board[i] = [0] * 4
            is_exist = True

    return is_exist


def down_with_bang(board):
    for j in range(1, 6):
        for i in range(4):
            if board[j][i] == 1 and board[j-1][i] == 0:
                k = j-1
                while k > 0 and board[k-1][i] == 0:
                    k -= 1
                board[k][i] = 1
                board[j][i] = 0
            elif i < 3 and board[j][i] == 2 and board[j][i+1] == 2:
                if board[j-1][i] == 0 and board[j-1][i+1] == 0:
                    k = j-1
                    while k > 0 and board[k-1][i] == 0 and board[k-1][i+1] == 0:
                        k -= 1
                    board[k][i] = board[k][i+1] = 2
                    board[j][i] = board[j][i+1] = 0


def find_light(board):
    cnt = 0
    for i in range(4, 6):
        if not board[i].count(0) == 4:
            cnt += 1

    for _ in range(cnt):
        board.pop(0)
        board.append([0] * 4)


def cnt_block():
    global green, blue

    cnt = 0
    for i in range(4):
        for j in range(4):
            if green[i][j] != 0:
                cnt += 1
            if blue[i][j] != 0:
                cnt += 1
    return cnt


# 메인 로직
green = [[0] * 4 for _ in range(6)]
blue = [[0] * 4 for _ in range(6)]
board = [green, blue]
score = 0

for _ in range(int(sys.stdin.readline())):
    t, x, y = map(int, sys.stdin.readline().split())

    # 처음 블럭 내려감
    down_block_green(t, y)
    down_block_blue(t, x)

    for color in board:
        while find_bang(color):     # 행 or 열이 터지는지 확인
            down_with_bang(color)   # 블럭 내리기
        find_light(color)           # 연한 블럭 내리기

print(score)
print(cnt_block())






