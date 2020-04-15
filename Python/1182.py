# 1182번 부분수열의 합
import sys

# dfs
def dfs(cur,cur_s):
    global n, s, arr, cnt
    
    if cur_s == s:
        cnt += 1

    for i in range(cur+1,n):
        dfs(i,cur_s+arr[i])

# main
n, s = map(int, input().split())
arr = [int(x) for x in sys.stdin.readline().split()]

cnt = 0
for i in range(n):
    dfs(i,arr[i])

print(cnt)
