from test_framework import generic_test
from typing import Set


# version 1: no optimizations:
# Average running time:    9s
# Median running time:    59 ms
def test_collatz_conjecture_v1(n: int) -> bool:
    # we start from 3.
    for i in range(3, n + 1):
        number = i

        while number != 1:
            number = (number * 3) + 1 if not number % 2 else number / 2

    return True


# Average running time:  976 ms
# Median running time:     4 ms
def test_collatz_conjecture_v2(n: int) -> bool:
    # we start from 3, skipping even numbers because we know it converges at 1
    for i in range(3, n + 1, 2):
        number = i

        while number != 1:
            if number % 2:  # odd
                number = (number * 3) + 1
            else:
                number /= 2

    return True


# Average running time:  113 ms
# Median running time:   714 us
def test_collatz_conjecture_v3(n: int) -> bool:
    # we start from 3, skipping even numbers because we know it converges at 1
    verified_numbers = set()
    for i in range(3, n + 1, 2):
        number = i

        while number != 1:
            if number % 2:  # odd
                number = (number * 3) + 1
            else:
                number /= 2
            if number in verified_numbers:
                break

        verified_numbers.add(i)

    return True


# Average running time:   80 ms
# Median running time:   474 us
def test_collatz_conjecture(n: int) -> bool:
    # Stores odd numbers already tested to converge to 1.
    verified_numbers: Set[int] = set()

    # Starts from 3, hypothesis holds trivially for 1.
    for i in range(3, n + 1):
        sequence: Set[int] = set()
        test_i = i
        while test_i >= i:
            if test_i in sequence:
                # We previously encountered test_i, so the Collatz sequence has
                # fallen into a loop. This disproves the hypothesis, so we
                # short-circuit, returning False.
                return False
            sequence.add(test_i)

            if test_i % 2:  # Odd number.
                if test_i in verified_numbers:
                    break  # test_i has already been verified to converge to 1.
                verified_numbers.add(test_i)
                test_i = 3 * test_i + 1  # Multiply by 3 and add 1.
            else:
                test_i //= 2  # Even number, halve it.
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('collatz_checker.py',
                                       'collatz_checker.tsv',
                                       test_collatz_conjecture))
