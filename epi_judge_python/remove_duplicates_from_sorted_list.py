from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    iterator = L
    while iterator:
        next_distinct = iterator.next

        # determine how many duplicates we have
        while next_distinct and next_distinct.data == iterator.data:
            next_distinct = next_distinct.next

        # skip the duplicates and set the iterator.next to the value after the last duplicate
        iterator.next = next_distinct

        # saving steps by shifting the iterator directly to the next_distinct position
        iterator = next_distinct

    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
