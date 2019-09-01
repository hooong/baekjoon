# DP 피보나치
n = int(input())

# n이 0이나 1이면 n 출력
if n == 0 or n == 1:
    print(n)
# 아니면 배열에 추가해주면서 전전과 전 수를 더해서 저장해줌.
else:
    fibonacci = [0,1]

    for i in range(2,n+1):
        fibonacci.append(fibonacci[i-2] + fibonacci[i-1])

    result = fibonacci[n]
    print(result)