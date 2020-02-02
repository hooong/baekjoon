# 1629번 곱셈

# B를 2분할해가면서 곱셈 진행
def devide(a,n):
    # c로 나눈 나머지므로 계속 나눈 나머지를 곱해도 결과는 동일.
    # 여기서 % c를 해주지 않으면 시간초과
    if n==1:
        return a % c
    elif n==2:
        return a*a % c
    else:
        tmp = devide(a,n//2)
        if n%2 == 0:
            return tmp*tmp % c
        else:
            return tmp*tmp*a % c

a,b,c = map(int,input().split())

result = devide(a,b)
print(result)