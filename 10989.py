import sys
n = int(input())
# counting sort
count = [0] * 10001

for _ in range(n):
    # readline을 써야 빠르다
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(len(count)):
    if count[i] == 0:
        pass
    else:
        for _ in range(count[i]):
            print(i)

# pypy3를 사용해서는 계속 메모리 초과가 떴음.
# python3를 사용했지만 input()을 쓰면 시간초과
# 결국 위처럼 readline()을 사용하니 성공!
