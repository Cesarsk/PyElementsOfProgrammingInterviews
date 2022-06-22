from typing import List

import bintrees as bintrees

from test_framework import generic_test


def find_closest_elements_in_sorted_arrays(sorted_arrays: List[List[int]]) -> int:
    # starts from the max possible distance
    min_distance_so_far = float('inf')

    # init a BST
    iters = bintrees.RBTree()

    # Stores array iterators in each entry
    for idx, sorted_arrays in enumerate(sorted_arrays):
        it = iter(sorted_arrays)
        first_min = next(it, None)
        if first_min is not None:
            iters.insert(
                (first_min, idx), it
            )

    # main algorithm
    while True:
        min_value, min_idx = iters.min_key()
        max_value = iters.max_key()[0]  # extract key
        min_distance_so_far = min(max_value - min_value, min_distance_so_far)
        it = iters.pop_min()[1]  # extract value
        next_min = next(it, None)
        if next_min is None:
            return min_distance_so_far
        iters.insert((next_min, min_idx), it)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_distance_3_sorted_arrays.py',
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
