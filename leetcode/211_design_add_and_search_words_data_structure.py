class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        cur = self.trie

        for ch in word:
            if ch not in cur.keys():
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = {}

    def search(self, word: str) -> bool:
        check = False

        def dfs(level, cur):
            nonlocal check

            if level == len(word):
                if '*' in cur.keys():
                    check = True
                return

            ch = word[level]
            if ch == '.':
                for candidate in cur.keys():
                    dfs(level + 1, cur[candidate])
            else:
                if ch not in cur.keys():
                    return
                dfs(level + 1, cur[ch])

        dfs(0, self.trie)
        return check


def test():
    wd = WordDictionary()

    wd.addWord("a")
    wd.addWord("ab")
    assert wd.search("a") is True
    assert wd.search("a.") is True
    assert wd.search("ab") is True
    assert wd.search(".a") is False
    assert wd.search(".b") is True
    assert wd.search("ab.") is False
    assert wd.search(".") is True
    assert wd.search("..") is True
