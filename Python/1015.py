# 1015번 수열 정렬

n = int(input())

a = list(map(int, input().split()))
p = [0] * n
b = sorted(a)

visited = [False] * n

for i in range(n):
    ai = a[i]

    for j in range(n):
        if ai == b[j] and not visited[j]:
            p[i] = j
            visited[j] = True
            break

print(*p)
