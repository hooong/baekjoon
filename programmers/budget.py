def solution(d, budget):
    answer = 0
    
    d.sort()
    for d_ in d:
        budget -= d_
        if budget < 0:
            return answer
        answer += 1

    return answer

if __name__ == '__main__':
    print(solution([1,3,2,5,4], 9))