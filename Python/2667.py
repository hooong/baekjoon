# 2667번 단지번호붙이기
import sys

# dfs
def dfs(x,y):
    global count 

    # 상하좌우 확인을 위한 배열
    dx = [-1, 0 ,1, 0]
    dy = [0, -1, 0, 1]
    
    count += 1      # dfs의 반복 횟수 측정 (즉, 단지 내 집의 수)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # map배열 범위 안의 값인지 확인
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 방문한 적이 없고 집이 있다면 재귀
            if visit[nx][ny] == 0 and map[nx][ny] == '1':
                visit[nx][ny] = 1
                dfs(nx,ny)

# main
n = int(sys.stdin.readline())

map = []
for _ in range(n):
    map.append(list(sys.stdin.readline()))

# 방문여부 저장
visit = [[0 for _ in range(n)] for _ in range(n)]

apart = []
for i in range(n):
    for j in range(n):
        # 방문한 적이 없고 집이 있다면
        if visit[i][j] == 0 and map[i][j] == '1':
            visit[i][j] = 1
            count = 0
            dfs(i,j)
            apart.append(count)   
        # 방문한 적이 없고 집도 없는 경우 또는 방문을 이미 한 경우
        else:
            visit[i][j] = 1

print(len(apart))
apart.sort()
for num in apart:
    print(num)