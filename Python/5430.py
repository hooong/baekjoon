from collections import deque
# 테스트 케이스 개수
t = int(input())

for _ in range(t):
    # 수행 함수
    p = list(input())

    # 배열 입력
    n = int(input())
    arr = deque(input()[1:-1].split(','))    # '[]'와 ','지우고 원소들만 담음.
    if n == 0:
        arr = deque([])

    # 뒤집기 여부(T:뒤집힌상태, F:원래상태)
    isR = False
    # error 여부
    no_arr = True

    for i in range(len(p)):
        # R이 나올때마다 뒤집음.
        if p[i] == 'R':
            isR = not isR
        else:
            if len(arr) == 0:
                print('error')
                no_arr = False
                break
            else:
                # 뒤집힌 상태라면 뒤에서 제거
                if isR:
                    arr.pop()
                # 원래 상태면 앞에서 제거
                else:
                    arr.popleft()
    
    if no_arr:
        arr = list(arr)
        if isR:
            arr.reverse()

        print('[', end='')
        print(','.join(arr), end='')
        print(']')

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