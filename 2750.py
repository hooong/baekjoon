n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))

# 정렬
nums.sort()

for num in nums:
    print(num)