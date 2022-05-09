import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
import string


def int_to_string(x: int) -> str:
    s = []

    sign = None
    if x < 0:
        sign = "-"
        x *= -1

    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    if sign:
        s.insert(len(s), sign)

    return ''.join(reversed(s))


def string_to_int(s: str) -> int:
    result = 0
    sign = -1 if s[0] == "-" else 1
    multi = 1

    for e in reversed(s):
        if e == "+" or e == "-":
            break
        result += multi * string.digits.index(e)
        multi = multi * 10

    return result * sign


def string_to_int_v2(s: str) -> int:
    return functools.reduce(lambda running_sum, c: running_sum * 10 + string.digits.index(c), s[s[0] == '-':], 0) \
           * (-1 if s[0] == '-' else 1)


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
