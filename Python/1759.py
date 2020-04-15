# 1759번 암호 만들기
import sys

#dfs
def dfs(cur,cnt,cnt_v,ps):
    global l, c, arr

    if cnt == l and cnt_v >= 1 and l-cnt_v >= 2:
        print(''.join(ps))

    for i in range(cur+1,c):
        if arr[i] in vowel:
            dfs(i,cnt+1,cnt_v+1,ps+[arr[i]])
        else:
            dfs(i,cnt+1,cnt_v,ps+[arr[i]])


# main
l, c = map(int, input().split())
arr = [x for x in sys.stdin.readline().split()]
arr.sort()      
vowel = ['a', 'e', 'i', 'o', 'u']   # 모음

# 모든 경우 탐색
for i in range(c-l+1):
    if arr[i] in vowel:
        dfs(i,1,1,[arr[i]])
    else:
        dfs(i,1,0,[arr[i]])
        