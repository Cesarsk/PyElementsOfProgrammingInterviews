from typing import List

from test_framework import generic_test


def maximum_revenue(coins: List[int]) -> int:
    def compute_maximum_revenue_for_range(a, b):
        if a > b:  # no coins left
            return 0

        # means it's unexplored cell
        if maximum_revenue_for_range[a][b] == 0:
            max_revenue_picking_a = coins[a] + min(
                compute_maximum_revenue_for_range(a + 2, b),  # next player picks A
                compute_maximum_revenue_for_range(a + 1, b - 1)  # next player picks B
            )
            max_revenue_picking_b = coins[b] + min(
                compute_maximum_revenue_for_range(a, b - 2),  # next player picks B
                compute_maximum_revenue_for_range(a + 1, b - 1)  # next player picks A
            )
            maximum_revenue_for_range[a][b] = max(max_revenue_picking_a, max_revenue_picking_b)
        return maximum_revenue_for_range[a][b]

    maximum_revenue_for_range = [[0] * len(coins) for _ in coins]
    return compute_maximum_revenue_for_range(0, len(coins) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('picking_up_coins.py',
                                       'picking_up_coins.tsv',
                                       maximum_revenue))
