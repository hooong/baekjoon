# 1009번 분산처리
import sys


for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())

    tmp = a
    for _ in range(b - 1):
        tmp = (tmp * a) % 10

    if (tmp % 10) == 0:
        print(10)
    else:
        print(tmp % 10)
