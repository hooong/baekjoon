# 10816번 숫자 카드 2
import sys

# main
n = int(sys.stdin.readline())

arr_dict = {}
for num in sys.stdin.readline().split():
    num = int(num)
    keys = arr_dict.keys()
    if num in keys:
        arr_dict[num] += 1
    else:
        arr_dict[num] = 1

m = int(sys.stdin.readline())
target = [int(x) for x in sys.stdin.readline().split()]

for t in target:
    if t in keys:
        print(arr_dict[t], end=' ')
    else:
        print(0, end=' ')
print()