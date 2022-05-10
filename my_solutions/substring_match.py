import functools

from test_framework import generic_test


def rabin_karp(t: str, s: str) -> int:
    if len(s) > len(t):
        return -1  # can't possibly be a substring

    BASE = 26
    s_hash = functools.reduce(lambda res, c: res * BASE + ord(c), s, 0)
    t_hash = functools.reduce(lambda res, c: res * BASE + ord(c), t[:len(s)], 0)
    power_s = BASE ** max(0, len(s) - 1)

    for i in range(len(s), len(t)):
        # second check is to avoid collision,
        # i represents the last char analyzed so we want the substring which is i-len(s):i
        if t_hash == s_hash and t[i - len(s):i] == s:
            return i - len(s)  # found a match

        # uses rolling hash: remove first char * power_s
        t_hash -= ord(t[i - len(s)]) * power_s

        # new hash is given by multiplying the reducted hash by BASE (it's a left-shift basically) and then add last char
        t_hash = t_hash * BASE + ord(t[i])

    # t[-len(s):] means: start from the -len(s) char and then go up to the end (direction: right) of the string
    if t_hash == s_hash and t[-len(s):] == s:
        return len(t) - len(s)

    return -1  # s is not a substring of t


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
