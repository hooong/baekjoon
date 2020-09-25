# 보석 도둑
import heapq

n, k = map(int, input().split())
visited = [False for _ in range(n)]

jewelry = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

jewelry.sort()
bags.sort()

answer = 0
heap = []
j = 0
for i in range(k):
    while j < n:
        if jewelry[j][0] <= bags[i]:
            heapq.heappush(heap, (-1) * jewelry[j][1])
            j += 1
        else:
            break

    if heap:
        answer += (-1) * heapq.heappop(heap)

print(answer)
