# 13460번 구슬 탈출 2
from collections import deque
import sys, copy

# 기울이기 bfs
def tilt(ball_r, ball_b, hall, board):
    visit_R = [[0 for _ in range(m)] for _ in range(n)]

    q = deque()
    q.append([ball_r,ball_b])

    count = 0
    d = [[-1,0], [0,-1], [1,0], [0,1]]  # 상하좌우
    while q:
        # 최대 10번만 움직일 수 있음
        if count == 10:
            return -1
        else:
            count += 1
           
        r, b = q.popleft()
        
        for i in range(4):
            dp = d[i]
            drx = r[0]
            dry = r[1]
            dbx = b[0]
            dby = b[1]

            while True:
                drx += dp[0]
                dry += dp[1]

                if board[dry][drx] != '#' and visit_R[dry][drx] == 0:
                    visit_R[dry][drx] = count

                    # R이 구멍을 만나는 경우
                    if board[dry][drx] == 'O':
                        while board[dby][dbx] != '#':
                            dbx += dp[0]
                            dby += dp[1]
                            
                            # B도 구멍을 만나 동시에 빠짐
                            if board[dby][dbx] == 'O':
                                return -1
                        # R만 구멍으로 나옴
                        return visit_R[dry][drx]
                    # R이 B를 만나는 경우
                    elif dry == dby and drx == dbx:
                        if board[dry][drx] == '#':
                            drx -= dp[0] * 2
                            dry -= dp[1] * 2
                            dbx -= dp[0]
                            dby -= dp[1]
                            q.append([[drx,dry],[dbx,dby]])
                            break

                        while board[dby][dbx] != '#':
                            dbx += dp[0]
                            dby += dp[1]
                            
                            # R보다 B가 먼저 구멍에 빠짐.
                            if board[dby][dbx] == 'O':
                                return -1
                        # R을 다시 움직임
                        continue


                    
                    



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
