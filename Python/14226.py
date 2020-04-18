# 14226번 이모티콘
from collections import deque

# bfs
def bfs(s):
    q = deque()
    q.append([1,0,0])

    visited = [[False for _ in range(s+1)] for _ in range(s+1)]
    visited[1][0] = True

    while q:
        display, clip, cnt = q.popleft()

        if display == s:
            return cnt

        # 1번 연산 - 현재 이모티콘 클립보드에 저장
        if not visited[display][display]:
            visited[display][display] = True
            q.append([display, display, cnt+1])

        # 2번 연산 - 화면에 클립보드를 복사
        if display+clip <= s:
            if not visited[display+clip][clip]:
                visited[display+clip][clip] = True
                q.append([display+clip, clip, cnt+1])

        # 3번 연산 - 화면에서 하나 삭제
        if display - 1 >= 0:
            if not visited[display-1][clip]:
                visited[display-1][clip] = True
                q.append([display-1, clip, cnt+1])

# main
s = int(input())
print(bfs(s))
