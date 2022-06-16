import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class Name:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name, self.last_name = first_name, last_name

    def __lt__(self, other) -> bool:
        return (self.first_name < other.first_name
                if self.first_name != other.first_name else
                self.last_name < other.last_name)


# this takes o(n) in space and time
def eliminate_duplicate(A: List[Name]) -> None:
    table = {a.first_name: a.last_name for a in A}
    A = [(a, table[a]) for a in table]
    print("A IS", A)


# this takes o(nlog(n)) for sorting and o(1) for space since it's in place
def eliminate_duplicate_better(A: List[Name]) -> None:
    A.sort()
    write_idx = 1
    for elem in A[1:]:
        if elem.first_name != A[write_idx - 1].first_name:
            A[write_idx] = elem
            write_idx += 1

    del A[write_idx:]


@enable_executor_hook
def eliminate_duplicate_wrapper(executor, names):
    names = [Name(*x) for x in names]

    executor.run(functools.partial(eliminate_duplicate, names))

    return names


def comp(expected, result):
    return all([
        e == r.first_name for (e, r) in zip(sorted(expected), sorted(result))
    ])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('remove_duplicates.py',
                                       'remove_duplicates.tsv',
                                       eliminate_duplicate_wrapper, comp))
