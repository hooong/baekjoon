class Trie:

    def __init__(self):
        self.ch = {}

    def insert(self, word: str) -> None:
        cur = self.ch

        for c in word:
            if c in cur:
                cur = cur[c]
                continue
            else:
                cur[c] = {}
                cur = cur[c]

        cur.update({'*': None})

    def search(self, word: str) -> bool:
        cur = self.ch

        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                return False

        if '*' in cur:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.ch

        for c in prefix:
            if c in cur:
                cur = cur[c]
            else:
                return False
        return True


def test_case():
    trie = Trie()

    assert trie.insert("apple") is None
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    assert trie.insert("app") is None
    assert trie.search("app") is True
