# 1012번 유기농 배추
import sys
sys.setrecursionlimit(100000)

# dfs
def worm(x,y):

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    # 상하좌우 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < m and 0 <= ny and ny < n:
            if visit[ny][nx] == 0  and farm[ny][nx] == 1:
                visit[ny][nx] = 1
                worm(nx,ny)

# main
t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    farm = [[0 for _ in range(m)] for _ in range(n)]
    visit = [[0 for _ in range(m)] for _ in range(n)]
    cabbage = []

    for _ in range(k):
        x, y = [int(a) for a in sys.stdin.readline().split()]
        farm[y][x] = 1
        cabbage.append([x,y])
    
    count = 0
    for x,y in cabbage:
        if visit[y][x] == 0:
            visit[y][x] = 1
            worm(x,y)
            count += 1
    
    print(count)
