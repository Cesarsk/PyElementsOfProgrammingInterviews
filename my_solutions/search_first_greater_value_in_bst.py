from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    subtree, candidate = tree, None
    while subtree:
        if subtree.data > k:  # explore left sub-tree
            candidate = subtree  # set candidate every time we walk the left-subtree
            subtree = subtree.left
        else:  # explore right sub-tree
            subtree = subtree.right
    return candidate


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
