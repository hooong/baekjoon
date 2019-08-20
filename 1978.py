n = int(input())

nums = input().split()
count = 0

for i in range(n):
	num = int(nums[i])			# 배열안에서 차례대로 int형으로 꺼냄
	if num == 1:
		pass
	else:
		for j in range(2,num+1):
			if j == num:		# 2부터 자기자신까지 안나뉘면 count 1증가
				count += 1
			if num % j == 0:	# 1과 자기 자신이 아닌데 나뉘어지면 break
				break

print(count)