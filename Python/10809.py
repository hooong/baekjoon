S = str(input())
alpha_dict = {}

#모든 알파벳 소문자를 담은 배열
alpha_list=['a','b','c','d',
            'e','f','g','h',
            'i','j','k','l',
            'm','n','o','p',
            'q','r','s','t',
            'u','v','w','x','y','z']

#dict에 알파벳 위치 저장
for i in alpha_list:
    alpha_dict[i] = S.find(i)

#출력
for i in alpha_list:
    print(alpha_dict[i], end = ' ')