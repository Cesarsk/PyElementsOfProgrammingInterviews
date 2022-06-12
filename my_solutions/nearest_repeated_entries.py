from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    word_to_latest_index, minimum_distance = {}, float('inf')
    for idx, word in enumerate(paragraph):
        if word in word_to_latest_index:
            latest_equal_word_idx = word_to_latest_index[word]
            minimum_distance = min(minimum_distance, idx - latest_equal_word_idx)
        word_to_latest_index[word] = idx

    return minimum_distance if minimum_distance != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
