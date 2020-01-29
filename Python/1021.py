def push_front(n):
    queue.insert(0,n)

def push_back(n):
    queue.append(n)

def pop_front():
    return queue.pop(0)

def pop_back():
    return queue.pop(len(queue)-1)

n, m = map(int, input().split())

queue = list(range(1,n+1))
pickNum = input().split()

count = 0
for num in pickNum:
    pos = queue.index(int(num))
    if pos < len(queue) - pos:
        for _ in range(pos):
            push_back(pop_front())
            count += 1
        pop_front()
    else:
        for _ in range(len(queue)-pos):
            push_front(pop_back())
            count += 1
        pop_front()

print(count)