m , n = map(int, input().split())

# 에라토네스의 체 사용
nums = [False for i in range(n+1)]

for i in range(2,n+1):              # 2부터 소수들의 배수를 지워나간다.
    for j in range(i*2,n+1,i):
        nums[j] = True              # 소수가 아니면 True
    
for i in range(2,n+1):              # 1을 제외하기위해 2부터 for문을 돌림
    if i >= m:
        if nums[i] == False:
            print(i)