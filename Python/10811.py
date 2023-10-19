n, m = map(int, input().split(" "))
arr = [x for x in range(1, n + 1)]
for _ in range(m):
    i, j = map(int, input().split(" "))
    tmp = arr[i - 1 : j]
    arr[i - 1 : j] = tmp[::-1]
print(" ".join([str(x) for x in arr]))
