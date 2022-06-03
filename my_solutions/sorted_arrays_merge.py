import heapq
from typing import List

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    min_heap = []

    iterators_sorted_arrays = [iter(x) for x in sorted_arrays]

    # add first element of every array to the heap
    for i, it in enumerate(iterators_sorted_arrays):
        first_elem = next(it, None)
        if first_elem is not None:
            heapq.heappush(min_heap, (first_elem, i))

    result = []

    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = iterators_sorted_arrays[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
