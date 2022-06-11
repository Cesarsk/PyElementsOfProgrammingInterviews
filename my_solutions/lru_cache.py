import collections

from test_framework import generic_test
from test_framework.test_failure import TestFailure


class LruCache:
    def __init__(self, capacity: int) -> None:
        self._isbn_hash_table = collections.OrderedDict()
        self._capacity = capacity

    def lookup(self, isbn: int) -> int:
        if isbn not in self._isbn_hash_table:
            return -1
        price = self._isbn_hash_table.pop(isbn)

        # this update is important to guarantee the LRU behavior since the OrderedDict class guarantee insertion order
        self._isbn_hash_table[isbn] = price
        return price

    def insert(self, isbn: int, price: int) -> None:
        if isbn in self._isbn_hash_table:
            price = self._isbn_hash_table.pop(isbn)

        elif self._capacity <= len(self._isbn_hash_table):
            self._isbn_hash_table.popitem(last=False)  # FIFO behavior: Least Recently Used behavior

        self._isbn_hash_table[isbn] = price

    def erase(self, isbn: int) -> bool:
        # returns None is isbn is absent
        return self._isbn_hash_table.pop(isbn) is not None if isbn in self._isbn_hash_table else None


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure('Lookup: expected ' + str(cmd[2]) +
                                  ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure('Erase: expected ' + str(cmd[2]) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))
