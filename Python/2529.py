# 2529번 부등호
import sys

# dfs
def min_dfs(answer, cur, cnt):
    global k, signs, min_int, visited

    if cnt == k:
        min_int = answer
        return True

    if signs[cnt] == '>':
        for i in range(cur):
            if not visited[i]:
                visited[i] = True
                if min_dfs(answer+str(i), i, cnt+1):
                    return True
                visited[i] = False
    else:
        for i in range(cur+1,10):
            if not visited[i]:
                visited[i] = True
                if min_dfs(answer+str(i), i, cnt+1):
                    return True
                visited[i] = False

def max_dfs(answer, cur, cnt):
    global k, signs, max_int, visited

    if cnt == k:
        max_int = answer
        return True

    if signs[cnt] == '>':
        for i in range(cur-1,-1,-1):
            if not visited[i]:
                visited[i] = True
                if max_dfs(answer+str(i), i, cnt+1):
                    return True
                visited[i] = False
    else:
        for i in range(9,cur,-1):
            if not visited[i]:
                visited[i] = True
                if max_dfs(answer+str(i), i, cnt+1):
                    return True
                visited[i] = False


# main
k = int(input())
signs = sys.stdin.readline().split()

min_int = ''
max_int = ''
visited = [False for _ in range(10)]
# 작은 값부터
for i in range(10):
    visited[i] = True
    if min_dfs(str(i), i, 0):
        break
    visited[i] = False

visited = [False for _ in range(10)]
# 큰 값부터
for i in range(9,-1,-1):
    visited[i] = True
    if max_dfs(str(i), i, 0):
        break
    visited[i] = False

for num in max_int:
    print(num, end='')
print()

for num in min_int:
    print(num, end='')
print()