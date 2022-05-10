import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    def length(list):
        size = 0
        while list:
            size += 1
            list = list.next

        return size

    def find_double_anchor(l1, l2):
        l1_len, l2_len = length(l1), length(l2)

        # we need to know which one is the longer list
        # we want L2 as the longest list
        if l1_len > l2_len:
            l1, l2 = l2, l1

        # advances the longer list to get equal length lists
        # so they start from the "same point"
        for _ in range(abs(l1_len - l2_len)):
            l2 = l2.next

        # advance in tandem both lists
        while l1 and l2 and l1 is not l2:
            l1, l2 = l1.next, l2.next

        return l1

    return find_double_anchor(l0, l1)


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
