t = int(input())

def count_zero_or_one(n):
    # n이 0이나 1이면 n 출력
    if n == 0:
        return [1,0]
    elif n == 1:
        return [0,1]
    # 아니면 배열에 추가해주면서 전전과 전 수를 더해서 저장해줌.
    else:
        fibonacci = [0,1]
        # 0과 1일때의 0,1 출력 횟수를 저장해놓음
        count = {0:[1,0], 1:[0,1]}

        for i in range(2,n+1):
            # 반복할때마다 각 수의 i-1과 i-2의 출력횟수를 차례로 더해주고 저장.
            count[i] = [count[i-2][0]+count[i-1][0], count[i-2][1]+count[i-1][1]]
            fibonacci.append(fibonacci[i-2] + fibonacci[i-1])

        return count[n]

nums = []
for _ in range(t): 
    nums.append(int(input()))

result = []
for n in nums:
    result.append(count_zero_or_one(n))

for i in result:
    print(i[0],i[1])


# 0,1 출력은 dictionary로 저장.

# 시간초과

# def fibo(n):
#     fibonacci = [0 for _ in range(n+1)]
#     if n == 0:
#         fibonacci[0] = 0
#         count[0] += 1
#         return 0
#     elif n == 1:
#         fibonacci[1] = 1
#         count[1] += 1
#         return 1
#     else:
#         fibonacci[n] = fibo(n-1) + fibo(n-2)
    
#     return fibonacci[n]

# t = int(input())

# nums = []
# global count
# for _ in range(t):
#     nums.append(int(input()))

# for n in nums:
#     count = {0:0,1:0}
#     fibo(n)
#     print(count[0],count[1])
