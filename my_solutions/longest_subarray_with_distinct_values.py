from typing import List

from test_framework import generic_test


def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    most_recent_occurrences = {}
    start_idx = result = 0
    for idx, a in enumerate(A):
        if a in most_recent_occurrences:
            dup_idx = most_recent_occurrences[a]
            if dup_idx >= start_idx:
                result = max(result, idx - start_idx)
                start_idx = dup_idx + 1
        most_recent_occurrences[a] = idx

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
