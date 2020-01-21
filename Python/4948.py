ns = []

while True:
    n = int(input())    
    if not n == 0:
        ns.append(n)
    elif n == 0:
        break

# 에라토스테네스의 체
def eratos(n):
    for i in range(2,n+1):
        for j in range(i*2,n+1,i):
            nums[j] = True

for n in ns:
    nums = [False for i in range(2*n+1)]

    eratos(2*n)
    
    # n보다 큰수니까 n보다 작은소수도 다 True로 바꿔준다.
    for i in range(n+1):
        nums[i] = True

    print(nums.count(False))