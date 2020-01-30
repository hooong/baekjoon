# 테스트 케이스 개수
t = int(input())

for _ in range(t):
    # 수행 함수
    p = list(input())

    # 배열 입력
    n = int(input())
    arr = input()[1:2*n].split(',')    # '[]'와 ','지우고 원소들만 담음.



    # 시간초과
    # no_arr = True
    # while len(p) != 0:
    #     if p.pop(0) == 'R':
    #         arr = arr[::-1]
    #     else:
    #         if len(arr) == 0:
    #             print('error')
    #             no_arr = False
    #             break
    #         arr.pop(0)
    
    # if no_arr:
    #     print(arr)