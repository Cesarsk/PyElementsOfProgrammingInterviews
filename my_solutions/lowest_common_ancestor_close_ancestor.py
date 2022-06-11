import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# Complexity is O(D0+D1) space and time,
# where D0 is the distance from the LCA to the first node, and D1 from the second node
def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    iter_0, iter_1 = node0, node1
    hash_table = set()

    while iter_0 or iter_1:
        if iter_0:
            # if it's present in the hash table we found the ancestor
            if iter_0 in hash_table:
                return iter_0

            hash_table.add(iter_0)
            iter_0 = iter_0.parent

        if iter_1:
            if iter_1 in hash_table:
                return iter_1

            hash_table.add(iter_1)
            iter_1 = iter_1.parent

    return None


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'lowest_common_ancestor_close_ancestor.py',
            'lowest_common_ancestor.tsv', lca_wrapper))
