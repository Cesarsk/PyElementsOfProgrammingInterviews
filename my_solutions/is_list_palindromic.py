from list_node import ListNode
from test_framework import generic_test


def reverse_list(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    while head:
        dummy.next, head.next, head = head, dummy.next, head.next
    return dummy.next


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    slow = fast = L

    # scroll up to the end of the list
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    first_half_iter, second_half_iter = L, reverse_list(slow)

    while second_half_iter and first_half_iter:
        if second_half_iter.data != first_half_iter.data:
            return False
        second_half_iter, first_half_iter = second_half_iter.next, first_half_iter.next

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
