import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

import is_list_cyclic as cycle
import do_terminated_lists_overlap as overlap


def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    # start of the cycle
    root0, root1 = cycle.has_cycle(l0), cycle.has_cycle(l1)

    # both with no cycle
    if not root0 and not root1:
        return overlap.overlapping_no_cycle_lists(l0, l1)

    # one of the two with cycles
    elif (root0 and not root1) or (root1 and not root0):
        # they cannot overlap in this case
        return None

    # both lists have cycles.
    temp = root1
    while temp:
        temp = temp.next
        if temp is root0 or temp is root1:
            break
    return root1 if temp is root0 else None


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
