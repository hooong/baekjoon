def solution(n, computers):
    global visited, count
    
    visited = [0 for _ in range(n)]
    count = 1

    for i in range(n):
        if visited[i] == 0:
            visited[i] = count
            dfs(i, n, computers)
            count += 1

    answer = max(visited)
    return answer

def dfs(cur, n, c):
    for i in range(n):
        if c[cur][i] == 1 and visited[i] == 0:
            visited[i] = count
            dfs(i, n, c)

if __name__ == '__main__':
    print(solution(3,[[1,1,0],[1,1,0],[0,0,1]]))