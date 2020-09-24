# 14503번 로봇 청소기

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

bx = [0, -1, 0, 1]
by = [1, 0, -1, 0] 
def dfs(y, x, d, cnt):
    global count 

    if cnt == 4:
        ny = y + by[d]
        nx = x + bx[d]

        if not room[ny][nx] == 1:
            dfs(ny, nx, d, 0)
            return
        else:
            return

    if room[y][x] == 0:
        count += 1
        room[y][x] = 2

    ny = y + dy[d]
    nx = x + dx[d]
    if room[ny][nx] == 0:
        dfs(ny, nx, (d+3)%4, 0)
    elif room[ny][nx] == 1 or room[ny][nx] == 2:
        dfs(y, x, (d+3)%4, cnt+1)


n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

count = 0
dfs(r,c,d,0)
print(count)
