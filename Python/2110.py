# 2110번 공유기 설치

# 이진 탐색
def binSearch(start,end,c):
    while start <= end:
        mid = (start + end) // 2

        cnt = 1
        cur = houses[0]
        for i in range(len(houses)):
            if (houses[i] - cur) >= mid:
                cnt += 1
                cur =  houses[i]
        
        if cnt >= c:
            p_len.append(mid)
            start = mid + 1
        else:
            end = mid - 1

# main
n, c = map(int, input().split())

houses = []
for _ in range(n):
    houses.append(int(input()))

# 집을 순서대로 정렬
houses.sort()

p_len = []
binSearch(1,houses[-1] - houses[0],c)

print(max(p_len))