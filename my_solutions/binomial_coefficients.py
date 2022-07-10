from test_framework import generic_test
import functools


@functools.lru_cache(None)
def compute_binomial_coefficient(n: int, k: int) -> int:
    # much slower
    if k == 0 or k == n:
        return 1

    first = compute_binomial_coefficient(n - 1, k)
    second = compute_binomial_coefficient(n - 1, k - 1)

    return first + second


# that's the cache, must be outside or every time it would be reset
map = {}


def compute_binomial_coefficient_manual_cache(n: int, k: int) -> int:
    def recursion(n, k, map):
        key = f"{n}:{k}"

        if k in (0, n):
            return 1

        if key in map:
            return map[key]

        n_minus_1_k = compute_binomial_coefficient_manual_cache(n - 1, k)
        n_minus_1_k_minus_1 = compute_binomial_coefficient_manual_cache(n - 1, k - 1)

        map[key] = n_minus_1_k + n_minus_1_k_minus_1
        return map[key]

    return recursion(n, k, map)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('binomial_coefficients.py',
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient_manual_cache))
