import sys

n = int(input())
list = []

for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    list.append(a+b)

for i in list:
    print(i)