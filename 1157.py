import operator

s = input().upper()     # 대소문자 구별을 안하므로 대문자로 바꿔줌
result_dict = {}        # 개수를 세기위한 딕셔너리

for i in s:
    if i not in result_dict:    # 처음나오면 1로 저장
        result_dict[i] = 1
    else:                       # 또 나온거면 1 증가
        result_dict[i] += 1

# value를 기준으로 정렬
result = dict(sorted(result_dict.items(), key=operator.itemgetter(1),reverse=True))
result_values = list(result.values())
result_keys = list(result.keys())

# 가장 큰 수가 한개뿐인지 구별해내기
if result_values.count(result_values[0]) != 1:
    print('?')
else:
    print(result_keys[0])



