# 1697번 숨바꼭질
from collections import deque

# bfs
def find(street,n,k):
    q = deque()
    q.append(n)

    dp = [-1,1]
    while q:
        pos = q.popleft()

        # 걷기
        for i in range(2):
            np = pos + dp[i]
            
            if 0 <= np <= 100000 and street[np] == 0:
                if np == k:
                    return street[pos] + 1
                else:
                    street[np] = street[pos] + 1
                    q.append(np)
        
        # 순간이동
        np = pos * 2

        if np <= 100000 and street[np] == 0:
            if np == k:
                return street[pos] + 1
            else:
                street[np] = street[pos] + 1
                q.append(np)

# main
n, k = map(int, input().split())
street = [0] * 100001

if n == k:
    print(0)
else:
    print(find(street,n,k))
