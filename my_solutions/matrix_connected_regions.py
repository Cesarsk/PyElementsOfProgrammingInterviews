import collections
from typing import List

from test_framework import generic_test


# DFS recursive solution O(mn) time complexity
def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    color = image[x][y]  # store color
    image[x][y] = 1 - image[x][y]  # flips color

    for d in ((0, 1), (1, 0), (-1, 0), (0, -1)):

        # next cell
        next_x, next_y = x + d[0], y + d[1]

        if 0 <= next_x < len(image) and 0 <= next_y < len(image[next_x]):
            if image[next_x][next_y] == color:
                flip_color(next_x, next_y, image)

    return


# BFS iterative solution
def flip_color_bfs(x: int, y: int, image: List[List[bool]]) -> None:
    Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

    # store color
    color = image[x][y]

    # flips
    image[x][y] = 1 - image[x][y]

    # queue
    q = collections.deque([Coordinate(x, y)])

    while q:
        x, y = q.popleft()
        for d in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            next_x, next_y = x + d[0], y + d[1]

            if 0 <= next_x < len(image) and 0 <= next_y < len(image[next_x]):
                if image[next_x][next_y] == color:
                    image[next_x][next_y] = 1 - image[next_x][next_y]
                    q.append(Coordinate(next_x, next_y))


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
