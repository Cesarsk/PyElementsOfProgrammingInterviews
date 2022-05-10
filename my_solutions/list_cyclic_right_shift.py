from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def find_tail(l):
    d = 1
    while l.next:
        d += 1
        l = l.next
    return l, d


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if L is None:
        return L

    # find the tail
    tail, length = find_tail(L)

    k %= length
    if k == 0:  # meaning equal to length
        return L

    # connect tail to head to make a cycle, it helps so we do not have to shift every element but only the tail and
    # reposition the head afterwards
    tail.next = L

    # i.e. k = 2 and length = 5, shifting 2 times to the right means shifting 5-2 times to the left, which is easier
    steps_to_new_head, new_tail = length - k, tail
    while steps_to_new_head:
        steps_to_new_head -= 1
        new_tail = new_tail.next

    # this is the head of the result
    new_head = new_tail.next

    # break the cycle
    new_tail.next = None
    return new_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
