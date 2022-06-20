import collections

import binary_tree_node
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst_alt(tree: BinaryTreeNode) -> bool:
    def recursive_check(tree, low=float('-inf'), high=float('inf')):
        if not tree:
            return True

        elif not low <= tree.data <= high:
            return False

        return recursive_check(tree.left, low, tree.data) and recursive_check(tree.right, tree.data, high)

    return recursive_check(tree)


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    QueueEntry = collections.namedtuple('QueueEntry', ('node', 'lower', 'upper'))
    queue = collections.deque([QueueEntry(tree, float('-inf'), float('inf'))])

    while queue:
        front = queue.popleft()
        if front.node:
            if not front.lower <= front.node.data <= front.upper:
                return False

            queue += [QueueEntry(front.node.left, front.lower, front.node.data),
                      QueueEntry(front.node.right, front.node.data, front.upper)]

    return True


def is_binary_tree_bst_inorder_traversal(tree):
    def inorder_traversal(tree):
        if not tree:
            return True
        elif not inorder_traversal(tree.left):
            return False
        elif prev[0] and prev[0].data > tree.data:
            return False
        prev[0] = tree
        return inorder_traversal(tree.right)

    prev = [None]
    return inorder_traversal(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
