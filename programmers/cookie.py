def solution(cookie):
    answer = 0

    for i in range(len(cookie)-1):
        f_idx = i
        e_idx = i+1
        f_value = cookie[i]
        e_value = cookie[i+1]

        while True:
            if f_value == e_value:
                answer = max(answer, f_value)

            if f_value <= e_value and f_idx > 0:
                f_idx -= 1
                f_value += cookie[f_idx] 
            elif f_value >= e_value and e_idx < len(cookie)-1:
                e_idx += 1
                e_value += cookie[e_idx]
            else:
                break

    return answer

if __name__ == '__main__':
    print(solution([1,1,2,3]))