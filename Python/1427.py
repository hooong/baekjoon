n = input()

nums = []
for num in list(n):
    nums.append(int(num))

nums.sort(reverse=True)

for num in nums:
    print(num,end='')

# 여기서도 readline()을 써보려했는데 readline을 쓰면 '\n'때문에 위와같이 못씀.
# 따로 처리를 해줘야하는데 귀찮아서 input()으로 해결함