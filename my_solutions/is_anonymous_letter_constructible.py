import collections

from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    anonymous_counter = collections.Counter(letter_text)
    magazine_counter = collections.Counter(magazine_text)

    # for each character in the anonymous letter,
    # the number of times it appears in the anonymous letter
    # is no more than the number of times it appears in the magazine

    # subtract the element of magazine from anonymous. If there are no elements remaining in anonymous_counter
    # it means that the condition is true
    return not anonymous_counter - magazine_counter

    # simple to understand solution
    for a in anonymous_counter.keys():
        if anonymous_counter[a] > magazine_counter[a]:
            return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
