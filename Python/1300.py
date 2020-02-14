# 1300번 K번째 수

# 이분 탐색
def binSearch(start, end, n, k):
    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for i in range(1,n+1):
            cnt += min(mid // i, n)
        
        if cnt >= k:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer

# main
n = int(input())
k = int(input())

print(binSearch(1, n*n, n, k))
