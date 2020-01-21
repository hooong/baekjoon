# n = 6까지 해본 결과 피보나치 수열의 관계를 찾음.

n = int(input())

# n이 0이나 1이면 n 출력
if n == 0 or n == 1:
    print(n)
# 아니면 배열에 추가해주면서 전전과 전 수를 더해서 저장해줌.
else:
    fibonacci = [0,1]

    for i in range(2,n+2):
        fibonacci.append((fibonacci[i-2] + fibonacci[i-1]) % 15746)


    result = fibonacci[n+1]
    print(result)

# 첫 시도 메모리초과
# 배열에 저장할때 15746으로 나눠주면 메모리초과 해결 
# => 왜냐하면 int범위를 넘어가 버리므로 숫자가 너무 크게 배열에 저장됨.
