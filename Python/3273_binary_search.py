# 3273번 두 수의 합 (binary_search)


def binary_search(start, end, key):
    if start > end:
        return 0

    mid = (start + end) // 2

    if seq[mid] == key:
        return 1
    elif seq[mid] > key:
        return binary_search(start, mid - 1, key)
    elif seq[mid] < key:
        return binary_search(mid + 1, end, key)


n = int(input())
seq = list(map(int, input().split()))
x = int(input())
answer = 0

seq.sort()

for num in seq:
    if (num * 2) == x:
        continue
    answer += binary_search(0, len(seq) - 1, x - num)

print(answer // 2)
