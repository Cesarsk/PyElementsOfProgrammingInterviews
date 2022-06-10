import collections
from typing import List

from test_framework import generic_test, test_utils


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    # complexity is O(nm log m)
    sorted_string_to_anagrams = collections.defaultdict(list)
    for s in dictionary:
        # access the key 'sorted(s)' and add the s to the hash table
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)

    return [group for group in sorted_string_to_anagrams.values() if len(group) >= 2]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
