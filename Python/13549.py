# 13549번 숨바꼭질 3
from collections import deque

# main
n, k = map(int, input().split())

answer = float('inf')

q = deque()
q.append([n,0])

visited = [False for _ in range(100001)]
visited[n] = True

while q:
    soo, cnt = q.popleft()
    visited[soo] = True

    if soo == k:
        answer = min(answer, cnt)

    if soo*2 < 100001 and not visited[soo*2]:
        q.append([soo*2,cnt])
    
    if soo+1 < 100001 and not visited[soo+1]:
        q.append([soo+1,cnt+1])

    if 0 <= soo-1 and not visited[soo-1]:
        q.append([soo-1,cnt+1])

print(answer)