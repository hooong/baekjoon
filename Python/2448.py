# 시간초과
# n = int(input())
# 2차원 배열을 공백으로 다 채운 다음 배열에 별을 찍은 뒤 출력
# list_star = [[' ']*(2*n) for i in range(n)]

# def star(n,x,y):
#     if n == 3:
#         list_star[y][x] = '*'
#         list_star[y+1][x-1] = '*'
#         list_star[y+1][x+1] = '*'
#         list_star[y+2][x-2] = '*'
#         list_star[y+2][x-1] = '*'
#         list_star[y+2][x] = '*'
#         list_star[y+2][x+1] = '*'
#         list_star[y+2][x+2] = '*'
#         return
      # 재귀로 구현
#     star(n//2, x, y)
#     star(n//2, x-(n//2), y+(n//2))
#     star(n//2, x+(n//2), y+(n//2))

# star(n, n-1, 0)

# for i in range(n):
#     for j in range(2*n):
#         print(list_star[i][j], end='')
#     print()

import math

# 가장작은 삼각형 하나
star = ["  *   ", " * *  ", "***** "]

def makestar(shift):
	c = len(star)
	for i in range(c):
		star.append(star[i] + star[i])
		star[i] = ("   " * shift + star[i] + "   " * shift)
		
n = int(input())
k = int(math.log(int(n/3),2))
for i in range(k):
	makestar(int(pow(2,i)))
	
for i in range(n):
	print(star[i])
