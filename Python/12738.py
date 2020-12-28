# 12738번 가장 긴 증가하는 부분 수열3


def lower_bound(start, end, num):
    while start < end:
        mid = (start + end) // 2

        if answer[mid] < num:
            start = mid + 1
        else:
            end = mid
    return end


n = int(input())
arr = list(map(int, input().split()))

answer = []
for num in arr:
    if len(answer) == 0:
        answer.append(num)
        continue

    if answer[-1] < num:
        answer.append(num)
    else:
        idx = lower_bound(0, len(answer)-1, num)
        answer[idx] = num

print(len(answer))
