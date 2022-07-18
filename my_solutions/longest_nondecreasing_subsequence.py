from typing import List

from test_framework import generic_test


# Complexity is O(n^2), because each L[i] takes O(n) time to compute. Space complexity is O(n)
def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    max_length = [1] * len(A)

    # scroll every element of the sequence
    for i in range(1, len(A)):
        max_length[i] = max(
            1 + max(
                [max_length[j] for j in range(i) if A[i] >= A[j]], default=0), max_length[i]
        )
    return max(max_length)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_nondecreasing_subsequence.py',
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
