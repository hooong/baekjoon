# 19236번 청소년 상어
import sys, copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def print_sea(board):
    for i in board:
        print(*i)
    print()


# 물고기 움직임
def move_fish(board, fish):
    for i in range(1, 17):
        if fish[i] == [-1, -1, -1]:
            continue

        fx, fy, fd = fish[i]

        cnt = 0
        while True:
            if cnt == 8:
                break

            nx = fx + dx[fd]
            ny = fy + dy[fd]

            if 0 <= nx < 4 and 0 <= ny < 4:
                if not board[nx][ny] == 'S':
                    fish[board[fx][fy]] = [nx, ny, fd]

                    if not board[nx][ny] == -1:
                        fish[board[nx][ny]][0] = fx
                        fish[board[nx][ny]][1] = fy

                    board[fx][fy], board[nx][ny] = board[nx][ny], board[fx][fy]
                    break

            fd = (fd + 1) % 8
            cnt += 1
    # print_sea(board)


# 상어의 움직임
def shark_round(cur_shark, board, fish, eat):
    global answer

    answer = max(answer, eat)

    # 물고기 움직임
    move_fish(board, fish)

    sx, sy, sd = cur_shark
    board[sx][sy] = -1

    while True:
        sx += dx[sd]
        sy += dy[sd]

        if 0 <= sx < 4 and 0 <= sy < 4:
            if not board[sx][sy] == -1:
                fish_num = board[sx][sy]
                fish_direction = fish[fish_num][2]

                tmp_fish = copy.deepcopy(fish)
                tmp_board = copy.deepcopy(board)

                tmp_fish[fish_num] = [-1, -1, -1]
                tmp_board[sx][sy] = 'S'
                shark_round([sx, sy, fish_direction], tmp_board, tmp_fish, eat + fish_num)
        else:
            break


sea = [[0] * 4 for _ in range(4)]
fish = [-1, -1, -1] * 17
answer = 0

for i in range(4):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(4):
        a = line.pop(0)
        b = line.pop(0)

        sea[i][j] = a
        fish[a] = [i, j, b-1]

# 상어 처음 (0,0)으로 진입
fish_eat = sea[0][0]
sea[0][0] = 'S'
shark = fish[fish_eat]
fish[fish_eat] = [-1, -1, -1]
answer += fish_eat

shark_round(shark, copy.deepcopy(sea), copy.deepcopy(fish), answer)
print(answer)
