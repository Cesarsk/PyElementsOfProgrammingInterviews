from typing import List

from test_framework import generic_test


# sorting is O(n log n) so for on a sorted is n so global runtime is o(n log n)
def smallest_nonconstructible_value(A: List[int]) -> int:
    smallest_constr_value = 0
    for a in sorted(A):
        if a > smallest_constr_value + 1:
            break
        smallest_constr_value += a

    return smallest_constr_value + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('smallest_nonconstructible_value.py',
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
