def solution(n, stations, w):
    answer = 0

    scope = (2*w) + 1

    start = 1
    for i in stations:
        between = (i-w) - start

        if between < 1:
            pass
        else:
            need = between // scope
            if between % scope == 0:
                answer += need
            else:
                answer += need + 1

        start = i+w+1
    
    if start <= n:
        between = n - start
        
        if between == 0:
            return answer + 1
        else:
            need = between // scope

            if between % scope == 0:
                return answer + need
            else:
                return answer + need + 1

    return answer

if __name__ == "__main__":
    print(solution(11, [4,11], 1))