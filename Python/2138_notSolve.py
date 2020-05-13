# 2138번 전구와 스위치
import sys, copy

# on-off
def on_off(i,j):
    global tLight

    for x in range(i,j+1):
        if tLight[x] == '0':
            tLight[x] = '1'
        else:
            tLight[x] = '0' 

# main
n = int(input())

bLight = list(sys.stdin.readline().strip())     # before
tLight = copy.deepcopy(bLight)
aLight = list(sys.stdin.readline().strip())     # after

cnt = 0
i = 0
while True:
    if not aLight[i] == tLight[i]:
        if i == 0:
            on_off(i,i+1)
        elif i == n-1:
            on_off(i-1,i)
        else:
            on_off(i-1,i+1)
        cnt += 1

        if tLight == bLight:
            print(-1)
            break
    
        if aLight == tLight:
            print(cnt)
            break
    i = (i + 1) % n
