import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def list_pivoting(l: ListNode, x: int) -> Optional[ListNode]:
    smaller, equal, bigger = ListNode(0), ListNode(0), ListNode(0)
    tail_s, tail_e, tail_b = smaller, equal, bigger

    while l:
        if x > l.data:
            # smaller
            tail_s.next = l
            tail_s = tail_s.next
        elif x == l.data:
            # equal
            tail_e.next = l
            tail_e = tail_e.next
        elif x < l.data:
            # bigger
            tail_b.next = l
            tail_b = tail_b.next
        l = l.next

    # attaching the three lists
    # you need to attach them from right to left because you may lose some connections otherwise in case some lists are null
    tail_e.next = bigger.next
    tail_s.next = equal.next
    tail_b.next = None

    print("result:", smaller.next)
    return smaller.next


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pivot_list.py', 'pivot_list.tsv',
                                       list_pivoting_wrapper))
