from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    spiral_ordering = []

    for _ in range(len(square_matrix) ** 2):
        spiral_ordering.append(square_matrix[x][y])
        square_matrix[x][y] = 0  # set to 0 the element extracted
        next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]

        # is the next element == 0 (meaning it's already explored) or next_x exceed the range means we need to switch direction
        if (next_x not in range(len(square_matrix))
                or next_y not in range(len(square_matrix))
                or square_matrix[next_x][next_y] == 0):
            # round-robin like, increase in the range 0,3
            direction = (direction + 1) & 3
            next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        x, y = next_x, next_y
    return spiral_ordering


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
