from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder_slower(preorder_sequence: List[int]) -> Optional[BstNode]:
    if not preorder_sequence:  # if sequence is empty return None
        return None

    # let's iterate over a generator
    transition_point = next(
        (i for i, a in enumerate(preorder_sequence) if a > preorder_sequence[0]), len(preorder_sequence)
    )

    return BstNode(
        preorder_sequence[0],  # node
        rebuild_bst_from_preorder_slower(preorder_sequence[1:transition_point]),  # left
        rebuild_bst_from_preorder_slower(preorder_sequence[transition_point:])  # right
    )


def rebuild_bst_from_preorder(preorder_sequence: List[int]) -> Optional[BstNode]:
    def rebuild_bst_from_preorder_on_value_range(lower_bound, upper_bound):
        if root_idx[0] == len(preorder_sequence):
            return None  # means we have explored all the steps

        root = preorder_sequence[root_idx[0]]  # get the element 0 of the list root_idx

        if not lower_bound <= root <= upper_bound:
            return None  # means the value can't be in this subtree or BST property would not be respected
        root_idx[0] += 1
        print(root_idx)

        left_subtree = rebuild_bst_from_preorder_on_value_range(lower_bound, root)
        right_subtree = rebuild_bst_from_preorder_on_value_range(root, upper_bound)

        return BstNode(root, left_subtree, right_subtree)

    root_idx = [0]  # tracks the current subtree. We use an integer masked
    # in a list so that it's available at all recursion levels
    return rebuild_bst_from_preorder_on_value_range(float('-inf'), float('inf'))  # start recursion


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
