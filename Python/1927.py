# 1927번 최소 힙
import sys
import heapq

# main
n = int(sys.stdin.readline())

heap = []
for _ in range(n):
    num = int(sys.stdin.readline())
    
    if num == 0:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, num)