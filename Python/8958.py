#점수매기기
def score(test_case):
    result = 0
    o = 0
    for i in test_case:
        if i == 'O':
            o += 1
        else:
            o = 0
        result += o
    return result     

#입력개수
n = int(input())

#결과값저장 리스트
result_list = []

#입력
for i in range(n):
    input_str = input()
    result_list.append(score(input_str))

#출력
for i in result_list:
    print(i)

