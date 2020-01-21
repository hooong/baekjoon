# greedy algorithm
n = int(input())

# 각 사람의 인출 시간입력
time = list(input().split())
p = []
for t in time:
    p.append(int(t))

# 인출시간이 짧은 사람부터 하면 뒤에 대기시간이 짧아질 것이다.
p.sort()

w = []
for i in range(n):
    min_wait = p.pop(0)
    # 처음으로 들어오는건 바로 넣어준다.
    if i == 0:
        w.append(min_wait)
    # 그 다음부터는 대기시간을 더해줘야하므로 앞의 것들을 모두 더한값을 저장해준다.
    else:
        w.append(min_wait+w[i-1])

# w에는 각 사람의 대기시간 + 인출시간이 저장되어 있으므로 다 더한값이 최솟값.
print(sum(w))