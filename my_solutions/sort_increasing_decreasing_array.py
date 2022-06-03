import heapq
from typing import List

from test_framework import generic_test

INCREASING, DECREASING = range(2)


# example: 57, 131, 493, 294, 221, 339 , 418, 452, 442, 190
def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    sorted_subarrays = []
    subarray_type = INCREASING
    start_idx = 0

    for i in range(1, len(A) + 1):

        # this is the "reversing" condition, when the array switches from increasing to decreasing (and viceversa)
        if (
                i == len(A) or  # A is ended
                (A[i - 1] < A[i] and subarray_type == DECREASING) or
                (A[i - 1] >= A[i] and subarray_type == INCREASING)
        ):
            sorted_subarrays.append(
                # add the subarray made by start_idx: i if INCREASING else add REVERSED subarray to the list
                A[start_idx: i] if subarray_type == INCREASING else A[i - 1: start_idx - 1: -1]
            )
            start_idx = i
            subarray_type = INCREASING if subarray_type == DECREASING else DECREASING

    # recall previous exercise, sorted_arrays_merge.py
    # in this case we use the one-line pythonic solution
    return list(heapq.merge(*sorted_subarrays))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
