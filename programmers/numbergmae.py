def solution(A, B):
    answer = 0

    A.sort(reverse=True)
    B.sort(reverse=True)
    
    b_index = 0
    for i in range(len(A)):
        if A[i] < B[b_index]:
            b_index += 1
            answer += 1
    
    return answer

if __name__ == "__main__":
    print(solution([5,1,3,7], [2,2,6,8]))