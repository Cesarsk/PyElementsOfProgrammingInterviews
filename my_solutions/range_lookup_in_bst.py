import collections
from typing import List

from bst_node import BstNode
from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst(tree: BstNode, interval: Interval) -> List[int]:
    def range_lookup_in_bst_helper(tree):
        if tree is None:
            return

        if interval.left <= tree.data <= interval.right:
            range_lookup_in_bst_helper(tree.left)
            result.append(tree.data)
            range_lookup_in_bst_helper(tree.right)
        elif tree.data < interval.left:
            range_lookup_in_bst_helper(tree.right)
        else:
            range_lookup_in_bst_helper(tree.left)

    result = []
    range_lookup_in_bst_helper(tree)
    return result


def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('range_lookup_in_bst.py',
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
