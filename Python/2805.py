# 2805번 나무 자르기
import sys

# 이진 탐색
def binSearch(start, end, m):
    while start <= end:
        mid = (start + end) // 2

        meter = 0
        for tree in trees:
            tmp = tree - mid
            if tmp > 0:
                meter += tmp
        
        if meter >= m:
            cut.append(mid)
            start = mid+1
        else:
            end = mid-1

# main
n, m = [int(x) for x in sys.stdin.readline().split()]
trees = [int(x) for x in sys.stdin.readline().split()]

cut = []
binSearch(0,max(trees),m)

print(max(cut))
