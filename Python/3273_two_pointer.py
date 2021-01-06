# 3273번 두 수의 합 (two pointer)

n = int(input())
seq = list(map(int, input().split()))
x = int(input())
answer = 0

seq.sort()

i = 0
j = len(seq) - 1
while i != j:
    if seq[i] + seq[j] == x:
        answer += 1
        i += 1
    elif seq[i] + seq[j] > x:
        j -= 1
    else:
        i += 1

print(answer)
