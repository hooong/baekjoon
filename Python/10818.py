n = int(input())

nums_str = input().split()

# 문자열로 받은걸 int형으로 변환
# 아마 이렇게 안해도 str로 sort가 될것 같음. => 안됨.
nums = []
for num in nums_str:
    nums.append(int(num))

nums.sort()

print(nums[0],nums[-1])