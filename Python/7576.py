# 7576번 토마토
import sys
from collections import deque

# main
m, n = [int(x) for x in sys.stdin.readline().split()]

farm = []       # 전체 토마토의 상황
ripe = deque()       # 익은 것을 저장하는 큐
unripe = 0      # 익지 않은 것의 수를 저장
for i in range(n):
    tmp = []
    j = 0
    for x in sys.stdin.readline().split():
        if x == '-1':
            tmp.append(-1)
        elif x == '0':
            tmp.append(0)
            unripe += 1
        else:
            tmp.append(1)
            ripe.append([i,j])
        j += 1
    farm.append(tmp)

if unripe == 0:
    print(0)
elif len(ripe) == 0:
    print(-1)
else:
    count = 0
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    
    else:
        while ripe:
            for _ in range(len(ripe)):
                tomato = ripe.popleft()
                x = tomato[0]
                y = tomato[1]

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx and nx < n and 0 <= ny and ny < m:
                        if farm[nx][ny] == 0:
                            farm[nx][ny] =1
                            ripe.append([nx,ny])
                            unripe -= 1
                if len(ripe) == 0 and unripe == 0:
                    print(count)
                elif len(ripe) == 0 and unripe != 0:
                    print(-1)

            count += 1

