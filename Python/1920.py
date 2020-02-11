# 1920번 수 찾기
import sys

# 이진 탐색
def binSearch(start,end,val):
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
arr = [int(x) for x in sys.stdin.readline().split()]
arr.sort()

m = int(sys.stdin.readline())
target = [int(x) for x in sys.stdin.readline().split()]

for t in target:
    if binSearch(0,n-1,t):
        print(1)
    else:
        print(0)