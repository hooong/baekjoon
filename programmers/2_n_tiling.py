def solution(n):
    answer = 0
    before = 1

    for i in range(1,n+1):
        if i == 1:
            answer = 1
        elif i == 2:
            answer = 2
        else:
            tmp = answer

            answer = (answer + before) % 1000000007
            before = tmp

    return answer % 1000000007

if __name__ == '__main__':
    print(solution(6))