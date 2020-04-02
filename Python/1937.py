# 1937번 욕심쟁이 판다
import sys

#main
n = int(input())

order = []  # 각 대나무의 양과 좌표를 저장
forest = [] # 입력되는 숲
for i in range(n):
    row = [int(x) for x in sys.stdin.readline().split()]
    for j in range(n):
        order.append([row[j],j,i])  # 대나무 양, x, y
    forest.append(row)

# 내림차순 정렬 (대나무 양 기준)
order.sort(reverse=True)

answer = 0
maxDays = [[1 for _ in range(n)] for _ in range(n)]
for t in order:
    tree, x, y = t

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    
    tmp = []        # 상하좌우 인접한 곳 중 더 큰 곳의 수를 저장 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if forest[y][x] < forest[ny][nx]:
                tmp.append(maxDays[ny][nx])
    
    # tmp가 비었다면 인접한 곳에 더 큰 곳이 없다.
    if len(tmp) != 0:
        maxDays[y][x] = max(tmp) + 1    # 가장 큰 값에서 하루를 더 살 수 있음.
    
    if answer < maxDays[y][x]:
        answer = maxDays[y][x]

print(answer)
