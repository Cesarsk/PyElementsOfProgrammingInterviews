import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    def is_leaf(node):
        return not node.left and not node.right

    # computes the nodes from the root to the leftmost leaf followed by all the leaves in subtree
    def left_boundary_and_leaves(subtree, is_boundary):
        if not subtree:
            return []

        return (
                ([subtree] if is_boundary or is_leaf(subtree) else []) +
                left_boundary_and_leaves(subtree.left, is_boundary) +
                left_boundary_and_leaves(subtree.right, is_boundary and not subtree.left)
        )

    # computes the leaves in left-to-right order followed by the rightmost leaf to the root path in subtree
    def right_boundary_and_leaves(subtree, is_boundary):
        if not subtree:
            return []

        return (
                right_boundary_and_leaves(subtree.left, is_boundary and not subtree.right) +
                right_boundary_and_leaves(subtree.right, is_boundary) +
                ([subtree] if is_boundary or is_leaf(subtree) else [])
        )

    return (
        [tree] +
        left_boundary_and_leaves(tree.left, True) +
        right_boundary_and_leaves(tree.right, True) if tree else []
    )


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
