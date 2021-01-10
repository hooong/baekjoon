# 1450번 냅색문제

def a_brute_force(l, w):
    if l >= len(a_weight):
        a_sum.append(w)
        return

    a_brute_force(l + 1, w)
    a_brute_force(l + 1, w + a_weight[l])


def b_brute_force(l, w):
    if l >= len(b_weight):
        b_sum.append(w)
        return

    b_brute_force(l + 1, w)
    b_brute_force(l + 1, w + b_weight[l])


def lower_bound(start, end, key):
    global cnt

    while start < end:
        mid = (start + end) // 2

        if b_sum[mid] <= key:
            start = mid + 1
        else:
            end = mid
    return end


n, c = map(int, input().split())
weight = list(map(int, input().split()))
cnt = 0

a_weight = weight[:n // 2]
b_weight = weight[n // 2:]

a_sum = []
b_sum = []
a_brute_force(0, 0)
b_brute_force(0, 0)
b_sum.sort()

for i in a_sum:
    if c - i < 0:
        continue
    cnt += (lower_bound(0, len(b_sum), c - i))

print(cnt)
