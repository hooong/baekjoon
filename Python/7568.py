n = int(input())

peoples = []
for _ in range(n):              # 키, 몸무게 입력
    people = input().split()
    peoples.append(people)

result = []
for i in range(n):              # 한사람마다 모든 사람과 비교
    k = 0
    for j in range(n):
        # 같은 사람일 경우 pass
        if i==j:
            pass
        # 키와 몸무게를 비교 후 자신보다 덩치가 큰 사람이 있을때마다 k값 증가
        elif (int(peoples[i][0]) < int(peoples[j][0])) and (int(peoples[i][1]) < int(peoples[j][1])):
            k += 1
    result.append(k+1)      # 결과로 k+1 값을 저장

for i in result:
    print(i ,end=' ')