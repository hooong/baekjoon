# 14002번 가장 긴 증가하는 부분 수열 4
import sys

# main
n = int(input())
seq = [int(x) for x in sys.stdin.readline().split()]

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j]+1)

l_cnt = max(dp)
print(l_cnt)

idx = dp.index(l_cnt)
aSeq = []

# 긴 수열 찾아내기
while idx >= 0:
    if dp[idx] == l_cnt:
        aSeq.append(seq[idx])
        l_cnt -= 1
    idx -= 1

for num in aSeq[::-1]:
    print(num, end = ' ')
print()# 14002번 가장 긴 증가하는 부분 수열 4
import sys

# main
n = int(input())
seq = [int(x) for x in sys.stdin.readline().split()]

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j]+1)

l_cnt = max(dp)
print(l_cnt)

idx = dp.index(l_cnt)
aSeq = []

# 긴 수열 찾아내기
while idx >= 0:
    if dp[idx] == l_cnt:
        aSeq.append(seq[idx])
        l_cnt -= 1
    idx -= 1

for num in aSeq[::-1]:
    print(num, end = ' ')
print()


