from typing import List

from test_framework import generic_test


# Worst-case complexity is O(n*2^n). If there are few palindromic decompositions the program is much faster than a
# Brute-force approach

def palindrome_decompositions(text: str) -> List[List[str]]:
    def palindrome_helper(offset, partial):
        if len(text) == offset:
            result.append(partial.copy())
            return

        for i in range(offset + 1, len(text) + 1):
            prefix = text[offset: i]
            if prefix == prefix[::-1]:
                palindrome_helper(i, partial + [prefix])

    result = []
    palindrome_helper(offset=0, partial=[])
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'enumerate_palindromic_decompositions.py',
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
