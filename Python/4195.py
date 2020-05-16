# 4195번 친구 네트워크
from collections import deque
import sys
input = sys.stdin.readline

# 이름을 숫자로 변환
def findPerson(name):
    global persons, parents
    
    if not name in persons.keys():
        persons[name] = len(persons)
        parents.append(persons[name])

    return persons[name]

# find
def find(x):
    global parents

    while True:
        if parents[x] == x:
            return x
        x = parents[x]

# union
def union(a,b):
    global parents

    a = find(a)
    b = find(b)

    if not a == b:
        parents[b] = a

# main
t = int(input())

for _ in range(t):
    f = int(input())
    
    persons = {'':0}
    parents = [0]
    for _ in range(f):
        n1, n2 = input().split()

        # 이름을 숫자로 바꿈
        p1 = findPerson(n1)
        p2 = findPerson(n2)

        # 친구 관계 형성
        union(p1, p2)

        # 친구 관계의 수
        count = 0
        tmp = find(p1)
        for i in range(1,len(parents)):
            if find(i) == tmp:
                count += 1
            
        print(count)
