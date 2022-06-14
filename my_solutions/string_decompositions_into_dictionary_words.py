import collections
from typing import List

from test_framework import generic_test


def find_all_substrings(s: str, words: List[str]) -> List[int]:
    def match_all_words_in_dict(start):
        curr_string_to_freq = collections.Counter()
        for i in range(start, start + len(words) * unit_size, unit_size):
            curr_word = s[i:i + unit_size]
            it = word_to_freq[curr_word]  # check whether the word has already been encountered

            if it == 0:  # means no encounter of the word in the string
                return False

            curr_string_to_freq[curr_word] += 1  # word encountered

            if curr_string_to_freq[curr_word] > it:
                return False  # word encountered too many times

        return True

    # assumption, all words have the same length
    unit_size = len(words[0])
    word_to_freq = collections.Counter(words)
    # it's pointless to test the whole word, for sure there's no need of search after len(s)-unit_size*len(words) + 1
    # because the concatenation of the input words would go over the length of the string
    return [i for i in range(len(s) - unit_size * len(words) + 1) if match_all_words_in_dict(i)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'string_decompositions_into_dictionary_words.py',
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
