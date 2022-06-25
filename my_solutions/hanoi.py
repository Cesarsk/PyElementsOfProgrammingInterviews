import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3


# Complexity is tricky. It's T(n-1)+1+T(n-1) which is the complexity
# from moving from A to C, and from C to B plus the single ring to move
# = 2*T(n-1)+1.
# This solves to O(2^n)
def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
    def tower_hanoi(num_rings_to_move, from_peg, to_peg, use_peg):
        if num_rings_to_move > 0:
            # start recursion with one less ring
            tower_hanoi(num_rings_to_move - 1, from_peg, use_peg, to_peg)

            # remove from from_peg
            removed_peg = pegs[from_peg].pop()
            # add to to_peg
            pegs[to_peg].append(removed_peg)

            # add to result the move above
            result.append([from_peg, to_peg])

            # once every ring has moved to use_peg, we move it to to_peg from the use_peg
            tower_hanoi(num_rings_to_move - 1, use_peg, to_peg, from_peg)

    # init pegs with num_rings
    result = []
    pegs = [list(reversed(range(1, num_rings + 1)))] \
           + [[] for _ in range(1, NUM_PEGS)]

    # starting recursion
    tower_hanoi(num_rings_to_move=num_rings,
                from_peg=0,
                to_peg=1,
                use_peg=2)

    return result


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure('Illegal move from {} to {}'.format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('hanoi.py', 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
