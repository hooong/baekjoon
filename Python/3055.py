# 3055번 탈출
from collections import deque
import sys

# bfs
def bfs(start, flood):
    global R, C, forest

    s_q = deque([start])
    f_q = deque(flood)

    # 고슴도치 방문 여부 배열
    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[start[1]][start[0]] = True
    
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    count = 1
    while s_q:
        # 물 이동
        f_len = len(f_q)
        for _ in range(f_len):
            x, y = f_q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < C and 0 <= ny < R:
                    if forest[ny][nx] == '.':
                        forest[ny][nx] = '*'
                        f_q.append([nx,ny])

        # 고슴도치 이동
        s_len = len(s_q)
        for _ in range(s_len):
            x, y = s_q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < C and 0 <= ny < R:
                    if forest[ny][nx] == 'D':
                        return count
                    if not visited[ny][nx] and forest[ny][nx] == '.':
                        visited[ny][nx] = True
                        s_q.append([nx,ny])
        count += 1
    # While문이 끝나게되면 굴로 들어가지 못함.
    return "KAKTUS" 

# main
R, C = map(int, input().split())

forest = [['.' for _ in range(C)] for _ in range(R)]    # 숲
flood = []  # 물의 좌표 저장
for i in range(R):
    tmp = sys.stdin.readline()
    for j in range(C):
        if tmp[j] == 'S':
            start = [j,i]
        else:
            forest[i][j] = tmp[j]
            if tmp[j] == '*':
                flood.append([j,i])

print(bfs(start,flood))
