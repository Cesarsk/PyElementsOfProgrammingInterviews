import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    WHITE, GRAY, BLACK = range(3)

    def __init__(self) -> None:
        self.edges: List['GraphVertex'] = []
        self.color = self.WHITE


# Time complexity is of DFS, which is O(|V|+|E|). Space is O(|V|)
def is_deadlocked(graph: List[GraphVertex]) -> bool:
    def has_cycle(cur):
        if cur.color == GraphVertex.GRAY:
            # if grey means a deadlock has been detected
            return True

        # start processing the vertex
        cur.color = GraphVertex.GRAY

        # check recursively the edges of the current node
        if any(next.color != GraphVertex.BLACK and has_cycle(next) for next in cur.edges):
            return True

        # stop processing the vertex
        cur.color = GraphVertex.BLACK

        return False

    # The goal is to detect if there's at least ONE cycle.
    return any(vertex.color == GraphVertex.WHITE and has_cycle(vertex) for vertex in graph)


@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError('Invalid num_nodes value')
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('deadlock_detection.py',
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))
