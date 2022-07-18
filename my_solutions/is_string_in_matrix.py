from typing import List

from test_framework import generic_test


def is_pattern_contained_in_grid(grid: List[List[int]], pattern: List[int]) -> bool:
    def check_presence(x, y, offset_pattern):
        if len(pattern) == offset_pattern:
            return True

        # if not known to fail
        if (x, y, offset_pattern) not in failed_attempts:
            # if inside the grid
            if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
                # if the element matches
                if pattern[offset_pattern] == grid[x][y]:
                    # if not known to fail
                    if any(check_presence(x + a, y + b, offset_pattern + 1)
                           for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                        return True

        failed_attempts.add((x, y, offset_pattern))
        return False

    failed_attempts = set()
    return any(check_presence(x, y, 0) for x in range(len(grid)) for y in range(len(grid[x])))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
