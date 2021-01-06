# 1806번 부분합
import sys
INF = sys.maxsize

n, s = map(int, input().split())
seq = list(map(int, input().split()))

# 전체합이 s 이상이 안될 경우
if sum(seq) < s:
    print(0)
else:
    i = 0
    j = 1

    min_len = INF
    sum_seq = seq[i] + seq[j]
    while i < j < len(seq)-1:
        if sum_seq - seq[i] >= s:
            sum_seq -= seq[i]
            i += 1
        else:
            j += 1
            sum_seq += seq[j]
        if sum_seq >= s:
            min_len = min(min_len, j - i + 1)

    # j가 마지막에 도달했고 앞에 지울 수 있는게 존재할 경우
    while i < len(seq):
        if sum_seq - seq[i] >= s:
            sum_seq -= seq[i]
            i += 1
        else:
            break
    min_len = min(min_len, j - i + 1)

    print(min_len)
