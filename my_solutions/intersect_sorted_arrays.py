from typing import List

from test_framework import generic_test

[1,2,3]

def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    len_a, len_b = len(A), len(B)
    iter_a, iter_b = 0, 0
    result = []

    while iter_a < len_a and iter_b < len_b:
        if A[iter_a] < B[iter_b]:
            iter_a += 1
        elif A[iter_a] > B[iter_b]:
            iter_b += 1
        else:
            if A[iter_a] != A[iter_a - 1] or iter_a == 0:
                result.append(A[iter_a])

            iter_a, iter_b = iter_a + 1, iter_b + 1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
