from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    largest_elements = []

    def find_k_largest_in_bst_helper(tree):
        if tree and len(largest_elements) < k:
            find_k_largest_in_bst_helper(tree.right)  # recursively reach the right most...
            if len(largest_elements) < k:
                largest_elements.append(tree.data)
                find_k_largest_in_bst_helper(tree.left)  # ... then go left... then repeat

    find_k_largest_in_bst_helper(tree)
    return largest_elements


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
