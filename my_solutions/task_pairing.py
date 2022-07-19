import collections
from typing import List

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations: List[int]) -> List[PairedTasks]:
    task_durations.sort()

    # ~i means ~i = -i-1. i.e. ~0 = -1, ~1 = -2, etc...
    return [PairedTasks(task_durations[i], task_durations[~i]) for i in range(len(task_durations) // 2)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('task_pairing.py', 'task_pairing.tsv',
                                       optimum_task_assignment))
