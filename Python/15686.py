# 15686번 치킨 배달
import sys

def dfs(cur, arr):
    global len_chicken

    if len(arr) == m:
        length = 0
        for house in houses:
            len_house = sys.maxsize
            for c in arr:
                len_house = min(len_house, abs(house[0] - c[0]) + abs(house[1] - c[1]))
            length += len_house
        len_chicken = min(len_chicken, length)
        return
    
    if cur == len(chickens):
        return
    
    dfs(cur+1, arr+[chickens[cur]])
    dfs(cur+1, arr)

n, m = map(int, input().split())

chickens = []
houses = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            houses.append([i, j])
        elif board[i][j] == 2:
            chickens.append([i, j])

len_chicken = sys.maxsize
dfs(0, [])
print(len_chicken)
