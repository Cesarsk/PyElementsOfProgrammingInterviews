from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    # n means n layers so let's start by creating a list of lists of n layers (n rows)
    pascal = [[1] * (i + 1) for i in range(n)]

    # scroll all the rows up to n
    for i in range(n):

        # scroll all columns starting from 1 and going to i
        for j in range(1, i):
            pascal[i].insert(j, pascal[i - 1][j] + pascal[i - 1][j - 1])

    return pascal


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
