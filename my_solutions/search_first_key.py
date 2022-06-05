from typing import List

from test_framework import generic_test


def search_first_of_k_attempt(A: List[int], k: int) -> int:
    for idx, item in enumerate(A):
        if k == item:
            return idx
    return -1


# solution
def search_first_of_k(A: List[int], k: int) -> int:
    left, right, result = 0, len(A) - 1, -1

    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1
        else:  # A[mid] < k
            left = mid + 1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
