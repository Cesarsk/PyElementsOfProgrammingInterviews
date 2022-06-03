import heapq
import itertools
from typing import Iterator, List

from test_framework import generic_test


def sort_approximately_sorted_array(sequence: Iterator[int], k: int) -> List[int]:
    result = []
    min_heap = []

    # adds the first k elements to min_heap
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    # extract the minimum and put it into result, while adding the new element to the heap (pushpop operation)
    for s in sequence:
        result.append(heapq.heappushpop(min_heap, s))

    # the remaining elements in the heap must be processed
    while min_heap:
        result.append(heapq.heappop(min_heap))

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
