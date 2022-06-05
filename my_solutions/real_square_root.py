import math

from test_framework import generic_test


def square_root(x: float) -> float:
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)

    # while they're not different
    while not math.isclose(left, right):
        mid = (left + right) / 2
        if mid ** 2 < x:
            left = mid
        else:
            right = mid

    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
