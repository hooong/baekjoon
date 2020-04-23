# 1248번 맞춰봐
import sys

# dfs
def dfs(cur):
    global s, arr, n

    if cur == -1:
        return True
    
    for i in range(-10,11):
        arr[cur] = i

        ispos = True
        for j in range(cur,n):
            tmp = sum(arr[cur:j+1])
            if s[cur][j] == '+':
                if not tmp > 0:
                    ispos = False
                    break
            elif s[cur][j] == '-':
                if not tmp < 0:
                    ispos = False
                    break
            else:
                if not tmp == 0:
                    ispos = False
                    break
        if ispos:
            if dfs(cur-1):
                return True

# main
n = int(input())
sign = list(sys.stdin.readline().strip())

s = [['' for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(i,n):
        s[i][j] = sign.pop(0)

arr = [0 for _ in range(n)]
dfs(n-1)

for num in arr:
    print(num, end=' ')
print()
