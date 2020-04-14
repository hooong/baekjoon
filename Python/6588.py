# 6588번 골드바흐의 추측

# 에라토스테네스의 채
eratos = [True for _ in range(1000001)]
for i in range(2,1000001):
    if eratos[i]:
        x = i*i
        while x < 1000001:
            eratos[x] = False
            x += i

# main
while True:
    n = int(input())
    
    if n == 0:
        break
    
    isPos = False
    for i in range(3,n,2):      # 3부터 2씩 증가시키면 홀수만 확인
        if eratos[i] and eratos[n-i]:       # 짝수에서 홀수를 빼면 홀수
            a = i
            b = n - i
            isPos = True
            break
        
    if isPos:
        print(str(n) + " = " + str(a) + " + " + str(b))
    else:
        print("Goldbach's conjecture is wrong.")
    