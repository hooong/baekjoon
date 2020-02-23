# 1655번 가운데를 말해요
import sys
import heapq

# main
n = int(sys.stdin.readline())

maxHeap = []    # 최대힙
minHeap = []    # 최소힙
for _ in range(n):
    num = int(sys.stdin.readline())

    # 1번 조건
    if len(maxHeap) == 0:
        heapq.heappush(maxHeap, -1 * num)
    elif len(minHeap) == len(maxHeap):
        heapq.heappush(maxHeap, -1 * num)
    else:
        heapq.heappush(minHeap, num)

    # 2번 조건
    if len(minHeap) != 0 and len(maxHeap) != 0 and minHeap[0] < (-1 * maxHeap[0]):
        tmp_min = heapq.heappop(minHeap)
        tmp_max = heapq.heappop(maxHeap)

        heapq.heappush(maxHeap, -1 * tmp_min)
        heapq.heappush(minHeap, -1 * tmp_max)

    print(-1 * maxHeap[0])
