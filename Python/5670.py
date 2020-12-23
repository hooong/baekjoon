# 5670번 휴대폰 자판
from sys import stdin


class Node:
    def __init__(self, key, count=0):
        self.key = key
        self.child = {}
        self.count = count


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
            cur.count += 1
        cur.child['*'] = True


def find_click(l, cur, before_size):
    global cnt

    if len(cur.child) > 1 or l == 0:
        for c in cur.child:
            if c != '*':
                cnt += cur.child[c].count

    for c in cur.child:
        if c != '*':
            find_click(l+1, cur.child[c], len(cur.child))


try:
    while True:
        n = int(stdin.readline())
        trie = Trie()
        cnt = 0

        for _ in range(n):
            trie.insert(stdin.readline().strip('\n'))

        find_click(0, trie.head, len(trie.head.child))
        print("{:,.2f}".format(round((cnt / n), 2)))
except:
    exit(0)

