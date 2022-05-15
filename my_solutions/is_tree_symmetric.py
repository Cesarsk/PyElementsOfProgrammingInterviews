from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def check_symmetric(subtree_0, subtree_1):

        # if subtrees are empty means it's a symmetric root tree
        if not subtree_0 and not subtree_1:
            return True

        if subtree_0 and subtree_1:
            return (
                    subtree_0.data == subtree_1.data
                    and check_symmetric(subtree_0.left, subtree_1.right)
                    and check_symmetric(subtree_0.right, subtree_1.left)
            )

        return False

    # a empty tree is considered a symmetric tree
    if not tree:
        return True

    return check_symmetric(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
