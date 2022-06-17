import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    if not intervals:
        return []

    # sort by i.left.val (ascending, and i.left.is_closed first)
    # I think it's "not i.left.is_closed" because 0 = False and 1 = True
    # so 0 would come first if you don't put it first
    intervals.sort(key=lambda i: (i.left.val, not i.left.is_closed))
    print(intervals)

    # first result to add
    result = [intervals[0]]

    for i in intervals:
        # checking that the current interval
        # left value comes first than last evaluated right value
        # meaning they have one condition to intersect
        if i.left.val < result[-1].right.val \
                or (i.left.val == result[-1].right.val
                    and (i.left.is_closed or result[-1].right.is_closed)):
            # checking that the current interval
            # right value comes later than last evaluated right value
            # meaning they have the other condition to intersect
            if i.right.val > result[-1].right.val \
                    or (i.right.val == result[-1].right.val
                        and i.right.is_closed):
                result[-1] = Interval(result[-1].left, i.right)
        else:
            result.append(i)

    return result


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intervals_union.py',
                                       'intervals_union.tsv',
                                       union_of_intervals_wrapper))
