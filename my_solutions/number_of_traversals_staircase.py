from test_framework import generic_test


# O(k) time to fill in each entry, time complexity is O(kn). Space O(n)
# expression is F(n,k)=sum(1,k) of F(n-i,k)
def number_of_ways_to_top(stairs: int, k: int) -> int:
    def recursion(n):
        if n <= 1:
            return 1

        if number_of_ways[n] == 0:
            number_of_ways[n] = sum(recursion(n - i) for i in range(1, min(k, n) + 1))
        return number_of_ways[n]

    number_of_ways = [0] * (stairs + 1)
    return recursion(stairs)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_staircase.py',
                                       'number_of_traversals_staircase.tsv',
                                       number_of_ways_to_top))
