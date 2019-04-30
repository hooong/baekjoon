# 테스트케이스 수 입력
n = int(input())
result = {}

for i in range(n):
    s = [i for i in input()]
    r = int(s.pop(0))           # r을 빼내기
    s.pop(0)                    # 공백을 없애기위해
    tmp = []
    for j in range(len(s)):
        for k in range(r):
            tmp.extend(s[j])
    result[str(i)] = tmp

for i in range(n):
    for j in result[str(i)]:    # 배열로 저장되서 한번도 for문 돌림.
        print(j,end = '')
    print()