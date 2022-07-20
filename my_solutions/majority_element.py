from typing import Iterator

from test_framework import generic_test


# Time Complexity is O(n) since we scroll every element of the stream and each operation is O(1)
def majority_search(stream: Iterator[str]) -> str:
    candidate = None
    count = 0

    for it in stream:
        if count == 0:
            candidate = it
            count = 1
        elif candidate == it:
            count += 1
        else:
            count -= 1

    return candidate


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
