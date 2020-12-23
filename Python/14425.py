# 14425번 문자열 집합
import sys

n, m = map(int, sys.stdin.readline().split())
str_arr = dict()
cnt = 0

for _ in range(n):
    s = sys.stdin.readline()
    str_arr[s] = True

for _ in range(m):
    candidate = sys.stdin.readline()

    if candidate in str_arr.keys():
        cnt += 1

print(cnt)
