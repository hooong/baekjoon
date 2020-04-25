# 1080번 행렬
import sys

# flip
def flip(y,x):
    global matA

    for i in range(3):
        for j in range(3):
            if matA[y+i][x+j] == '0':
                matA[y+i][x+j] = '1'
            else:
                matA[y+i][x+j] = '0' 

# main
n, m = map(int, input().split())

matA = []
matB = []
for _ in range(n):
    matA.append(list(sys.stdin.readline().strip()))

for _ in range(n):
    matB.append(list(sys.stdin.readline().strip()))

cnt = 0
if n < 3 or m < 3:
    if matA == matB:
        print(cnt)
        exit(0)

for i in range(n-2):
    for j in range(m-2):
        if not matA[i][j] == matB[i][j]:
            flip(i,j)
            cnt += 1

        if matA == matB:
            print(cnt)
            exit(0)

print(-1)
        