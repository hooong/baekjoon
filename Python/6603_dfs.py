# 6603번 로또
from collections import deque
import sys

# dfs
def dfs(s, cur, pos):
    if len(cur) == 6:
        for i in cur:
            print(i, end=' ')
        print()
        return

    for i in range(pos, len(s)):
        if pos < len(s):
            cur.append(s[i])
            dfs(s,cur,i+1)
            cur.pop()

# main
while True:
    # input array
    s = [int(x) for x in sys.stdin.readline().split()]
    k = s.pop(0)

    # end of testcase
    if k == 0:
        break

    s.sort()
    dfs(s,[],0)
    print()
    