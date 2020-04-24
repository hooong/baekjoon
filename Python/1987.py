# 1987번 알파벳
import sys

# dfs
def dfs(x, y, count):
    global board, R, C, alpha, maxCount

    # 최대 칸수 최신화
    maxCount = max(maxCount,count)

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # ord()를 사용해서 아스키 코드로 변환
        if 0 <= nx < C and 0 <= ny < R:
            c = ord(board[ny][nx]) - 65
            if not alpha[c]:
                alpha[c] = True
                dfs(nx,ny,count+1)
                alpha[c] = False

# main
R, C = map(int, input().split())

board = []
for _ in range(R):
    board.append(sys.stdin.readline())

alpha = [False] * 26    # 알파벳 방문 여부
alpha[ord(board[0][0])-65] = True

maxCount = 0    # 최대 이동 칸수
dfs(0,0,1)
print(maxCount)
