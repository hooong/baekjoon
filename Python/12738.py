# 12738번 가장 긴 증가하는 부분 수열3


def lower_bound(start, end, num):
    while start < end:
        mid = (start + end) // 2

        if tmp[mid] < num:
            start = mid + 1
        else:
            end = mid
    return end


n = int(input())
arr = list(map(int, input().split()))

tmp = []
index = [[0, 0] for _ in range(n)]
for i in range(len(arr)):
    num = arr[i]
    index[i][1] = num

    if len(tmp) == 0:
        tmp.append(num)
        continue

    if tmp[-1] < num:
        index[i][0] = len(tmp)
        tmp.append(num)
    else:
        idx = lower_bound(0, len(tmp)-1, num)
        index[i][0] = idx
        tmp[idx] = num

answer = []
idx = len(tmp)-1
for i in range(len(index)-1, -1, -1):
    if idx == -1:
        break

    if idx == index[i][0]:
        answer.append(index[i][1])
        idx -= 1

print(len(tmp))
print(*answer[::-1])
