# 2475번 검증수
import sys

# main
nums = [int(x) for x in sys.stdin.readline().split()]

result = 0
for n in nums:
    result += n ** 2

print(result % 10)
