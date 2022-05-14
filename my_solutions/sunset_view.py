import collections
from typing import Iterator, List

from test_framework import generic_test


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    candidates = []
    Building = collections.namedtuple("Building", ("id", "height"))

    for index_building, height_building in enumerate(sequence):
        while candidates and height_building >= candidates[-1].height:
            candidates.pop()
        candidates.append(Building(index_building, height_building))

    return [i.id for i in reversed(candidates)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
