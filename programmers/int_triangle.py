def solution(triangle):
    size = len(triangle)
    dp = [[0 for _ in range(size+1)] for _ in range(size+1)]

    for i in range(size):
        for j in range(len(triangle[i])):
            cur = triangle[i][j]
            dp[i+1][j+1] = max(cur + dp[i][j], cur + dp[i][j+1])

    answer = max(dp[size])
    return answer

if __name__ == '__main__':
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))