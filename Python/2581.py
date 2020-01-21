m = int(input())
n = int(input())

prime_num = []

for num in range(m,n+1):
	if m == 1:
		pass
	for i in range(2,num+1):
		if i == num:
			prime_num.append(num)
		if num % i == 0:
			break

prime_num.sort()

if len(prime_num) == 0:
	print(-1)
else:
	print(sum(prime_num))
	print(prime_num[0])
