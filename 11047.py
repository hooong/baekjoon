n, k = map(int, input().split())

values = []
for _ in range(n):
    values.append(int(input()))

# 큰 값부터 접근하기위함.
values = values[::-1]
count = 0
# 큰 값부터 k에서 뺄수있는만큼씩 빼준다.
for value in values:
    if k == 0:
        break
    elif k < value:
        continue
    else:
        # 같거나 클때는 계속 value값을 빼준다.
        while k >= value:
            k -= value
            count += 1
        
print(count)

# 원래는 까다로운 문제이지만 여기서 value의 조건이 i번째 value는 i-1번째의 배수라는 조건덕분에 쉽다.