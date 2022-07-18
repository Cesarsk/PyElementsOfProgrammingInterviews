import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    def knapsack_helper(k, available_capacity):
        if k < 0:
            return 0

        # means unexplored subproblem
        if V[k][available_capacity] == -1:
            # not picking item so recalling the function with k-1
            without_item = knapsack_helper(k - 1, available_capacity)
            # picking item
            with_item = 0
            if available_capacity >= items[k].weight:
                with_item = items[k].value + knapsack_helper(k - 1, available_capacity - items[k].weight)

            V[k][available_capacity] = max(without_item, with_item)
        return V[k][available_capacity]

    V = [[-1] * (capacity + 1) for _ in items]
    return knapsack_helper(len(items) - 1, capacity)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
