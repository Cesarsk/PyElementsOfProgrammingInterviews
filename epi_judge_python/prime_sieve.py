from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n. Time complexity is O(nlog(log(n))) while Space is O(n)
def generate_primes(n: int) -> List[int]:
    primes = []

    # boolean array of canditates prime numbers
    is_prime = [False, False] + [True] * (n - 1)

    # scroll the array up to n+1 (because last element is excluded)
    for i in range(2, n + 1):

        # if it's a potential candidate, enter
        if is_prime[i]:

            # add it to primes' list, next instruction you will understand why
            primes.append(i)

            # set the i's multiples of itself to False, because every multiple of a number can't be a prime number
            for j in range(i, n + 1, i):
                is_prime[j] = False

    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
