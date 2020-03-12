# 7569번 토마토(3차원)
import sys
from collections import deque

# bfs
def ripening(farm,ripe,unripe):
    count = 0
    dx = [-1,0,1,0,0,0]
    dy = [0,-1,0,1,0,0]
    dz = [0,0,0,0,-1,1]
    
    while ripe:
        for _ in range(len(ripe)):
            tomato = ripe.popleft()
            z = tomato[0]
            x = tomato[1]
            y = tomato[2]

            for i in range(6):
                nz = z + dz[i]
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                    if farm[nz][nx][ny] == 0:
                        farm[nz][nx][ny] = 1
                        unripe -= 1
                        ripe.append([nz,nx,ny])
            
            if len(ripe) == 0 and unripe == 0:
                return count
            elif len(ripe) == 0 and unripe != 0:
                return -1
        count += 1

#main
m, n, h = [int(x) for x in sys.stdin.readline().split()]

farm = []
ripe = deque()
unripe = 0

for i in range(h):
    tmp_h = []
    for j in range(n):
        tmp_n = []
        k = 0
        for x in sys.stdin.readline().split():
            tmp_n.append(int(x))
            
            if x == '1':
                ripe.append([i,j,k])
            elif x == '0':
                unripe += 1

            k += 1
        tmp_h.append(tmp_n)
    farm.append(tmp_h)

if unripe == 0:
    print(0)
elif len(ripe) == 0:
    print(-1)
else:
    print(ripening(farm,ripe,unripe))
