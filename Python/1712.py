a, b, c = map(int,input().split())

if c-b <= 0:		# 노트북판매가격이 만드는 비용보다 크면 이익발생 안됨
	print(-1)
else:
	x = a // (c-b)
	if c*x > a + b*x:
		print(x)
	else:
		print(x+1)