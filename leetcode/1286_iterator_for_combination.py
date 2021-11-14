import itertools


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combination_list = list(itertools.combinations(characters, combinationLength))

    def next(self) -> str:
        if self.hasNext():
            tmp = self.combination_list.pop(0)
            return ''.join(tmp)
        else:
            raise Exception()

    def hasNext(self) -> bool:
        return bool(len(self.combination_list))

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()


def test():
    itr = CombinationIterator('abc', 2)

    assert itr.next() == 'ab'
    assert itr.hasNext() is True
    assert itr.next() == 'ac'
    assert itr.hasNext() is True
    assert itr.next() == 'bc'
    assert itr.hasNext() is False
