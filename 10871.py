n, a = map(int, input().split())

list = [int(s) for s in input().split()]

for i in list:
    if i < a:
        print(i, end=' ')