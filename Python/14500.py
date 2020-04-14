# 14500번 테트로미노
import sys

# dfs
def dfs(y,x,cnt,cur):
    global maxSum, visit, board

    if cnt == 4:
        maxSum = max(maxSum,cur)
        return
    
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if not visit[ny][nx]:
                visit[ny][nx] = True
                dfs(ny, nx, cnt+1, cur+board[ny][nx])
                visit[ny][nx] = False

# main
n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append([int(x) for x in sys.stdin.readline().split()])

maxSum = 0
visit = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        visit[i][j] = True
        dfs(i,j,1,board[i][j])
        visit[i][j] = False

        # 'ㅗ'모양에 대한 탐색
        di = [[1,1,2],[1,1,1],[1,1,2],[0,0,1]]
        dj = [[0,1,0],[-1,0,1],[-1,0,0],[1,2,1]]
        for k in range(4):
            tmp = board[i][j]
            isPos = True

            for l in range(3):
                ni = i + di[k][l]
                nj = j + dj[k][l]

                if 0 <= ni < n and 0 <= nj < m:
                    tmp += board[ni][nj]
                else:
                    isPos = False
                    break
            
            if isPos:
                maxSum = max(maxSum, tmp)

print(maxSum)