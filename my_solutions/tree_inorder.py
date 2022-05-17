from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    s = []
    result = []

    while s or tree:
        if tree:
            s.append(tree)
            # left side of the tree
            tree = tree.left
        else:
            # up side of the tree
            tree = s.pop()
            result.append(tree.data)
            # right side of the tree
            tree = tree.right

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
