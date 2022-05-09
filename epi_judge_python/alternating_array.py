import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName, TestFailure
from test_framework.test_utils import enable_executor_hook


# O(n) time complexity
def rearrange(A: List[int]) -> None:
    for i in range(len(A) - 1):
        A[i:i + 2] = sorted(A[i:i + 2], reverse=bool(i % 2))

    return


"""
    head = 1
    for i in range(len(A) - 1):
        if i % 2 == 0:
            if A[i] <= A[head]:
                pass
            else:
                A[i], A[head] = A[head], A[i]
        else:
            if A[i] >= A[head]:
                pass
            else:
                A[i], A[head] = A[head], A[i]

        head += 1
"""


@enable_executor_hook
def rearrange_wrapper(executor, A):
    def check_answer(A):
        for i in range(len(A)):
            if i % 2:
                if A[i] < A[i - 1]:
                    raise TestFailure().with_property(
                        PropertyName.RESULT, A).with_mismatch_info(
                        i, 'A[{}] <= A[{}]'.format(i - 1, i),
                        '{} > {}'.format(A[i - 1], A[i]))
                if i + 1 < len(A):
                    if A[i] < A[i + 1]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                            i, 'A[{}] >= A[{}]'.format(i, i + 1),
                            '{} < {}'.format(A[i], A[i + 1]))
            else:
                if i > 0:
                    if A[i - 1] < A[i]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                            i, 'A[{}] >= A[{}]'.format(i - 1, i),
                            '{} < {}'.format(A[i - 1], A[i]))
                if i + 1 < len(A):
                    if A[i + 1] < A[i]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                            i, 'A[{}] <= A[{}]'.format(i, i + 1),
                            '{} > {}'.format(A[i], A[i + 1]))

    executor.run(functools.partial(rearrange, A))
    check_answer(A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('alternating_array.py',
                                       'alternating_array.tsv',
                                       rearrange_wrapper))
