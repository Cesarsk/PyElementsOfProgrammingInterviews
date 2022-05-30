from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# todo repeat this exercise
def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    # maps node to index
    node_to_inorder_idx = {node: i for i, node in enumerate(inorder)}

    # helper function that will be invoked in the recursive functions
    def binary_tree_from_preorder_inorder_helper(
            preorder_start, preorder_end,
            inorder_start, inorder_end):
        # end cannot be less than start
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None

        #
        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]

        #
        left_subtree_size = root_inorder_idx - inorder_start

        # BinaryTreeNode(data, left, right)
        return BinaryTreeNode(
            # data
            preorder[preorder_start],
            # left
            binary_tree_from_preorder_inorder_helper(
                preorder_start + 1,
                preorder_start + 1 + left_subtree_size,
                inorder_start,
                root_inorder_idx
            ),
            # right
            binary_tree_from_preorder_inorder_helper(
                preorder_start + 1 + left_subtree_size,
                preorder_end,
                root_inorder_idx + 1,
                inorder_end
            ))

    return binary_tree_from_preorder_inorder_helper(
        0, len(preorder), 0, len(inorder)
    )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
