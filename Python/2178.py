# 2178번 미로 탐색

# bfs
def search(x,y):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    q = [[x,y]]
    while q:
        pos = q.pop(0)
        x = pos[0]
        y = pos[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx and nx < m and 0 <= ny and ny < n:
                if maze[ny][nx] == 1:
                    q.append([nx,ny])
                    maze[ny][nx] = maze[y][x] + 1
# main
n, m = map(int, input().split())

maze = []
for _ in range(n):
    tmp = []
    for num in list(input()):
        tmp.append(int(num))
    maze.append(tmp)

search(0,0)
print(maze[n-1][m-1])

