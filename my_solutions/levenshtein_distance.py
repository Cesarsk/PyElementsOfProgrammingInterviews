from test_framework import generic_test
import functools


def levenshtein_distance(A: str, B: str) -> int:
    @functools.lru_cache(None)
    def compute_distance_between_prefixes(A_idx, B_idx):
        if A_idx < 0:  # meaning if A is an empty string
            return B_idx + 1  # which is len(B)
        elif B_idx < 0:  # meaning if B is an empty string
            return A_idx + 1  # which is len(A)

        if A[A_idx] == B[B_idx]:
            return compute_distance_between_prefixes(A_idx - 1, B_idx - 1)

        replace_last = compute_distance_between_prefixes(A_idx - 1, B_idx - 1)
        add_last = compute_distance_between_prefixes(A_idx - 1, B_idx)
        delete_last = compute_distance_between_prefixes(A_idx, B_idx - 1)

        return 1 + min(replace_last, add_last, delete_last)

    return compute_distance_between_prefixes(len(A) - 1, len(B) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
