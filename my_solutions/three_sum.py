from typing import List

from test_framework import generic_test


def has_two_sum(A: List[int], t: int) -> bool:
    i, j = 0, len(A) - 1

    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:  # A[i]+A[j] > t
            j -= 1

    return False


# Time complexity is the sum of the time taken to sort O(n log n),
# and then to run the O(n) algorithm to find a pair in a sorted array that sums to a specified value,
# which is O(n^2) overall
def has_three_sum(A: List[int], t: int) -> bool:
    A.sort()
    return any(has_two_sum(A, t - a) for a in A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
