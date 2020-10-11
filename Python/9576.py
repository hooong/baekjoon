# 9576번 책 나눠주기
from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    books = [False] * (n+1)

    requests = []
    for _ in range(m):
        requests.append(list(map(int, input().split())))
    requests.sort(key=lambda x: x[1])

    cnt = 0
    while requests:
        a, b = requests.pop(0)

        for i in range(a, b+1):
            if not books[i]:
                cnt += 1
                books[i] = True
                break
        
    print(cnt)
