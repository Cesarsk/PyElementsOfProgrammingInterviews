import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    def __init__(self) -> None:
        self.d = -1
        self.edges: List[GraphVertex] = []


# Time complexity is the same as for BFS which is O(p+w) time complexity,
# w is the number of wires and O(p) is the space complexity
def is_any_placement_feasible(graph: List[GraphVertex]) -> bool:
    def bfs(s):
        s.d = 0
        q = collections.deque([s])

        while q:
            for t in q[0].edges:
                if t.d == -1:
                    t.d = q[0].d + 1  # increase by 1
                    q.append(t)  # add to queue
                elif t.d == q[0].d:
                    # condition not respected, returns false
                    return False

            del q[0]  # queue has one element at a time
        return True

    return all(bfs(v) for v in graph if v.d == -1)


@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_circuit_wirable.py',
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))
