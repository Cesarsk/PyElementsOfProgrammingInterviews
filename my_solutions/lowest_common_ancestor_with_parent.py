import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # knowing the depth is a must to solve the problem
    def get_depth(node):
        depth = 0
        while node:
            depth += 1
            node = node.parent

        return depth

    # computing the nodes' depths
    depth0, depth1 = get_depth(node0), get_depth(node1)

    # move up the node that has a higher depth
    while depth0 != depth1:
        if depth0 < depth1:
            node1 = node1.parent
            depth1 -= 1
        else:
            node0 = node0.parent
            depth0 -= 1

    # now both have the same depth so...
    while node0 is not node1:
        node0, node1 = node0.parent, node1.parent

    # since LCA is the same, it doesn't make any difference which node to return
    return node0


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
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
