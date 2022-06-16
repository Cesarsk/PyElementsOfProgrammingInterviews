import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))

    E = [Endpoint(event.start, True) for event in A] + \
        [Endpoint(event.finish, False) for event in A]

    # order by ascending time, with is_start=true before is_start=false
    E.sort(key=lambda e: (e.time, not e.is_start))

    max_simultaneous, cur_simultaneous = 0, 0

    for e in E:
        if e.is_start:
            cur_simultaneous += 1
            max_simultaneous = max(max_simultaneous, cur_simultaneous)
        else:
            cur_simultaneous -= 1

    return max_simultaneous


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
