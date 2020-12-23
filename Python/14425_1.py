# 14425번 문자열 집합 (트라이)
from sys import stdin


class Node:
    def __init__(self, key):
        self.key = key
        self.child = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
        cur.child['*'] = True

    def search(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur.child:
                return False
            cur = cur.child[ch]
        if '*' in cur.child:
            return True


n, m = map(int, stdin.readline().split())
trie = Trie()
cnt = 0

for _ in range(n):
    s = stdin.readline()
    trie.insert(s)

for _ in range(m):
    candidate = stdin.readline()

    if trie.search(candidate):
        cnt += 1

print(cnt)
