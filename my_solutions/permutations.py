from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    def recursive_permutations(i):
        if i == len(A) - 1:
            result.append(A.copy())
            return

        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            recursive_permutations(i + 1)
            A[i], A[j] = A[j], A[i]

    result = []
    recursive_permutations(0)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py',
                                        'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
