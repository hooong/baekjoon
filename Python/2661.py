# 2661번 좋은수열

def dfs(l, seq):
    for j in range(1, l//2+1):
        if seq[l-(2*j):l-(2*j)+j] == seq[l-(2*j)+j:]:
            return

    if l == n:
        print(*seq, sep='')
        exit(0)
    
    for i in range(1, 4):
        if seq and seq[-1] == i:
            continue
        dfs(l+1, seq+[i])

n = int(input())
dfs(0, [])
