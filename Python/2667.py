# 2667번 단지번호붙이기
import sys

# main
n = int(sys.stdin.readline())

map = []
for _ in range(n):
    map.append([int(x) for x in sys.stdin.readline().split()])

for i in range(n):
    for j in range(n):
        