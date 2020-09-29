# 17070번 파이프 옮기기 1

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(n+1)] for _ in range(n+1)]
dp[1][2] = [1, 0, 0]

dx = [-1, 0, -1]
dy = [0, -1, -1]
for i in range(1,n+1):
    for j in range(1,n+1):
        # 가로
        ny = i + dy[0]
        nx = j + dx[0]
        if not dp[ny][nx][0] == 0 or not dp[ny][nx][2] == 0:
            if not board[i-1][j-1] == 1:
                dp[i][j][0] = dp[ny][nx][0] + dp[ny][nx][2]

        # 세로
        ny = i + dy[1]
        nx = j + dx[1]
        if not dp[ny][nx][1] == 0 or not dp[ny][nx][2] == 0:
            if not board[i-1][j-1] == 1:
                dp[i][j][1] = dp[ny][nx][1] + dp[ny][nx][2]

        # 대각
        ny = i + dy[2]
        nx = j + dx[2]
        if not sum(dp[ny][nx]) == 0:
            if not board[i-1][j-1] == 1 and not board[i-2][j-1] == 1 and not board[i-1][j-2] == 1:
                dp[i][j][2] = sum(dp[ny][nx])

print(sum(dp[-1][-1]))

        

