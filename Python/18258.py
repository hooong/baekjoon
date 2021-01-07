# 18258번 큐 2
from collections import deque
from sys import stdin


def push(num):
    global q

    q.append(num)


def pop():
    global q

    try:
        return q.popleft()
    except:
        return -1


def size():
    global q

    return len(q)


def is_empty():
    global q

    return True if size() == 0 else False


def front():
    global q

    return -1 if is_empty() else q[0]


def back():
    global q

    return -1 if is_empty() == 1 else q[-1]


q = deque()
for _ in range(int(stdin.readline())):
    command = stdin.readline().strip().split()
    op = command[0]

    if op == 'push':
        push(command[1])
    elif op == 'pop':
        print(pop())
    elif op == 'size':
        print(size())
    elif op == 'empty':
        print(1 if is_empty() else 0)
    elif op == 'front':
        print(front())
    elif op == 'back':
        print(back())
