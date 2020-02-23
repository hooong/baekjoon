# 11286번 절댓값 힙
import sys
import heapq

# main
n = int(sys.stdin.readline())

heap_p = []
heap_n = []

for _ in range(n):
    num = int(sys.stdin.readline())

    if num == 0:
        if len(heap_n) == 0 and len(heap_p) == 0:
            print(0)
        elif len(heap_n) != 0 and len(heap_p) == 0:
            print(-1 * heapq.heappop(heap_n))
        elif len(heap_n) == 0 and len(heap_p) != 0:
            print(heapq.heappop(heap_p))
        else:
            p = heapq.heappop(heap_p)
            n = heapq.heappop(heap_n)

            if p < n:
                print(p)
                heapq.heappush(heap_n, n)
            else:
                print(-1 * n)
                heapq.heappush(heap_p, p)
    else:
        if num < 0:
            heapq.heappush(heap_n, -1 * num)
        else:
            heapq.heappush(heap_p, num)
    