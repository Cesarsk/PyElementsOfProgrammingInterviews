import functools
from typing import List, Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def generate_all_binary_trees(num_nodes: int) -> List[Optional[BinaryTreeNode]]:
    if num_nodes == 0:
        return [None]

    result = []

    for left in range(num_nodes):
        right = num_nodes - 1 - left

        # start recursive process
        left_subtrees = generate_all_binary_trees(left)
        right_subtrees = generate_all_binary_trees(right)

        result += [BinaryTreeNode(0, left, right) for left in left_subtrees for right in right_subtrees]

    return result


def serialize_structure(tree):
    result = []
    q = [tree]
    while q:
        a = q.pop(0)
        result.append(0 if not a else 1)
        if a:
            q.append(a.left)
            q.append(a.right)
    return result


@enable_executor_hook
def generate_all_binary_trees_wrapper(executor, num_nodes):
    result = executor.run(
        functools.partial(generate_all_binary_trees, num_nodes))

    return sorted(map(serialize_structure, result))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_trees.py',
                                       'enumerate_trees.tsv',
                                       generate_all_binary_trees_wrapper))
