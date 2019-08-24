n = int(input())

# 브루트 포스
i = 1                           # i를 1부터 모두 검사
while True:
    if i > n:                   # i가 n보다 크다는 얘기는 생성자 없음.
        print(0)
        break
    result = i
    for num in str(i):          # i에 각 자리수 더함.
        result += int(num)
    if result == n:             # 다 더한 값이 n이랑 같으면 i 출력
        print(i)
        break
    i += 1