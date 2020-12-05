# 4195번 친구 네트워크
import sys


def set_index(f):
    global network, size

    if not f in network:
        network[f] = f
        size[f] = 1

    return network[f]


def find(x):
    global network

    if network[x] == x:
        return x

    network[x] = find(network[x])
    return network[x]


def union(x, y):
    global network

    x = find(x)
    y = find(y)

    if not x == y:
        if size[x] < size[y]:
            x, y = y, x

        network[y] = x
        size[x] += size[y]

    print(size[x])


for _ in range(int(sys.stdin.readline())):
    f = int(sys.stdin.readline())
    network, size = {}, {}

    for _ in range(f):
        f1, f2 = sys.stdin.readline().split()
        f1 = set_index(f1)
        f2 = set_index(f2)

        union(f1, f2)
