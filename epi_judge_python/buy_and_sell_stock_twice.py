from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    if not prices:
        return 0

    min_price, max_profit = float('inf'), 0
    first_profits = []

    # forward part: first buy-and-sell
    for stock in prices:
        min_price = min(min_price, stock)
        max_profit = max(max_profit, stock - min_price)
        first_profits.append(max_profit)

    max_price = float('-inf')
    # backwart part: second buy-and-sell
    for i in reversed(range(1, len(prices))):
        max_price = max(max_price, prices[i])
        max_profit = max(max_profit, first_profits[i - 1] + max_price - prices[i])

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
