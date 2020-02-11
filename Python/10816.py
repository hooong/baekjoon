# 10816번 숫자 카드 2
import sys

# 이진 탐색
def binSearch(start, end, val):
    mid = (start + end) // 2
    if arr[mid] == val:
        return True
    else:
        if start >= end:
            return False
        if arr[mid] > val:
            return binSearch(start,mid,val)
        else:
            return binSearch(mid+1,end,val)

# main
n = int(sys.stdin.readline())

arr = []
arr_dict = {}
for num in sys.stdin.readline().split():
    num = int(num)
    if num in arr:
        arr_dict[num] += 1
    else:
        arr.append(num)
        arr_dict[num] = 1
arr.sort()

m = int(sys.stdin.readline())
target = [int(x) for x in sys.stdin.readline().split()]

for t in target:
    if binSearch(0,len(arr)-1,t):
        print(arr_dict[t], end=' ')
    else:
        print(0, end=' ')
print()