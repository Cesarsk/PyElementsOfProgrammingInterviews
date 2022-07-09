from test_framework import generic_test
import functools


# Complexity is O(nm) both space and time with n number of rows and m number of columns
def number_of_ways(n: int, m: int) -> int:
    @functools.lru_cache(None)
    def recursion(x, y):
        # base case
        if x == y == 0:
            return 1

        # unexplored cell
        ways_top = 0 if y == 0 else recursion(x, y - 1)
        ways_left = 0 if x == 0 else recursion(x - 1, y)

        # the result is given by the sum of the two subproblems left and top
        return ways_left + ways_top

    return recursion(n - 1, m - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
