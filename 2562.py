nums = []
for _ in range(9):
    nums.append(int(input()))

# sort를 안쓰는게 편할것같다는 생각을 했음.
# 최댓값이랑 index를 저장
max = nums[0]
count = 1
for i in range(9):
    if max < nums[i]:
        max = nums[i]
        count = i+1

print(max)
print(count)