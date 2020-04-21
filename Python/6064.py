# 6064번 카잉달력
import sys

# 최대공약수
def gcd(x,y):
    a = min(x,y)
    b = max(x,y)

    while True:
        if a == 0:
            return b

        tmp = a
        a = b % a
        b = tmp

# main
t = int(input())

for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())

    lcm = (m * n) // gcd(m,n)
    cnt = x
    i = x % n
    while True:
        if i == 0:
            i = n

        if cnt > lcm:
            print(-1)
            break
        
        if i == y:
            print(cnt)
            break

        cnt += m
        i = (i+m) % n
