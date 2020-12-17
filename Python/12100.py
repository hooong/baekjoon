# 12100번 2048 (Easy)
from copy import deepcopy

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def print_board(board):
    for b in board:
        print(*b)
    print()


def up(board):
    global answer

    for x in range(n):
        # 일단 모두 위로
        for y in range(1, n):
            if not board[y][x] == 0:
                ny = y
                while ny > 0:
                    if not board[ny-1][x] == 0:
                        break
                    ny -= 1

                board[y][x], board[ny][x] = board[ny][x], board[y][x]

        # 위에서부터 같은 것 합치기
        for y in range(n-1):
            if not board[y][x] == 0:
                if board[y][x] == board[y+1][x]:
                    board[y][x] *= 2
                    board[y+1][x] = 0

                    answer = max(answer, board[y][x])

        # 다시 모두 위로 올리기
        for y in range(1, n):
            if not board[y][x] == 0:
                ny = y
                while ny > 0:
                    if not board[ny-1][x] == 0:
                        break
                    ny -= 1

                board[y][x], board[ny][x] = board[ny][x], board[y][x]

    return board

def down(board):
    global answer

    for x in range(n):
        # 일단 모두 아래로
        for y in range(n-1, -1, -1):
            if not board[y][x] == 0:
                ny = y
                while ny < n-1:
                    if not board[ny+1][x] == 0:
                        break
                    ny += 1

                board[y][x], board[ny][x] = board[ny][x], board[y][x]

        # 아래에서부터 같은 것 합치기
        for y in range(n-1, 0, -1):
            if not board[y][x] == 0:
                if board[y][x] == board[y-1][x]:
                    board[y][x] *= 2
                    board[y-1][x] = 0

                    answer = max(answer, board[y][x])

        # 다시 모두 아래로
        for y in range(n - 1, -1, -1):
            if not board[y][x] == 0:
                ny = y
                while ny < n-1:
                    if not board[ny + 1][x] == 0:
                        break
                    ny += 1

                board[y][x], board[ny][x] = board[ny][x], board[y][x]

    return board


def left(board):
    global answer

    for y in range(n):
        # 일단 모두 왼쪽으로
        for x in range(1, n):
            if not board[y][x] == 0:
                nx = x
                while nx > 0:
                    if not board[y][nx-1] == 0:
                        break
                    nx -= 1

                board[y][x], board[y][nx] = board[y][nx], board[y][x]

        # 왼쪽에서부터 같은 것들 합치기
        for x in range(n-1):
            if not board[y][x] == 0:
                if board[y][x] == board[y][x+1]:
                    board[y][x] *= 2
                    board[y][x+1] = 0

                    answer = max(answer, board[y][x])

        # 다시 모두 왼쪽으로
        for x in range(1, n):
            if not board[y][x] == 0:
                nx = x
                while nx > 0:
                    if not board[y][nx - 1] == 0:
                        break
                    nx -= 1

                board[y][x], board[y][nx] = board[y][nx], board[y][x]

    return board


def right(board):
    global answer

    for y in range(n):
        # 일단 모두 오른쪽으로
        for x in range(n - 1, -1, -1):
            if not board[y][x] == 0:
                nx = x
                while nx < n - 1:
                    if not board[y][nx+1] == 0:
                        break
                    nx += 1

                board[y][x], board[y][nx] = board[y][nx], board[y][x]

        # 위에서부터 같은 놈들 합치기
        for x in range(n - 1, 0, -1):
            if not board[y][x] == 0:
                if board[y][x] == board[y][x-1]:
                    board[y][x] *= 2
                    board[y][x-1] = 0

                    answer = max(answer, board[y][x])

        # 다시 모두 위로 올리기
        for x in range(n - 1, -1, -1):
            if not board[y][x] == 0:
                nx = x
                while nx < n - 1:
                    if not board[y][nx+1] == 0:
                        break
                    nx += 1

                board[y][x], board[y][nx] = board[y][nx], board[y][x]

    return board


def move_block(board, cnt):
    global max_num

    if cnt == 5:
        return

    # 상
    move_block(up(deepcopy(board)), cnt+1)

    # 하
    move_block(down(deepcopy(board)), cnt+1)

    # 좌
    move_block(left(deepcopy(board)), cnt+1)

    # 우
    move_block(right(deepcopy(board)), cnt+1)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, board[i][j])

move_block(board, 0)
print(answer)

