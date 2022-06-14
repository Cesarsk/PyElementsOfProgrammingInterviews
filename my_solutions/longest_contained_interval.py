from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    unprocessed_entries = set(A)  # remove duplicated elements
    max_interval_size = 0
    while unprocessed_entries:
        a = unprocessed_entries.pop()
        lower_bound = a - 1
        while lower_bound in unprocessed_entries:
            unprocessed_entries.remove(lower_bound)
            lower_bound = lower_bound - 1

        upper_bound = a + 1
        while upper_bound in unprocessed_entries:
            unprocessed_entries.remove(upper_bound)
            upper_bound = upper_bound + 1

        max_interval_size = max(max_interval_size, upper_bound - lower_bound - 1)

    return max_interval_size


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
