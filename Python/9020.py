t = int(input())

ns = []
for _ in range(t):
    n = int(input())
    ns.append(n)

# 에라토스테네스의 체
def eratos(n,nums):
    for i in range(2,n+1):
        for j in range(i*2,n+1,i):
            nums[j] = True

for n in ns:
    nums = [False for i in range(n+1)]
    eratos(n,nums)

    # 처음에는 2로 나눈 수로 초기화
    a = n//2
    b = a

    while True:
        # a,b가 모두 소수이면 출력
        if (nums[a] == False) and (nums[b] == False):
            print(a,b)
            break
        # a,b 둘중 하나라도 소수가 아니면 a는 -1, b는 +1을 해준다.
        else:
            a -= 1
            b += 1