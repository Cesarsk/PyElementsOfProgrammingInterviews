import functools
from typing import Optional

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size


def find_kth_node_binary_tree(tree: BinaryTreeNode, k: int) -> Optional[BinaryTreeNode]:
    while tree:
        # left_size is the number of nodes of the left subtree (including root)
        left_size = tree.left.size if tree.left else 0

        # this means it's not in the left-subtree but in the right so the right subtree must be explored
        # k >= L
        if left_size + 1 < k:
            # k is decreased because we are going into the direction of finding it
            k -= left_size + 1
            tree = tree.right

        # it's the solution of the problem
        elif left_size == k - 1:
            return tree

        # means it's in the left so keep exploring the left side
        else:
            tree = tree.left

    return None


@enable_executor_hook
def find_kth_node_binary_tree_wrapper(executor, tree, k):
    def init_size(node):
        if not node:
            return 0
        node.size = 1 + init_size(node.left) + init_size(node.right)
        return node.size

    init_size(tree)

    result = executor.run(functools.partial(find_kth_node_binary_tree, tree,
                                            k))

    if not result:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_node_in_tree.py',
                                       'kth_node_in_tree.tsv',
                                       find_kth_node_binary_tree_wrapper))
