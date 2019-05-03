n = int(input())
count = 0

#n번 반복하기
for i in range(n):
    s = input()
    s_set = set(s)                      # set으로 만들어서 반복제거
    result = True

    # 포함된 알파벳들을 하나씩 확인
    for j in s_set:
        index = s.find(j)
        while index != len(s)-1 and s[index] == s[index+1]:   # 반복되는 만큼 index이동
            index += 1
        if index != s.rfind(j):           # 반복의 끝이랑 오른쪽부터 찾은 index가 같으면 그룹단어
            result = False

    if result == True:
        count += 1

print(count)
