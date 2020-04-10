# 1074번 Z
import sys

# find part
def find(n,y,x):
    if n == 1:
        if y == 0:
            if x == 0:
                return 0
            else:
                return 1
        else:
            if x == 0:
                return 2
            else:
                return 3
    
    half = 2 ** (n-1)
    if 0 <= y < half:
        # 1사분면
        if 0 <= x < half:
            tmp = find(n-1,y,x)
            return tmp
        # 2사분면 
        else:
            tmp = find(n-1,y,x-half)
            return half*half + tmp
    else:
        # 3사분면
        if 0 <= x < half:
            tmp = find(n-1,y-half,x)
            return 2*half*half + tmp
        # 4사분면 
        else:
            tmp = find(n-1,y-half,x-half)
            return 3*half*half + tmp

# main
N, r, c = [int(x) for x in sys.stdin.readline().split()]

print(find(N,r,c))