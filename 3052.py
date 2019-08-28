nums = []

for _ in range(10):
    nums.append(int(input()))

remainder = []
for num in nums:
    remainder.append(num%42)

# set으로 변환시켜 중복되는 수 제거
remainder_set = set(remainder)

print(len(remainder_set))