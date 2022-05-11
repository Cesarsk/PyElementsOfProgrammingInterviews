from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L:
        return L

    # create two linked lists
    even_dummy_head, odd_dummy_head = ListNode(0), ListNode(0)

    tails, turn = [even_dummy_head, odd_dummy_head], 0

    while L:
        tails[turn].next = L
        tails[turn] = tails[turn].next  # advance even/odd list
        L = L.next  # next item to evaluate
        turn ^= 1  # alternate 0 (even) and 1 (odd)

    # odd list end in None
    tails[1].next = None

    # merge even and odd lists
    tails[0].next = odd_dummy_head.next

    return even_dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
