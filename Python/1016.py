# 1016번 제곱 ㄴㄴ수
import math

# 에라토스테네스 채
def ertos(num):
    global prime
    arr = [True for _ in range(num+1)]

    for i in range(2,num+1):
        if arr[i]:
            prime.append(i**2)
            x = i * i
            while x <= num:
                arr[x] = False
                x += i

# main
minNum, maxNum = map(int,input().split())

prime = []
ertos(int(math.sqrt(maxNum)))

count = maxNum - minNum + 1
for num in range(minNum,maxNum+1):
    for p in prime:
        if num % p == 0:
            count -= 1
            break

print(count)
