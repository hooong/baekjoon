# 2470번 두 용액
import sys
INF = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

i = 0
j = len(arr) - 1
pair = []
min_val = INF
while i < j:
    tmp = arr[i] + arr[j]

    if abs(tmp) < min_val:
        pair = [arr[i], arr[j]]
        min_val = abs(tmp)

    if tmp >= 0:
        j -= 1
    else:
        i += 1

print(*pair)
