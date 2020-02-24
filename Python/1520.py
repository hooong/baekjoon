# 1520번 내리막 길
import sys

# dfs
def find_dfs(x,y):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    if x == m-1 and y == n-1:
        return 1

    if dp[y][x] == -1:
        dp[y][x] = 0
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx and nx < m and 0 <= ny and ny < n:
                if map[y][x] > map[ny][nx]:
                    dp[y][x] += find_dfs(nx, ny)
    return dp[y][x]


# main
n, m = [int(x) for x in sys.stdin.readline().split()]

map = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
dp = [[(-1) for _ in range(m)] for _ in range(n)]

print(find_dfs(0,0))

