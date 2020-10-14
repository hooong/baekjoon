# 1422번 숫자의 신
import heapq
from functools import cmp_to_key

def compare(a, b):
    return int(str(a)+str(b)) - int(str(b)+str(a))

k, n = map(int, input().split())
nums = [int(input()) for _ in range(k)]

max_num = max(nums)
for _ in range(n - len(nums)):
    nums.append(max_num)
nums= sorted(nums, key=cmp_to_key(lambda a, b: -1 if int(str(a)+str(b)) > int(str(b)+str(a)) else 1))
print(*nums, sep='')
