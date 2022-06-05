from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2

        # means 'left' can starts from mid + 1
        if A[mid] > A[right]:
            left = mid + 1

        # means there cannot be a solution on the right of 'mid' position
        else:  # A[mid] < A[right]
            right = mid

    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
