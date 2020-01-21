n, m = map(int, input().split())

card = input().split()

result = 0

# 브루트 포스
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            add = int(card[i]) + int(card[j]) + int(card[k])
            if add <= m:            # m보다 넘지않는 조건
                if result == 0:     # 초기값 셋팅
                    result = add
                elif abs(result-m) > abs(add-m):    # 차이가 제일 적게나는 경우
                    result = add
print(result)