from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from sorted_lists_merge import merge_two_sorted_lists


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    if not L or not L.next:
        return L

    pre_slow, slow, fast = None, L, L

    # when the fast iterator reaches the end means the slow iterator has reached the mid point of the array
    while fast and fast.next:
        pre_slow = slow
        slow = slow.next
        fast = fast.next.next

    pre_slow.next = None  # splits the list in two halves, L will be the first half and slow the second half

    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
