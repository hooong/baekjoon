# 1654번 랜선 자르기

# 이진 탐색
def binSearch(n, start, end):
    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for line in lines:
            cnt += (line // mid)

        if cnt >= n:
            cut.append(mid)
            start = mid + 1
        else:
            end = mid - 1

# main
k, n = map(int,input().split())

lines = []
for _ in range(k):
    lines.append(int(input()))

cut = []
binSearch(n,1,max(lines))

print(max(cut))
