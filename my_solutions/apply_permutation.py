import copy
from typing import List

from test_framework import generic_test

"""
def apply_permutation(perm: List[int], A: List[int]) -> None:
    B = copy.deepcopy(A)
    for i in range(len(A)):
        A[perm[i]] = B[i]

    return
"""

# Time: O(n) Space: O(1)
def apply_permutation(perm: List[int], A: List[int]) -> None:
    for i in range(len(A)):
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            perm[next] -= len(A) # makes it negative
            next = temp

    # restore the array by making it positive again
    perm[:] = [a + len(perm) for a in perm]

    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
