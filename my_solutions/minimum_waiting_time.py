from typing import List

from test_framework import generic_test


def minimum_total_waiting_time_slower(service_times: List[int]) -> int:
    total_waiting_time = 0
    service_times.sort()
    for i in range(len(service_times)):
        for j in range(i):
            total_waiting_time += service_times[j]

    return total_waiting_time


# time is dominated by the time to sort which is O(n log n)
def minimum_total_waiting_time(service_times: List[int]) -> int:
    total_waiting_time = 0
    service_times.sort()
    for i, service_time in enumerate(service_times):
        num_remaining_queries = len(service_times) - (i + 1)
        total_waiting_time += service_time * num_remaining_queries

    return total_waiting_time


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_waiting_time.py',
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
