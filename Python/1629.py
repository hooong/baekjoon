# 1629번 곱셈
def devide(a,n):
    if n==1:
        return a
    elif n==2:
        return a*a
    else:
        tmp = devide(a,n//2)
        if n%2 == 0:
            return tmp*tmp
        else:
            return tmp*tmp*a

a,b,c = map(int,input().split())

result = devide(a,b) % c
print(result)