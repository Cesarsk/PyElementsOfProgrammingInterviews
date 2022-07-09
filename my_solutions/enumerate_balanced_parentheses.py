from typing import List

from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    def directed_building(num_left, num_right, valid_prefix, result=[]):
        if num_left > 0:
            directed_building(num_left - 1, num_right, valid_prefix + '(')

        if num_left < num_right:
            directed_building(num_left, num_right - 1, valid_prefix + ')')

        if num_right == 0:
            result.append(valid_prefix)

        return result

    return directed_building(num_pairs, num_pairs, '')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
