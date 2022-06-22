import math
from typing import List

import bintrees

from test_framework import generic_test


class ABSqrt2:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.val = a + b * math.sqrt(2)

    def __eq__(self, other):
        return self.val == other.val

    def __lt__(self, other):
        return self.val < other.val


# uses a BST to generate the first numbers.
# The idea behind is to generate two elements at a time and add it to the collection,
# extracting the minimum from the BST every time
# complexity: O(k log k) space O(k), since there are no more than 2k insertions
def generate_first_k_a_b_sqrt2_rbtree(k: int) -> List[float]:
    candidates = bintrees.RBTree([
        (ABSqrt2(a=0, b=0), None)
    ])  # it's None because the interface of RBTree is [(k,v),(k1,v1),...]

    result = []

    # stop condition
    while len(result) < k:
        next_smallest = candidates.pop_min()[0]  # extract and add to the result
        result.append(next_smallest.val)  # append to the result the value of the object
        candidates[ABSqrt2(next_smallest.a + 1,
                           next_smallest.b)] = None  # same reason as above, we don't care about the value but the key instead
        candidates[ABSqrt2(next_smallest.a, next_smallest.b + 1)] = None

    return result


def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    cand = [ABSqrt2(0, 0)]

    i = j = 0

    for _ in range(1, k):
        i_cand = ABSqrt2(cand[i].a + 1, cand[i].b)
        j_cand = ABSqrt2(cand[j].a, cand[j].b + 1)

        cand.append(min(i_cand, j_cand))

        if cand[-1].val == i_cand.val:
            i += 1

        if cand[-1].val == j_cand.val:
            j += 1

    return [x.val for x in cand]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
