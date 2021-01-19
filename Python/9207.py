# 9207번 페그 솔리테어
import sys, copy, heapq
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(sys.stdin.readline())
for t in range(n):
    board = [list(sys.stdin.readline().strip()) for _ in range(5)]

    pin = 0
    for i in range(5):
        for j in range(9):
            if board[i][j] == 'o':
                pin += 1

    move = sys.maxsize
    min_pin = sys.maxsize
    q = []
    heapq.heappush(q, [0, pin, board])
    while q:
        cur_move, cur_pin, cur_board = heapq.heappop(q)

        if min_pin > cur_pin:
            if min_pin == cur_pin:
                move = min(move, cur_move)
            else:
                move = cur_move
            min_pin = cur_pin

        is_move = False
        for i in range(5):
            for j in range(9):
                if cur_board[i][j] == 'o':
                    for k in range(4):
                        ni = i + dy[k]
                        nj = j + dx[k]

                        if 0 <= ni < 5 and 0 <= nj < 9:
                            if cur_board[ni][nj] == 'o':
                                nni = ni + dy[k]
                                nnj = nj + dx[k]

                                if 0 <= nni < 5 and 0 <= nnj < 9:
                                    if cur_board[nni][nnj] == '.':
                                        nboard = copy.deepcopy(cur_board)
                                        nboard[ni][nj] = '.'
                                        nboard[i][j] = '.'
                                        nboard[nni][nnj] = 'o'
                                        is_move = True
                                        heapq.heappush(q, [cur_move + 1, cur_pin - 1, nboard])

    print(min_pin, move)

    if not t == n - 1:
        sys.stdin.readline()