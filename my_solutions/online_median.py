import heapq
from typing import Iterator, List

from test_framework import generic_test


def online_median(sequence: Iterator[int]) -> List[float]:
    min_heap, max_heap, result = [], [], []

    for s in sequence:
        # push in max_heap WHAT you pop from min_heap and push s in min_heap
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, s))

        # they either need to have the same number of elements or min_heap must have one more
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        if len(min_heap) == len(max_heap):
            result.append(0.5 * (min_heap[0] + -max_heap[0]))
        else:
            result.append(min_heap[0])

    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
