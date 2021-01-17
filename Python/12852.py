# 12852번 1로 만들기 2
from collections import deque


n = int(input())
visited = [False] * ((10 ** 6) + 1)

q = deque()
q.append([n])
while q:
    cur = q.popleft()

    if cur[-1] == 1:
        print(len(cur) - 1)
        print(*cur)
        break

    if cur[-1] % 3 == 0 and not visited[cur[-1] // 3]:
        visited[cur[-1] // 3] = True
        q.append(cur + [cur[-1] // 3])
    if cur[-1] % 2 == 0 and not visited[cur[-1] // 2]:
        visited[cur[-1] // 2] = True
        q.append(cur + [cur[-1] // 2])
    if not visited[cur[-1] - 1]:
        visited[cur[-1] - 1] = True
        q.append(cur + [cur[-1] - 1])

