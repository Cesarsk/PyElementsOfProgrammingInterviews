import heapq
from typing import List

from test_framework import generic_test, test_utils


# pythonic solution
def k_largest_in_binary_heap_python(A: List[int], k: int) -> List[int]:
    return heapq.nlargest(k, A)


# note for the reader: when you insert a tuple into a heap the first value is evaluated.
# That is why here the indices are put into the second element of a tuple, so that it's ordered by data value

# standard solution
def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    if k <= 0:
        return []

    candidate_max_heap = []

    # insert largest element at index 0
    candidate_max_heap.append((-A[0], 0))
    result = []

    for _ in range(k):
        # index
        candidate_idx = candidate_max_heap[0][1]

        # extract from the candidate_max_heap the element and insert it to result
        result.append(-heapq.heappop(candidate_max_heap)[0])

        # now let's take care of the left and right children, if they exist they're possible candidates

        # left child has index 2i+1, right child has index 2i+2
        left_child_idx = 2 * candidate_idx + 1
        right_child_idx = 2 * candidate_idx + 2

        # means the left child exists
        if left_child_idx < len(A):
            heapq.heappush(candidate_max_heap, (-A[left_child_idx], left_child_idx))

        if right_child_idx < len(A):
            heapq.heappush(candidate_max_heap, (-A[right_child_idx], right_child_idx))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
