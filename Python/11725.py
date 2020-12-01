# 11725번 트리의 부모 찾기
from collections import deque

n = int(input())
node = [0 for _ in range(n+1)]

adj_list = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())

    adj_list[x].append(y)
    adj_list[y].append(x)

q = deque()
q.append(1)
node[1] = 1
while q:
    cur = q.pop()

    for i in adj_list[cur]:
        if node[i] == 0:
            node[i] = cur
            q.append(i)

for i in range(2, n+1):
    print(node[i])
