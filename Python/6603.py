# 6603번 로또
from collections import deque
import sys, copy

# bfs
def bfs(s, k):
    q = deque()
    
    for i in range(k-5):
        q.append([s[i]])

    while q:
        lotto = q.popleft()

        if len(lotto) == 6:
            for i in lotto:
                print(i, end=' ')
            print()

        for num in s:
            if num > lotto[-1]:
                tmp = copy.deepcopy(lotto)
                tmp.append(num)
                q.append(tmp)

# main
while True:
    # input array
    s = [int(x) for x in sys.stdin.readline().split()]
    k = s.pop(0)

    # end of testcase
    if k == 0:
        break

    s.sort()
    bfs(s, k)
    print()
    