from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # tree is the root node
    path, result = [tree], []

    while path:
        curr = path.pop()
        if curr:
            # first right because left will be popped first
            path += [curr.right, curr.left]
            result.append(curr.data)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_preorder.py', 'tree_preorder.tsv',
                                       preorder_traversal))
