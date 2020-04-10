# 1476번 날짜 계산
import sys

# main
date = [int(x) for x in sys.stdin.readline().split()]

i = 1
while True:
    e = i % 15
    if e == 0:
        e = 15

    s = i % 28
    if s == 0:
        s = 28

    m = i % 19
    if m == 0:
        m = 19

    if e == date[0] and s == date[1] and m == date[2]:
        print(i)
        break
    else:
        i += 1