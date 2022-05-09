from typing import List

from test_framework import generic_test

"""
[
[0, 3, 2| 0, 0, 0| 8, 0, 4],
[8, 0, 0| 2, 0, 0| 0, 7, 0],
[0, 1, 7| 0, 0, 5| 9, 0, 6],
--------|--------|---------
[5, 8, 0| 0, 2, 0| 0, 3, 0],
[0, 0, 6| 0, 4, 0| 7, 0, 0],
[0, 0, 4| 9, 1, 3| 0, 6, 0],
--------|--------|---------
[0, 0, 0| 7, 3, 0| 2, 0, 0],
[0, 5, 9| 0, 0, 0| 0, 0, 1],
[1, 0, 0| 8, 0, 9| 0, 0, 0]
]
"""
"""
[
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[7, 0, 0, 5, 9, 8, 0, 2, 1],
[0, 1, 0, 4, 0, 0, 9, 0, 3],
--------|--------|---------
[3, 0, 6, 7, 0, 0, 4, 0, 8],
[8, 2, 0, 1, 5, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 3, 0, 0, 0],
--------|--------|---------
[0, 8, 4, 3, 0, 7, 0, 5, 0],
[6, 9, 0, 0, 0, 0, 2, 0, 0],
[1, 3, 0, 0, 0, 2, 8, 0, 7]]
"""


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    def check_column(sudoku, index_row, index_col):
        elem = sudoku[index_row][index_col]
        col = [row[index_col] for row in sudoku]

        for i in range(len(col)):
            if col[i] == elem and i != index_row:
                return False

        return True

    def check_row(sudoku, index_row, index_col):
        row = sudoku[index_row]
        elem = sudoku[index_row][index_col]
        for i in range(len(row)):
            if row[i] == elem and i != index_col:
                return False

        return True

    def check_subarray(sudoku, index_row, index_col):
        # the formula is n - (n%3)
        start_r = index_row - (index_row % 3)
        start_c = index_col - (index_col % 3)
        elem = sudoku[index_row][index_col]

        for i in range(start_r, start_r + 3):
            for j in range(start_c, start_c + 3):
                if elem == sudoku[i][j] and (i != index_row or j != index_col):
                    return False
        return True

    for i in range(len(partial_assignment)):
        for j in range(len(partial_assignment)):
            if partial_assignment[i][j] == 0:
                continue
            if not (check_row(sudoku=partial_assignment, index_row=i, index_col=j) and \
                    check_column(sudoku=partial_assignment, index_row=i, index_col=j) and \
                    check_subarray(sudoku=partial_assignment, index_row=i, index_col=j)):
                return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
