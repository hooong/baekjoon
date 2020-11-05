# 15683번 감시

def dfs(level):
    if level == len(cctv):
        # 사각지대 카운트

    
    

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
cctv = []

for i in range(n):
    for j in range(m):
        if not office[i][j] in [0,6]:
            cctv.append([i, j, kind])

dfs(0)



